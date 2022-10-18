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

const listForums = ref<Array<any>>([])

const doForumsList = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let f = await fetch(`${API}/forums/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {
        let r = await f.json()
        listForums.value = r.results
        isLoading.value = false
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else ElMessage.error("AnErrorOccurred")
        isLoading.value = false
        hasError.value = `${f.status}`
    }
}

const doForumsCreate = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let data = new FormData()
    data.append("name", "Qalatlán")
    data.append("slug", "qalatlan")
    data.append("owner", "1")
    // ===---
    let f = await fetch(`${API}/forums/create/`, {
        method: "POST",
        headers: HEADERS(rat.value, lang.value),
        body: data
    })
    if (f.status === 201) {
        let r = await f.json()
        listForums.value = [r]
        isLoading.value = false
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else ElMessage.error("AnErrorOccurred")
        isLoading.value = false
        hasError.value = `${f.status}`
    }
}

const doForumsDetail = async (pk: number) => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let f = await fetch(`${API}/forums/${pk}/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {
        let r = await f.json()
        listForums.value = [r]
        isLoading.value = false
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else ElMessage.error("AnErrorOccurred")
        isLoading.value = false
        hasError.value = `${f.status}`
    }
}

const doForumsDetailEdit = async (pk: number) => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let data = new FormData()
    data.append("name", "Qalatlán")
    data.append("slug", "qalatlan")
    data.append("owner", "1")
    // ===---
    let f = await fetch(`${API}/forums/${pk}/`, {
        method: "PATCH",
        headers: HEADERS(rat.value, lang.value),
        body: data
    })
    if (f.status === 200) {
        let r = await f.json()
        listForums.value = [r]
        isLoading.value = false
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
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
            <el-button :loading="isLoading" @click="doForumsList()">get forums</el-button>
            <el-button :loading="isLoading" @click="doForumsCreate()">create forums</el-button>
            <el-button :loading="isLoading" @click="doForumsDetail(1)">get forum 1</el-button>
            <el-button :loading="isLoading" @click="doForumsDetailEdit(1)">edit forum 1</el-button>
        </div>
        <div v-for="(forum, n) in listForums" :key="`forum-${n}`">
          <pre>{{ forum }}</pre>
        </div>
    </qp-page>
</template>
