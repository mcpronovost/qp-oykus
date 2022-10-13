<script setup lang="ts">
const listProjects: Array<any> = []
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