import { createApp } from "vue";
import App from "./App.vue";
import i18n from "./plugins/i18n";
import router from "./plugins/router";
import store from "./plugins/store";
import ElementPlus from "element-plus";
import fr from "element-plus/es/locale/lang/fr";
import "element-plus/dist/index.css";
import "@mdi/font/css/materialdesignicons.min.css";
import "@fontsource/nunito/400.css";
import "@fontsource/nunito/600.css";
import "@fontsource/quicksand/300.css";
import "@fontsource/quicksand/400.css";
import "@fontsource/quicksand/600.css";
import "@/assets/css/element.css";
import "@/assets/css/style.css";

import QpPage from "@/components/BasePage.vue";
import QpHeader from "@/components/BaseHeader.vue";

const app = createApp(App);

app.component("QpPage", QpPage);
app.component("QpHeader", QpHeader);

app.use(i18n);
app.use(router);
app.use(store);
app.use(ElementPlus, {
    locale: fr,
})

app.mount("#app");
