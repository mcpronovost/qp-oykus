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
        document.title = `${r.name}`
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
        rpg.value.primary_color = "#89a411"
        let bhex = rpg.value.primary_color
        styletag.innerHTML = `:root{`
        styletag.innerHTML += `--qp-primary:${rpg.value.primary_color};`
        styletag.innerHTML += `--qp-primary-dark-1:${qpSlideHex(bhex, 21, "#1c1c1d")};`
        styletag.innerHTML += `--qp-primary-dark-2:${qpSlideHex(bhex, 42, "#1c1c1d")};`
        styletag.innerHTML += `--qp-primary-dark-3:${qpSlideHex(bhex, 63, "#1c1c1d")};`
        styletag.innerHTML += `--qp-primary-dark-4:${qpSlideHex(bhex, 84, "#1c1c1d")};`
        styletag.innerHTML += `--qp-primary-dark-5:${qpSlideHex(bhex, 105, "#1c1c1d")};`
        styletag.innerHTML += `--qp-primary-dark-6:${qpSlideHex(bhex, 126, "#1c1c1d")};`
        document.head.appendChild(styletag);
    }
    isLoading.value = false
}

const qpSlideHex = (colour: string, slide: number, bg: string) => {
    // ===---
    let bhex = colour.slice(1).match(/.{2}/g)
    let abg = bg.slice(1).match(/.{2}/g)
    if (bhex && abg) {
        let r: string|number = parseInt(bhex[0], 16)
        let g: string|number = parseInt(bhex[1], 16)
        let b: string|number = parseInt(bhex[2], 16)
        let br: string|number = parseInt(abg[0], 16)
        let bg: string|number = parseInt(abg[1], 16)
        let bb: string|number = parseInt(abg[2], 16)
        // ===---
        if (r > br) {r -= slide} else r += slide
        if (g > bg) {g -= slide} else g += slide
        if (b > bb) {b -= slide} else b += slide
        // ===---
        if (r > 255) r = 255
        else if (r < 28) r = 28
        if (g > 255) g = 255
        else if (g < 28) g = 28
        if (b > 255) b = 255
        else if (b < 29) b = 29
        // ===---
        r = r.toString(16)
        g = g.toString(16)
        b = b.toString(16)
        return `#${r}${g}${b}`
    } else {
        return colour
    }
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
    <footer v-if="rpg" class="qp-forum-footer">
        <div class="qp-forum-footer-wrapper">
            <small>
                <span v-text="`${rpg.copyright}`"></span>
            </small>
        </div>
    </footer>
    <qp-notfound v-else-if="!isLoading" />
</template>
