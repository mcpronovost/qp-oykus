<script setup lang="ts">
import type { TypeProjectSimple } from "../../types/projects";
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRoute, useRouter } from "vue-router";
import { API, HEADERS } from "../../plugins/store/index";
import { storeUser } from "../../plugins/store";

const route = useRoute()
const router = useRouter()

const useStoreUser = storeUser()
const { rat, lang } = storeToRefs(useStoreUser)

const isLoading = ref<boolean>(true)
const hasError = ref<string|null>(null)

const project = ref<TypeProjectSimple|null>(null)

const getProject = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let f = await fetch(`${API}/projects/${route.params.slug}/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value),
    })
    if (f.status === 200) {
        let r = await f.json()
        project.value = r
        isLoading.value = false
    } else {
        isLoading.value = false
        hasError.value = `${f.status}`
    }
}

const doDeleteProject = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let f = await fetch(`${API}/projects/${route.params.slug}/delete/`, {
        method: "PATCH",
        headers: HEADERS(rat.value, lang.value),
    })
    if (f.status === 204) {
        router.push({name: "Projects"})
        isLoading.value = false
    } else {
        isLoading.value = false
        hasError.value = `${f.status}`
    }
}

onMounted(() => getProject())
</script>

<template>
    <div v-if="!isLoading && !hasError && project" class="qp-container">
        <qp-header :title="project.name" :content="project.caption" />
        <el-row>
            <el-col>
                <el-button @click="doDeleteProject()"></el-button>
            </el-col>
        </el-row>
    </div>
    <div v-else-if="!isLoading" class="qp-container qp-centered">
        <el-row>
            <el-col style="text-align:center;">
                <el-result :title="$t('Error')" :sub-title="$t('ContentNotFound')">
                    <template #icon>
                        <el-icon class="mdi mdi-emoticon-sad-outline" :size="120" />
                    </template>
                </el-result>
            </el-col>
        </el-row>
    </div>
</template>
