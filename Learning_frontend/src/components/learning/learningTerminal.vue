<template>
    <div>
        <input type="text" v-model="test_text">
        <button @click="testCommand">Submit</button>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const test_text = ref('')

async function testCommand() {    
    const response = await fetch("http://127.0.0.1:5000/test/" + test_text.value);
    const command = await response.json()
    console.log(command.command)
}
</script>