<template>
    <div class="relative z-50">
        <div class="navbar-container">
            <div class="navbar-logo-container">
                <RouterLink to="/">
                    <h1 class="main-title">PassDf</h1>
                </RouterLink>
            </div>
            <div class="navbar-icon-container">
                <div class="navbar-icon">
                    <RouterLink to="/login" v-if="!status">
                        <BIconBoxArrowInRight class="h-5 w-5 text-white" />
                    </RouterLink>
                </div>
                <div class="navbar-icon">
                    <RouterLink to="/signup" v-if="!status">
                        <BIconPlusSquare class="h-5 w-5 text-white" />
                    </RouterLink>
                </div>
                <div class="navbar-icon" v-if="status">
                    <p class="cursor-pointer" @click="logOut">
                        <BIconBoxArrowDownLeft class="h-5 w-5 text-white" />
                    </p>
                </div>
                <div class="navbar-icon">
                    <RouterLink to="/lections" v-if="status">
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
                <div class="navbar-text text-secondary" v-if="!status">
                    <RouterLink to="/login">
                        {{ $t("navbar.nav.login") }}
                    </RouterLink>
                </div>
                <div class="navbar-text text-secondary" v-if="!status">
                    <RouterLink to="/signup">
                        {{ $t("navbar.nav.signup") }}
                    </RouterLink>
                </div>
                <div class="navbar-text text-secondary" v-if="status">
                    <p class="cursor-pointer" @click="logOut">{{ $t("navbar.nav.logout") }}</p>
                </div>
                <div class="navbar-text text-secondary" v-if="status">
                    <RouterLink to="/lections">
                        {{ $t("navbar.nav.lections") }}
                    </RouterLink>
                </div>
                <div class="navbar-text text-secondary">
                    <a class="cursor-pointer" href="#download">{{ $t("navbar.nav.download") }}</a>
                </div>
                <div class="navbar-text text-secondary">
                    <a class="cursor-pointer" href="#aboutus">{{ $t("navbar.nav.aboutus") }}</a>
                </div>
                <div class="ml-auto mr-8 h-[100%] flex flex-row items-center">
                    <img src="https://cdn3.iconfinder.com/data/icons/flag-world/512/flags-06-512.png" alt="czech-flag"
                        class="w-4 h-4 mr-2">
                    <label class="relative inline-flex cursor-pointer items-center">
                        <input id="switch" type="checkbox" @click="changeLocale" class="peer sr-only" />
                        <label for="switch" class="hidden"></label>
                        <div class="language-switch peer peer-checked:bg-secondary border-none">
                        </div>
                    </label>
                    <img src="https://cdn-icons-png.flaticon.com/512/330/330536.png" alt="uk-flag" class="w-4 h-4 ml-2">
                </div>
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

const i18n = useI18n()

const status = ref(false);

const router = useRouter()

const supportedLocales = Tr.supportedLocales

let localeIndex = ref(0)

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

async function seeSession() {
    const localUser = await supabase.auth.getSession()
    console.log(localUser);
    console.log(status.value);
}

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