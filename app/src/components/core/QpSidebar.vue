<script setup>
import { ref } from "vue";
import { storeToRefs } from "pinia";
import { storeUser } from "@/plugins/store";
import QpCreated from "@/components/core/sidebar/QpCreated.vue";
import QpLoved from "@/components/core/sidebar/QpLoved.vue";
import QpFeatured from "@/components/core/sidebar/QpFeatured.vue";
import QpProjectCreate from "@/components/projects/QpCreate.vue";

const useStoreUser = storeUser()
const { rat } = storeToRefs(useStoreUser)

const showCreateProject = ref(false)
const openCreateProject = () => {
    showCreateProject.value = true
}
const closeCreateProject = () => {
    showCreateProject.value = false
}
</script>

<template>
    <div id="qp-sidebar">
        <el-scrollbar height="calc(100vh - 49px)">
            <nav class="qp-sidebar-nav">
                <ul v-if="rat" class="qp-sidebar-nav-list">
                    <QpCreated />
                    <QpLoved />
                </ul>
                <ul v-else class="qp-sidebar-nav-list">
                    <QpFeatured />
                </ul>
                <ul class="qp-sidebar-nav-list">
                    <li v-if="rat" class="qp-sidebar-nav-list-item">
                        <el-button circle @click="openCreateProject()">
                            <i class="mdi mdi-plus mdi-24px"></i>
                        </el-button>
                    </li>
                    <li class="qp-sidebar-nav-list-item">
                        <el-button circle disabled>
                            <i class="mdi mdi-compass-outline mdi-24px"></i>
                        </el-button>
                    </li>
                </ul>
            </nav>
        </el-scrollbar>
        <QpProjectCreate :show="showCreateProject" @close="closeCreateProject()" />
    </div>
</template>

<style scope>
#qp-sidebar {
    background-color: var(--qp-sidebar-bg);
    display: flex;
    width: 100%;
    align-items: flex-start;
    justify-content: center;
    grid-column: 3 / 4;
    grid-row: 3 / 4;
}

@media (max-width: 767px) {
    #qp-sidebar {
        display: none;
    }
}

/* ===---=== */
.qp-sidebar-nav {
    display: flex;
    width: 64px;
    height: calc(100vh - 61px);
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 6px 0;
}

.qp-sidebar-nav-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

/* ===---=== */
.qp-sidebar-nav-list-item {
    text-align: center;
    list-style: none;
    padding: 12px 0;
    margin: 0;
}

.qp-sidebar-nav-list-item>.el-icon {
    margin: 14px 0 12px;
}

.qp-sidebar-nav-list-item .el-button,
.qp-sidebar-nav-list-item .el-button:hover,
.qp-sidebar-nav-list-item .el-button:focus,
.qp-sidebar-nav-list-item .el-button:active {
    background-color: transparent !important;
    border-color: transparent !important;
}

.qp-sidebar-nav-list-item .el-button {
    width: 32px;
    height: 32px;
    opacity: 0.6;
    transition: opacity 0.3s;
}

.qp-sidebar-nav-list-item .el-button:not(.is-disabled):hover {
    opacity: 1;
}

.qp-sidebar-nav-list-item .el-avatar {
    background-color: transparent;
}

.qp-sidebar-nav-list-item .el-avatar span {
    background-color: rgba(255, 255, 255, 0.05);
    line-height: 40px;
    width: 100%;
    height: 100%;
}
</style>
