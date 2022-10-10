<script setup>
import { storeToRefs } from "pinia";
import { storeUser } from "@/plugins/store";

const useStoreUser = storeUser()
const { created_projects, owned_projects } = storeToRefs(useStoreUser)

const listProjects = [...new Map([
    ...created_projects.value,
    ...owned_projects.value
].map(item => [item["id"], item])).values()]

const goTo = (obj) => {
    router.push(obj)
}
</script>

<template>
    <el-menu default-active="1">
        <el-sub-menu index="1">
            <template #title>
                <span v-text="$t('Projects')"></span>
            </template>
            <el-menu-item v-for="(project, n) in listProjects" :key="`project-${n}`" :index="project.slug">
                <span v-text="project.name"></span>
            </el-menu-item>
        </el-sub-menu>
        <el-sub-menu index="2" disabled>
            <template #title>
                <span v-text="$t('Tasks')"></span>
            </template>
            <el-menu-item index="2-1">
                <span>urhwegfgre regw</span>
            </el-menu-item>
        </el-sub-menu>
    </el-menu>
</template>
