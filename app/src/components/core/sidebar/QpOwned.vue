<script setup>
import { computed } from "vue";
import { storeToRefs } from "pinia";
import { storeUser } from "@/plugins/store";

const useStoreUser = storeUser()
const { owned_projects } = storeToRefs(useStoreUser)

const listProjects = computed(() => [...new Map([
    ...owned_projects.value
].map(item => [item["id"], item])).values()])
</script>

<template>
    <li v-for="(project, n) in listProjects" :key="`owned-project-${n}`" class="qp-sidebar-nav-list-item">
        <el-tooltip placement="left" :content="project.name">
            <el-button size="large" circle>
                <el-avatar :src="project.icon" :size="40" :style="`background-color:${project.icon ? 'transparent' : project.primary_color};color:#fff;`">
                    <span v-text="project.initial"></span>
                </el-avatar>
            </el-button>
        </el-tooltip>
    </li>
</template>