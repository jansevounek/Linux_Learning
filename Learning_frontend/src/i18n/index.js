// taken from https://lokalise.com/blog/vue-i18n/#Installing_and_configuring_the_Vue_I18n_plugin
import { createI18n } from "vue-i18n";
import en from "./locales/en.json";
import cz from "./locales/cz.json";

const Trans = {
    get supportedLocales() {
        return import.meta.env.VITE_SUPPORTED_LOCALES.split(",")
    }
}

export default createI18n({
    locale: import.meta.env.VITE_DEFAULT_LOCALE,
    fallbackLocale: import.meta.env.VITE_FALLBACK_LOCALE,
    legacy: false,
    globalInjection: true,
    messages: {
        en,
        cz
    },
    supportedLocales: Trans.supportedLocales,
})
