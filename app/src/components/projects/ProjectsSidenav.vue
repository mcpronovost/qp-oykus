<script setup lang="ts">
import type { TypeProject } from "../../types/projects";
const props = defineProps({
    projects: {
        type: Array<TypeProject>,
        required: false
    }
})
</script>

<template>
    <el-menu router :default-active="`${$route.path}`">
        <el-sub-menu v-for="(project, n) in props.projects" :key="`projects-${n}`" :index="`/projects/${project.slug}`">
            <template #title><span v-text="project.name"></span></template>
            <el-menu-item :index="`/projects/${project.slug}`">
                <span v-text="$t('Overview')"></span>
            </el-menu-item>
            <el-menu-item :index="`/projects/${project.slug}/tasks`">
                <span v-text="$t('Tasks')"></span>
            </el-menu-item>
            <el-menu-item-group title="Les indispensables">
                <el-menu-item>
                    <span v-text="'Règlement'"></span>
                </el-menu-item>
                <el-menu-item>
                    <span v-text="'Contexte'"></span>
                </el-menu-item>
            </el-menu-item-group>
        </el-sub-menu>
    </el-menu>
</template>
