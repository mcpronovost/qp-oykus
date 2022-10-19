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
const listCategories = ref<Array<any>>([])
const listSections = ref<Array<any>>([])
const listTopics = ref<Array<any>>([])
const listMessages = ref<Array<any>>([])

const doForumsList = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let f = await fetch(`${API}/forums/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    .then((r) => {return r})
    .catch(() => {return new Response(null,{status: 400})})
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
    .then((r) => {return r})
    .catch(() => {return new Response(null,{status: 400})})
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
    .then((r) => {return r})
    .catch(() => {return new Response(null,{status: 400})})
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
    .then((r) => {return r})
    .catch(() => {return new Response(null,{status: 400})})
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

const doForumsCategoriesList = async (pk: number) => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let f = await fetch(`${API}/forums/${pk}/categories/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    .then((r) => {return r})
    .catch(() => {return new Response(null,{status: 400})})
    if (f.status === 200) {
        let r = await f.json()
        listCategories.value = r.results
        isLoading.value = false
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else ElMessage.error("AnErrorOccurred")
        hasError.value = `${f.status}`
        isLoading.value = false
    }
}

const doForumsSectionsList = async (pk: number) => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let f = await fetch(`${API}/forums/${pk}/sections/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    .then((r) => {return r})
    .catch(() => {return new Response(null,{status: 400})})
    if (f.status === 200) {
        let r = await f.json()
        listSections.value = r.results
        isLoading.value = false
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else ElMessage.error("AnErrorOccurred")
        hasError.value = `${f.status}`
        isLoading.value = false
    }
}

const doForumsTopicsList = async (pk: number) => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let f = await fetch(`${API}/forums/${pk}/topics/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    .then((r) => {return r})
    .catch(() => {return new Response(null,{status: 400})})
    if (f.status === 200) {
        let r = await f.json()
        listTopics.value = r.results
        isLoading.value = false
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else ElMessage.error("AnErrorOccurred")
        hasError.value = `${f.status}`
        isLoading.value = false
    }
}

const doForumsMessagesList = async (pk: number) => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let f = await fetch(`${API}/forums/${pk}/messages/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    .then((r) => {return r})
    .catch(() => {return new Response(null,{status: 400})})
    if (f.status === 200) {
        let r = await f.json()
        listMessages.value = r.results
        isLoading.value = false
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else ElMessage.error("AnErrorOccurred")
        hasError.value = `${f.status}`
        isLoading.value = false
    }
}

const doClear = () => {
    listForums.value = []
    listCategories.value = []
    listSections.value = []
    listTopics.value = []
    listMessages.value = []
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
            <el-button :loading="isLoading" @click="doClear()">clear</el-button>
        </div>
        <div>
            <el-button :loading="isLoading" @click="doForumsCategoriesList(1)">get categories of forum 1</el-button>
            <el-button :loading="isLoading" @click="doForumsSectionsList(1)">get sections of forum 1</el-button>
            <el-button :loading="isLoading" @click="doForumsTopicsList(1)">get topics of forum 1</el-button>
            <el-button :loading="isLoading" @click="doForumsMessagesList(1)">get messages of forum 1</el-button>
        </div>
        <h2>Forum</h2>
        <div v-for="(forum, n) in listForums" :key="`forum-${n}`">
            <pre>{{ forum }}</pre>
        </div>
        <h2>Categories</h2>
        <div v-for="(category, n) in listCategories" :key="`category-${n}`">
            <pre>{{ category }}</pre>
        </div>
        <h2>Sections</h2>
        <div v-for="(section, n) in listSections" :key="`section-${n}`">
            <pre>{{ section }}</pre>
        </div>
        <h2>Topics</h2>
        <div v-for="(topic, n) in listTopics" :key="`topic-${n}`">
            <pre>{{ topic }}</pre>
        </div>
        <h2>Messages</h2>
        <div v-for="(message, n) in listMessages" :key="`message-${n}`">
            <pre>{{ message }}</pre>
        </div>
    </qp-page>
</template>
