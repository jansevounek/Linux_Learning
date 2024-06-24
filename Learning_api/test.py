import subprocess

result = subprocess.check_output('ls', shell = True, executable = "/bin/bash", stderr = subprocess.STDOUT)

print(result.partition)