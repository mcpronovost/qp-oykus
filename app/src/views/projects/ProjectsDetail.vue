<script setup lang="ts">
import type { TypeProject } from "../../types/projects";
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useI18n } from "vue-i18n";
import { useRoute, useRouter } from "vue-router";
import { ElMessage } from "element-plus";
import { API, HEADERS } from "../../plugins/store/index";
import { storeUser } from "../../plugins/store";

const { t } = useI18n()

const route = useRoute()
const router = useRouter()

const useStoreUser = storeUser()
const { rat, lang, tz } = storeToRefs(useStoreUser)

const isLoading = ref<boolean>(true)
const hasError = ref<string|null>(null)

const project = ref<TypeProject|null>(null)

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
        ElMessage.success(t("Projectdeletedsuccessfully"))
        router.push({name: "Projects"})
        isLoading.value = false
    } else {
        isLoading.value = false
        ElMessage.error(t("Youdoesnthavetherighttodothat"))
    }
}

onMounted(() => getProject())
</script>

<template>
    <div v-if="!isLoading && !hasError && project" class="qp-container">
        <qp-header :title="project.name" :content="project.caption" />
        <el-row>
            <el-col>
                <pre>{{project.created_at}}</pre>
                <pre>qpdated ({{tz}}) : {{$f.qpdate(project.created_at, tz)}}</pre>
            </el-col>
        </el-row>
    </div>
    <qp-notfound v-else-if="!isLoading" />
</template>
