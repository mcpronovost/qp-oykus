<script setup>
import { computed } from "vue";
import { storeToRefs } from "pinia";
import { storeUser } from "@/plugins/store";

const useStoreUser = storeUser()
const { owned_projects } = storeToRefs(useStoreUser)

const listProjects = computed(() => [...new Map([
    ...owned_projects.value
].map(item => [item["id"], item])).values()])

const goTo = (obj) => {
    router.push(obj)
}
</script>

<template>
    <qp-page :sidenav-title="$t('Projects')">
        <div class="qp-container">
            <el-row>
                <el-col>
                    <qp-header :title="$t('Projects')" :content="$t('Allyourprojects')" />
                </el-col>
            </el-row>
            <el-row>
                <el-col v-for="(project, n) in listProjects" :key="`project-${n}`" :span="24" :sm="12" :md="8" :lg="6">
                    <el-card class="qp-projects-list-item">
                        <div class="qp-projects-list-item-wrapper">
                            <div class="qp-projects-list-item-header">
                                <el-avatar :src="project.icon" :size="64" shape="square" :style="`background-color:${project.icon ? 'transparent' : project.primary_color};color:#fff;`">
                                    <span v-text="project.initial"></span>
                                </el-avatar>
                                <h3 class="qp-projects-list-item-name">
                                    <span v-text="project.name"></span>
                                </h3>
                            </div>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </div>
    </qp-page>
</template>

<style>
.qp-projects-list-item,
.qp-projects-list-item > .el-card__body {
    text-align: center;
    height: 100%;
    padding: 0;
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
.qp-projects-list-item-header .el-avatar {
    font-size: 0;
    line-height: 0;
    display: flex;
    margin: 0 auto 0 0;
}
.qp-projects-list-item-header .el-avatar span {
    font-size: 24px;
    line-height: 120%;
}
.qp-projects-list-item-name {
    font-size: 18px;
    font-weight: 600;
    line-height: 150%;
    padding: 0;
    margin: 24px 0 0;
}
</style>
