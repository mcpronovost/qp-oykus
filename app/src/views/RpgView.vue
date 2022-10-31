<script setup lang="ts">
import type { TypeProject } from "../types/projects";
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { ElMessage } from "element-plus";
import { API, HEADERS } from "../plugins/store/index";
import { storeUser } from "../plugins/store";

const useStoreUser = storeUser()
const { rat, lang } = storeToRefs(useStoreUser)

const isLoading = ref<boolean>(false)
const hasError = ref<string|null>(null)

const listRPGs = ref<Array<any>>([])

const doRpgList = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let f = await fetch(`${API}/rpg/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {
        let r = await f.json()
        listRPGs.value = r.results
        isLoading.value = false
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else ElMessage.error("AnErrorOccurred")
        isLoading.value = false
        hasError.value = `${f.status}`
    }
}

onMounted(() => {doRpgList()})
</script>

<template>
    <qp-page>
        <router-view :key="$route.fullPath" />
    </qp-page>
</template>
