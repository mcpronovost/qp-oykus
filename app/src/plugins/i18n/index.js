import { createI18n  } from "vue-i18n";
import fr from "./locales/fr.json";

const messages = {
    fr: fr
}

const i18n = createI18n({
    legacy: false,
    locale: "fr",
    fallbackLocale: "fr",
    messages
})

export default i18n;
