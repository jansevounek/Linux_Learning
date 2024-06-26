<template>
    <div class="h-screen w-screen flex justify-center">
        <div class="signup-container">
            <h1 class="text-[50px] h-28 main-title">
                <VueTypewriterEffect :strings="['Create a new account!', 'Sign up!']" />
            </h1>
            <LoginSignupSocials />
            <form action="">
                <span class="signup-error-msg" v-if="emailErrorMsg">{{ $t("signup.errormsg.email") }}</span>

                <input type="text" class="log-in-form mt-5 text-white" placeholder="Email"
                    v-motion-slide-visible-once-left v-model="email"
                    :class="isEmailValid === false ? 'wrong-email' : ''">

                <span class="signup-error-msg" v-if="password1ErrorMsg">{{ $t("signup.errormsg.password1") }}</span>
                <br v-if="password2ErrorMsg && password1ErrorMsg">
                <span class="signup-error-msg" v-if="password2ErrorMsg">{{ $t("signup.errormsg.password2") }}</span>

                <input :type="showPassword === true ? 'text' : 'password'" class="log-in-form" placeholder="Password"
                    v-motion-slide-visible-once-right v-model="password">
                <div class="flex flex-row">
                    <input :type="showPassword === true ? 'text' : 'password'" class="log-in-form w-[80%]"
                        placeholder="Repeat the password" v-motion-slide-visible-once-right v-model="repeat_password">
                    <div class="show-password-button" @click="showPassword = !showPassword">
                        <BIconEye v-if="!showPassword" />
                        <BIconEyeSlash v-if="showPassword" />
                    </div>
                </div>
            </form>
            <div class="flex relative flex-row mb-2 h-10 w-[100%] justify-end items-center">
                <span class="password-strength-box" :class="strengthLevel > 1 ? 'password-strength-1' : ''">
                </span>
                <span class="password-strength-box" :class="strengthLevel > 2 ? 'password-strength-2' : ''">
                </span>
                <span class="password-strength-box" :class="strengthLevel > 3 ? 'password-strength-3' : ''">
                </span>
                <span class="password-strength-box" :class="strengthLevel > 4 ? 'password-strength-4' : ''">
                </span>
            </div>
            <div class="relative w-[100%] flex justify-center mt-8">
                <button class="download-button w-40 h-10" @click="createAccount" v-motion-slide-visible-once-left>
                    {{ $t("signup.button1") }}
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import VueTypewriterEffect from "vue-typewriter-effect";
import { ref, computed } from 'vue'
import { supabase } from '../../supabase/init'
import { useRouter } from 'vue-router'
import LoginSignupSocials from '../../components/login-signup/LoginSignupSocials.vue'

const showPassword = ref(false)

const router = useRouter()

let emailErrorMsg = ref(false)
let password1ErrorMsg = ref(false)
let password2ErrorMsg = ref(false)

const password = ref('')
const email = ref('')
const repeat_password = ref('')

const isEmailValid = computed(() => {
    if (email.value === '') {
        return true
    }
    return /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1, 3}\.[0-9]{1, 3}\.[0-9]{1, 3}\.[0-9]{1, 3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email.value)
})

const passwordStrength = computed(() => {
    let score = 0

    let letters = {}
    for (let i = 0; i < password.value.length; i++) {
        letters[password.value[i]] = (letters[password.value[i]] || 0) + 1
        score += 5.0 / letters[password.value[i]]
    }

    let variations = {
        digits: /\d/.test(password.value),
        lower: /[a-z]/.test(password.value),
        upper: /[A-Z]/.test(password.value),
        nonWords: /\W/.test(password.value),
    };

    let variationCount = 0;
    for (let check in variations) {
        variationCount += (variations[check] === true) ? 1 : 0;
    }

    score += ((variationCount - 1) * 10);

    return parseInt(score)
})

const strengthLevel = computed(() => {
    if (passwordStrength.value < 20) {
        return 1
    } else if (passwordStrength.value < 40) {
        return 2
    } else if (passwordStrength.value < 60) {
        return 3
    } else if (passwordStrength.value < 75) {
        return 4
    } else {
        return 5
    }
})

async function createAccount() {
    if (email.value.length < 3 || !isEmailValid.value) {
        emailErrorMsg.value = true
    } else {
        emailErrorMsg.value = false
    }

    if (password.value != repeat_password.value) {
        password1ErrorMsg.value = true
    } else {
        password1ErrorMsg.value = false
    }

    if (strengthLevel.value != 5) {
        password2ErrorMsg.value = true
    } else {
        password2ErrorMsg.value = false
    }

    if (password.value === repeat_password.value && strengthLevel.value == 5 && isEmailValid.value && email.value.length > 2) {
        const { data, error } = await supabase.auth.signUp({
            email: email.value,
            password: password.value
        })
        if (error) {
            console.log(error)
        } else {
            console.log(data)
            router.push('/')
            location.reload()
        }
    }
}

function loginWithGoogle() {
    supabase.auth.signInWithOAuth({
        provider: 'google',
    })
}
</script>