<template>
    <div v-if="sessionStarted">
        <input type="text" v-model="test_text">
        <button @click="testCommand" class="text-white">Submit</button>
    </div>
    <button v-if="!sessionStarted" class="text-white" @click="startSession">Start Session</button>
</template>

<script setup>
import { ref } from 'vue';

const test_text = ref('')
let sessionStarted = ref(false)

async function testCommand() {    
    const response = await fetch("http://127.0.0.1:5000/test/" + test_text.value);
    const command = await response.json()
    console.log(command.command)
}

async function startSession() {
    sessionStarted.value = !sessionStarted.value
    fetch("http://127.0.0.1:5000/start_session", {
        method: "post",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            allowed_commands: 'cd, ls, mkdir, rm, rm -r'
        })
    })
    
    .then( (response) => { 
        console.log("ok")
    });
}
</script>