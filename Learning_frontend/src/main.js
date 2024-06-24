import { createApp } from 'vue/dist/vue.esm-bundler'
import App from './App.vue'
import router from './router'
import './index.css'
import { BootstrapIconsPlugin } from 'bootstrap-icons-vue'
import { MotionPlugin } from '@vueuse/motion'
import i18n from "./i18n"

const app = createApp(App)

app.use(BootstrapIconsPlugin)

app.use(MotionPlugin)

app.use(i18n)

app.use(router)

app.mount('#app')
