import { BIconBoxArrowRight } from 'bootstrap-icons-vue';

import { BIconPlusSquare } from 'bootstrap-icons-vue';

import { BIconBoxes } from 'bootstrap-icons-vue';

import { BIconBoxArrowInRight } from 'bootstrap-icons-vue';

import { BIconBoxArrowRight } from 'bootstrap-icons-vue';

import { BIconHouse } from 'bootstrap-icons-vue';

import { BIconSearch } from 'bootstrap-icons-vue';

import { BIcon0Circle } from 'bootstrap-icons-vue';
<template>
    <div class="bg-primary h-12 w-screen flex flex-row fixed z-50">
        <div class="navbar-logo-container">
            <RouterLink to="/">
                <h1 class="main-title text-white">PassDf</h1>
            </RouterLink>
        </div>
        <div class="navbar-icon-container">
            <div class="navbar-icon" v-if="!status">
                <RouterLink to="/login">
                    <BIconBoxArrowInRight class="h-5 w-5 text-white" />
                </RouterLink>
            </div>
            <div class="navbar-icon" v-if="!status">
                <RouterLink to="/signup">
                    <BIconPlusSquare class="h-5 w-5 text-white" />
                </RouterLink>
            </div>
            <div class="navbar-icon" v-if="status">
                <p class="cursor-pointer" @click="logOut">
                    <BIconBoxArrowDownLeft class="h-5 w-5 text-white" />
                </p>
            </div>
            <div class="navbar-icon" v-if="status">
                <RouterLink to="/lections">
                    <BIconBook class="h-5 w-5 text-white" />
                </RouterLink>
            </div>
            <div class="navbar-icon">
                <button @click="changeLocale" class="language-button">
                    <BIconTranslate class="h-5 w-5 text-white" />
                </button>
            </div>
            <div class="navbar-icon" @click="handleNavBarExpand">
                <BIconList class="h-5 w-5 text-white" />
            </div>
        </div>
        <div class="navbar-text-container">
            <div class="navbar-text">
                <RouterLink to="/">
                    {{ $t("navbar.nav.home") }}
                </RouterLink>
            </div>
            <div class="navbar-text" v-if="!status">
                <RouterLink to="/signup">
                    {{ $t("navbar.nav.signup") }}
                </RouterLink>
            </div>
            <div class="navbar-text" v-if="!status">
                <RouterLink to="/login">
                    {{ $t("navbar.nav.login") }}
                </RouterLink>
            </div>
            <div class="navbar-text" v-if="status">
                <RouterLink to="/lections">
                    {{ $t("navbar.nav.lections") }}
                </RouterLink>
            </div>
            <div class="navbar-text" v-if="status">
                <p class="cursor-pointer" @click="logOut">{{ $t("navbar.nav.logout") }}</p>
            </div>
            <div class="ml-auto mr-8 h-[100%] flex flex-row items-center">
                <img src="https://cdn3.iconfinder.com/data/icons/flag-world/512/flags-06-512.png" alt="czech-flag"
                    class="w-4 h-4 mr-2">
                <label class="relative inline-flex cursor-pointer items-center">
                    <input id="switch" type="checkbox" @click="changeLocale" class="peer sr-only" />
                    <label for="switch" class="hidden"></label>
                    <div class="language-switch peer peer-checked:bg-tertiary border-none">
                    </div>
                </label>
                <img src="https://cdn-icons-png.flaticon.com/512/330/330536.png" alt="uk-flag" class="w-4 h-4 ml-2">
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue'
import { RouterLink } from 'vue-router';
import Tr from "@/i18n/translation"
import { useI18n } from 'vue-i18n'
import { supabase } from '@/supabase/init';
import { useRouter } from 'vue-router'

const router = useRouter()

// Changing languages
const i18n = useI18n()
let localeIndex = ref(0)
const supportedLocales = Tr.supportedLocales

const status = ref(false);

const changeLocale = () => {
    localeIndex.value = (localeIndex.value + 1) % supportedLocales.length
    i18n.locale.value = supportedLocales[localeIndex.value]
}

watchEffect(async () => {
    const localUser = await supabase.auth.getSession()
    if (localUser.data.session) {
        status.value = true
    } else {
        status.value = false
    }
});

async function logOut() {
    const { error } = await supabase.auth.signOut();
    if (error) {
        console.log(error.message)
    } else {
        router.push('/')
        location.reload()
    }
}
</script>

<style></style>