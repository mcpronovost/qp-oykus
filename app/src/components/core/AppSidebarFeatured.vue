<script setup lang="ts">
import type { TypeProject } from "../../types/projects";
import { onMounted, ref } from "vue";
import { storeToRefs } from "pinia";
import { storeUser } from "../../plugins/store";
import { API, HEADERS } from "../../plugins/store/index";

const useStoreUser = storeUser()
const { rat, lang } = storeToRefs(useStoreUser)

const listProjects = ref<Array<TypeProject>>([])

const getFeaturedProjects = async () => {
    let f = await fetch(`${API}/projects/list-featured/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {
        let r = await f.json()
        listProjects.value = r.results
    }
}

onMounted(() => {
    getFeaturedProjects()
})
</script>

<template>
    <li v-if="listProjects.length" class="qp-sidebar-nav-list-item">
        <el-icon size="large">
            <i class="mdi mdi-star-outline"></i>
        </el-icon>
    </li>
    <li v-for="(project, n) in listProjects" :key="`owned-project-${n}`" class="qp-sidebar-nav-list-item">
        <el-tooltip placement="left" :content="project.name">
            <el-button size="large" circle @click="$router.push({name:'ProjectsDetail', params:{slug:`${project.slug}`}})">
                <el-avatar :src="project.icon" :size="40" :style="`background-color:${project.icon ? 'transparent' : project.primary_color};color:#fff;`">
                    <span v-text="project.initial"></span>
                </el-avatar>
            </el-button>
        </el-tooltip>
    </li>
</template>