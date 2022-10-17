<script setup lang="ts">
import type { TypeProject } from "../../types/projects";
import { storeToRefs } from "pinia";
import { storeUser } from "../../plugins/store";

const useStoreUser = storeUser()
const { id } = storeToRefs(useStoreUser)

const props = defineProps({
    projects: {
        type: Array<TypeProject>,
        required: false
    }
})
</script>

<template>
    <div class="qp-container">
        <qp-header :title="$t('Projects')" :content="$t('Allyourprojects')" />
        <el-row>
            <el-col v-for="(project, n) in props.projects" :key="`project-${n}`" :span="24" :sm="12" :md="8" :lg="6">
                <el-card class="qp-projects-list-item" @click="$router.push({name: 'ProjectsDetail', params: {slug: project.slug}})">
                    <div class="qp-projects-list-item-wrapper">
                        <div class="qp-projects-list-item-header">
                            <div class="qp-projects-list-item-icon">
                                <el-avatar :src="project.icon" :size="64" shape="square" :style="`background-color:${project.icon ? 'transparent' : project.primary_color};color:#fff;`">
                                    <span v-text="project.initial"></span>
                                </el-avatar>
                                <el-avatar v-if="project.owner?.id !== id" :src="project.owner?.avatar" :size="32" class="qp-projects-list-item-owner">
                                    <span v-if="project.owner" v-text="project.owner?.initial"></span>
                                    <span v-else>
                                        <el-icon class="mdi mdi-account-outline" />
                                    </span>
                                </el-avatar>
                            </div>
                            <h3 class="qp-projects-list-item-name">
                                <span v-text="project.name"></span>
                            </h3>
                        </div>
                    </div>
                </el-card>
            </el-col>
        </el-row>
    </div>
</template>

<style>
.qp-projects-list-item,
.qp-projects-list-item > .el-card__body {
    text-align: center;
    height: 100%;
    padding: 0;
}
.qp-projects-list-item:hover {
    box-shadow: 0 4px 4px rgba(0, 0, 0, 0.04)!important;
    cursor: pointer;
    transform: translateY(-4px);
}
.qp-projects-list-item-wrapper {
    display: flex;
    width: 100%;
    height: 100%;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
}
.qp-projects-list-item-header {
    box-sizing: border-box;
    text-align: left;
    display: block;
    width: 100%;
    padding: 32px;
}
.qp-projects-list-item-icon {
    font-size: 0;
    line-height: 0;
    display: flex;
    position: relative;
    margin: 0 auto 0 0;
}
.qp-projects-list-item-icon span {
    font-size: 24px;
    line-height: 120%;
}
.qp-projects-list-item-owner {
    border: 4px solid var(--qp-card-bg);
    box-shadow: 0 0 0 2px var(--qp-card-bg) inset;
    position: absolute;
    top: 40px;
    left: 40px;
}
.qp-projects-list-item-owner span {
    background-color: var(--qp-card-bg-light-1);
    font-size: 12px;
    line-height: 24px;
    width: 100%;
    height: 100%;
}
.qp-projects-list-item-name {
    font-size: 18px;
    font-weight: 600;
    line-height: 150%;
    padding: 0;
    margin: 24px 0 0;
}
</style>
