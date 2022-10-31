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

const doRpgCreate = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let data = new FormData()
    data.append("name", "Qalatlán")
    data.append("slug", "qalatlan")
    data.append("owner", "1")
    // ===---
    let f = await fetch(`${API}/rpg/create/`, {
        method: "POST",
        headers: HEADERS(rat.value, lang.value),
        body: data
    })
    if (f.status === 201) {
        let r = await f.json()
        listRPGs.value = [r]
        isLoading.value = false
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else ElMessage.error("AnErrorOccurred")
        isLoading.value = false
        hasError.value = `${f.status}`
    }
}

const doRpgDetail = async (slug: string) => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let f = await fetch(`${API}/rpg/${slug}/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {
        let r = await f.json()
        listRPGs.value = [r]
        isLoading.value = false
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else if (f.status === 404) ElMessage.error("not found")
        else ElMessage.error("AnErrorOccurred")
        isLoading.value = false
        hasError.value = `${f.status}`
    }
}

const doRpgDetailEdit = async (slug: string) => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let data = new FormData()
    data.append("name", "Qalatlán")
    data.append("slug", "qalatlan")
    data.append("owner", "1")
    // ===---
    let f = await fetch(`${API}/rpg/${slug}/`, {
        method: "PATCH",
        headers: HEADERS(rat.value, lang.value),
        body: data
    })
    if (f.status === 200) {
        let r = await f.json()
        listRPGs.value = [r]
        isLoading.value = false
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else if (f.status === 404) ElMessage.error("not found")
        else ElMessage.error("AnErrorOccurred")
        isLoading.value = false
        hasError.value = `${f.status}`
    }
}

onMounted(() => {console.log("ready")})
</script>

<template>
    <qp-page>
        <div>
            <el-button :loading="isLoading" @click="doRpgList()">get all rpg</el-button>
            <el-button :loading="isLoading" @click="doRpgCreate()">create rpg</el-button>
            <el-button :loading="isLoading" @click="doRpgDetail('1')">get rpg 1</el-button>
            <el-button :loading="isLoading" @click="doRpgDetailEdit('1')">edit rpg 1</el-button>
        </div>
        <div v-for="(rpg, n) in listRPGs" :key="`rpg-${n}`">
          <pre>{{ rpg }}</pre>
        </div>
    </qp-page>
</template>
