<template>
    <div class="h-screen w-screen flex justify-center z-0">
        <div class="login-container">
            <h1 class="text-[50px] h-28 main-title">
                <VueTypewriterEffect :strings="['Log into your account!', 'Log in!']" />
            </h1>
            <LoginSignupSocials />
            <form action="">
                <input type="text" class="log-in-form w-[100%] text-white" placeholder="Email"
                    v-motion-slide-visible-once-left v-model="email"
                    :class="isEmailValid === false ? 'wrong-email' : 'text-green-600'">
                <div class="flex flex-row">
                    <input :type="showPassword === true ? 'text' : 'password'" class="log-in-form w-[80%]"
                        placeholder="Password" v-motion-slide-visible-once-right v-model="password">
                    <div class="show-password-button" @click="showPassword = !showPassword">
                        <BIconEye v-if="!showPassword" />
                        <BIconEyeSlash v-if="showPassword" />
                    </div>
                </div>
            </form>
            <div class="relative w-[100%] flex flex-col justify-center mt-5">
                <button class="download-button h-10" v-motion-slide-visible-once-left @click="logIn" type="submit">{{
                    $t("login.button1") }}</button>
                <RouterLink to="/signup">
                    <button class="download-button h-10 w-48 mt-4 text-nowrap" v-motion-slide-visible-once-right>
                        {{ $t("login.button2") }}
                    </button>
                </RouterLink>
            </div>
        </div>
    </div>
</template>

<script setup>
import VueTypewriterEffect from "vue-typewriter-effect";
import { ref, computed } from 'vue'
import LoginSignupSocials from '../../components/login-signup/LoginSignupSocials.vue'
import { supabase } from '../../supabase/init'
import { useRouter } from 'vue-router'

const router = useRouter()

const showPassword = ref(false)

const password = ref('')
const email = ref('')

const isEmailValid = computed(() => {
    if (email.value === '') {
        return true
    }
    return /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1, 3}\.[0-9]{1, 3}\.[0-9]{1, 3}\.[0-9]{1, 3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email.value)
})

async function logIn() {
    const { data, error } = await supabase.auth.signInWithPassword({
        email: email.value,
        password: password.value,
    })
    if (error) {
        alert(error.message)
    } else {
        router.push('/')
        location.reload()
    }
}

function loginWithGoogle() {
    supabase.auth.signInWithOAuth({
        provider: 'google',
    })
}
</script>