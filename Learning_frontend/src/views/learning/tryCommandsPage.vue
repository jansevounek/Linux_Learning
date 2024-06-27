<template>
    <div class="relative top-12 flex flex-col h-screen w-[100%] justify-start">
        <div class="text-tertiary mx-4 mt-4">
            <h1 class="text-[20px] underline">{{ $t("learning.trycommands.header") }}</h1>
            <br>
            <p>{{ $t("learning.trycommands.text1") }}</p>
            <br>
            <p>{{ $t("learning.trycommands.text2") }}</p>
        </div>

        <hr class="bg-primary border-primary mt-4 mx-4">

        <div class="flex flex-col text-primary mx-4 mt-4" v-if="!startedSession">
            <p>{{ $t("learning.trycommands.textsession") }}</p>
            <div class="text-primary flex flex-row">
                <p>"start session":</p>
                <form action="" @submit.prevent="startSession">
                    <input type="text" class="bg-inherit ml-2 outline-none" v-model="start_session_input">
                    <button class="relative md:hidden">{{ $t("learning.trycommands.button") }}</button>
                </form>
            </div>
        </div>
        <learningTerminal v-if="startedSession"/>
    </div>
</template>

<script setup>
import learningTerminal from "../../components/learning/learningTerminal.vue";
import { ref } from "vue";

let startedSession = ref(false)

const start_session_input = ref('')

function startSession() {
    if (start_session_input.value === "start session") {
        startedSession.value = true
    }
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