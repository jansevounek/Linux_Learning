from flask import Flask, jsonify, request
import subprocess
from flask_cors import CORS
import json
import docker
import io


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/test/<command>', methods=['GET'])
def execute_command(command):
    result = subprocess.check_output(command, shell = True, executable = "/bin/bash", stderr = subprocess.STDOUT)
    rs = result.decode('utf-8')
    return jsonify({'command': rs})

#Route that starts a session
#(It starts a docker container that a user can use)
@app.route('/start_session', methods=['POST'])
def start_session():
    data = request.get_json()

    dump_commands_into_json_file(data)

    start_docker_container()

    return jsonify({'success': 'success'})

#Puts commands allowed in the container into the json config file
#TODO add data
def dump_commands_into_json_file(data):
    # taken from https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/
    cm = ['/bin/ls', '/bin/mkdir']

    commands = {
        'allowed_commands' : cm
    }

    json_object = json.dumps(commands, indent=1)

    with open("docker/commands.json", "w") as outfile:
        outfile.write(json_object)

def start_docker_container():
    client = docker.from_env()

    #Generated by chatgpt question: 
    #file start 
    #FROM alpine:latest
    #RUN apk update && apk add --no-cache bash sudo jq
    #COPY commands.json /etc/commands.json
    #RUN adduser -D user
    #RUN jq -r '.allowed_commands[] | "user ALL=(ALL) NOPASSWD: \(.);"' /etc/commands.json >> /etc/sudoers
    #USER user
    #CMD ["/bin/bash"]
    #file end 
    #Could you rewrite me this file in python docker plugin
    # Initialize the Docker client
    client = docker.from_env()

    base_image = 'alpine:latest'

    packages = ['bash', 'sudo', 'jq']

    json_file = 'commands.json'

    sudoers_content = ''

    with open(json_file, 'r') as f:
        import json
        commands = json.load(f)
        for command in commands['allowed_commands']:
            sudoers_content += f"user ALL=(ALL) NOPASSWD: {command};\n"

    dockerfile_content = (
        "FROM {}\n"
        "RUN apk update && apk add --no-cache {}\n"
        "COPY {} /etc/{}\n"
        "RUN adduser -D user\n"
        "RUN echo '{}' >> /etc/sudoers\n"
        "USER user\n"
        "CMD [\"/bin/bash\"]\n"
    ).format(base_image, ' '.join(packages), json_file, json_file, sudoers_content)

    fileobj = io.BytesIO(dockerfile_content.encode('utf-8'))

    client.images.build(
        fileobj=fileobj,
        rm=True
    )
    

if __name__ == '__main__':
    app.run()