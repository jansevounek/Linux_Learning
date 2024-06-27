<template>
    <div class="flex flex-col text-primary mx-4 mt-4">
        <div class="whitespace-pre-line">{{ console_output }}</div>
        <div class="flex flex-row text-primary">
            <p>user@ubuntu:~$</p>
            <form action="" @submit.prevent="testCommand">
                <input type="text" class="bg-inherit ml-2 outline-none" v-model="test_text">
                <button class="relative md:hidden">Execute</button>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';

const test_text = ref('')
const console_output = ref('')

async function testCommand() {
    if (test_text.value == "clear") {
        console_output.value = ''
        test_text.value = ""
    } else {
        const response = await fetch("http://127.0.0.1:5000/test/" + test_text.value);
        const command = await response.json()
        console_output.value += 'user@ubuntu:~$ \n' + command.command
        test_text.value = ""
    }
}

</script>