<script setup>
import { reactive, ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import { API, HEADERS } from "@/plugins/store/index";
import { storeUser } from "@/plugins/store";

const route = useRoute()

const useStoreUser = storeUser()
const { rat, lang } = storeToRefs(useStoreUser)

const isLoading = ref(true)
const hasError = ref(null)

const project = ref(null)

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
        hasError.value = 404
    }
}

onMounted(() => getProject())
</script>

<template>
    <qp-page v-loading="isLoading" :sidenav-title="$t('Project')">
        <div v-if="!isLoading && !hasError && project" class="qp-container">
            <el-row>
                <el-col>
                    <qp-header :title="project.name" :content="project.caption" />
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
    </qp-page>
</template>
