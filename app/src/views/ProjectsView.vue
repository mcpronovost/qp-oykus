<script setup lang="ts">
import type { TypeProjectSimple } from "../types/projects";
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { API, HEADERS } from "../plugins/store/index";
import { storeUser } from "../plugins/store";
import QpProjectsSidenav from "../components/projects/ProjectsSidenav.vue";

const useStoreUser = storeUser()
const { rat, lang } = storeToRefs(useStoreUser)

const isLoading = ref<boolean>(true)
const hasError = ref<string|null>(null)

const listProjects = ref<Array<TypeProjectSimple>>([])

const getProjects = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let f = await fetch(`${API}/projects/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value),
    })
    if (f.status === 200) {
        let r = await f.json()
        listProjects.value = r.results
        isLoading.value = false
    } else {
        isLoading.value = false
        hasError.value = `${f.status}`
    }
}

onMounted(() => getProjects())
</script>

<template>
    <qp-page :sidenav-title="$t('Projects')">
        <router-view :key="$route.fullPath" :projects="listProjects" />
        <template #sidenav>
            <QpProjectsSidenav :projects="listProjects" />
        </template>
    </qp-page>
</template>
