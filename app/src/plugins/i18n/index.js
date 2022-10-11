import { createI18n  } from "vue-i18n";
import fr from "@/plugins/i18n/locales/fr.json";
import en from "@/plugins/i18n/locales/en.json";

const messages = {
    fr: fr,
    en: en
}

const i18n = createI18n({
    legacy: false,
    locale: "fr",
    fallbackLocale: "fr",
    messages
})

export default i18n;
