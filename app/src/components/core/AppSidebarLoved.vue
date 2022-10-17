<script setup lang="ts">
import type { TypeProject } from "../../types/projects";
import { computed } from "vue";

const listProjects = computed<Array<TypeProject>>(() => [])
</script>

<template>
    <li v-if="listProjects.length" class="qp-sidebar-nav-list-item">
        <el-icon size="large">
            <i class="mdi mdi-heart-outline"></i>
        </el-icon>
    </li>
    <li v-for="(project, n) in listProjects" :key="`loved-project-${n}`" class="qp-sidebar-nav-list-item">
        <el-tooltip placement="left" :content="project.name">
            <el-button size="large" circle @click="$router.push({name:'ProjectsDetail', params:{slug:`${project.slug}`}})">
                <el-avatar :src="project.icon" :size="40" :style="`background-color:${project.icon ? 'transparent' : project.primary_color};color:#fff;`">
                    <span v-text="project.initial"></span>
                </el-avatar>
            </el-button>
        </el-tooltip>
    </li>
</template>