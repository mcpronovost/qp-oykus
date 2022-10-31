<script setup lang="ts">
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import { ElMessage } from "element-plus";
import { API, HEADERS } from "../../plugins/store/index";
import { storeUser } from "../../plugins/store";

const route = useRoute()

const useStoreUser = storeUser()
const { rat, lang } = storeToRefs(useStoreUser)

const isLoading = ref<boolean>(false)
const hasError = ref<string|null>(null)

const rpg = ref<any>(null)

const doRpgDetail = async () => {
    isLoading.value = true
    hasError.value = null
    let slug = route.params.slug
    // ===---
    let f = await fetch(`${API}/rpg/${slug}/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {
        let r = await f.json()
        rpg.value = r
        initStyle()
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else if (f.status === 404) ElMessage.error("not found")
        else ElMessage.error("AnErrorOccurred")
        isLoading.value = false
        hasError.value = `${f.status}`
    }
}

const initStyle = () => {
    isLoading.value = true
    let styletag = document.getElementById("qp-custom-style");
    if (document.getElementById("qp-custom-style")) {
        styletag = document.getElementById("qp-custom-style")
    } else {
        styletag = document.createElement("style");
        styletag.setAttribute("id", "qp-custom-style");
    }
    if (styletag) {
        styletag.innerHTML = `:root{`
        styletag.innerHTML += `--qp-primary:${rpg.value.primary_color};`
        document.head.appendChild(styletag);
    }
    isLoading.value = false
}

onMounted(() => {doRpgDetail()})
</script>

<template>
    <header v-if="rpg" class="qp-forum-header">
        <div class="qp-forum-header-wrapper">
            <div class="qp-forum-header-content">
                <h1 class="qp-forum-header-title">
                    <span v-text="rpg.name"></span>
                </h1>
                <p v-if="rpg.caption" class="qp-forum-header-caption" v-text="rpg.caption"></p>
            </div>
        </div>
    </header>
    <router-view v-if="!isLoading && !hasError && rpg" :key="$route.fullPath" :rpg="rpg" />
    <qp-notfound v-else-if="!isLoading" />
</template>
