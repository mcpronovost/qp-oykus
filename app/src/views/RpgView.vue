<script setup lang="ts">
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import { ElMessage } from "element-plus";
import { API, HEADERS } from "../plugins/store/index";
import { storeUser } from "../plugins/store";
import QpRpgSidenav from "../components/rpg/RpgSidenav.vue";

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
        let bhex = rpg.value.primary_color
        styletag.innerHTML = `:root{`
        styletag.innerHTML += `--qp-primary:${rpg.value.primary_color};`
        styletag.innerHTML += `--qp-primary-dark-1:${qpSlideHex(bhex, 1, "#1c1c1d")};`
        styletag.innerHTML += `--qp-primary-dark-2:${qpSlideHex(bhex, 2, "#1c1c1d")};`
        styletag.innerHTML += `--qp-primary-dark-3:${qpSlideHex(bhex, 3, "#1c1c1d")};`
        styletag.innerHTML += `--qp-primary-dark-4:${qpSlideHex(bhex, 4, "#1c1c1d")};`
        styletag.innerHTML += `}`
        if (rpg.value.style) {
            styletag.innerHTML += rpg.value.style.stylesheet
        }
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
        let r_range = getRange(br, r, 6)
        let g_range = getRange(bg, g, 6)
        let b_range = getRange(bb, b, 6)
        r = r_range[slide].toString(16)
        g = g_range[slide].toString(16)
        b = b_range[slide].toString(16)
        return `#${r}${g}${b}`
    } else {
        return colour
    }
}

const getRange = (upper: number, lower: number, steps: number) => {
    const difference = upper - lower
    const increment = difference / (steps - 1)
    return [lower, ...Array(steps - 2).fill('').map((_, index) => 
        Math.ceil(lower + (increment * (index + 1)))
    ), upper]
}

onMounted(() => {doRpgDetail()})
</script>

<template>
    <qp-page :sidenav-title="rpg ? rpg.name : ''">
        <header v-if="rpg" class="rpg-forum-header">
            <div class="rpg-forum-header-wrapper">
                <div class="rpg-forum-header-content">
                    <h1 class="rpg-forum-header-title">
                        <span v-text="rpg.name"></span>
                    </h1>
                    <p v-if="rpg.caption" class="rpg-forum-header-caption" v-text="rpg.caption"></p>
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
        <template #sidenav>
            <QpRpgSidenav v-if="rpg" :rpg="rpg" />
        </template>
    </qp-page>
</template>
