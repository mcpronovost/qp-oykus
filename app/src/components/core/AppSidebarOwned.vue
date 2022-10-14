<script setup lang="ts">
import { storeToRefs } from "pinia";
import { storeUser } from "../../plugins/store";

const useStoreUser = storeUser()
const { owned_projects } = storeToRefs(useStoreUser)
</script>

<template>
    <li v-for="(project, n) in owned_projects" :key="`owned-project-${n}`" class="qp-sidebar-nav-list-item">
        <el-tooltip placement="left" :content="project.name">
            <el-button size="large" circle>
                <el-avatar :src="project.icon" :size="40" :style="`background-color:${project.icon ? 'transparent' : project.primary_color};color:#fff;`">
                    <span v-text="project.initial"></span>
                </el-avatar>
            </el-button>
        </el-tooltip>
    </li>
</template>