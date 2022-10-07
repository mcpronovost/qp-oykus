<script setup>
    import router from "../../plugins/router";
    import { Bell, Message } from "@element-plus/icons-vue";

    const goTo = (obj) => {
        router.push(obj)
    }
</script>

<template>
    <div id="qp-topbar">
        <div id="qp-topbar-left">
            <!---->
        </div>
        <div id="qp-topbar-center">
            <!---->
        </div>
        <div id="qp-topbar-right">
            <div class="qp-topbar-item">
                <el-badge :value="0" :hidden="true">
                    <el-button :icon="Message"></el-button>
                </el-badge>
            </div>
            <div class="qp-topbar-item">
                <el-badge :value="0" :hidden="true">
                    <el-button :icon="Bell"></el-button>
                </el-badge>
            </div>
            <div class="qp-topbar-item qp-player">
                <el-dropdown trigger="click" placement="bottom-end" popper-class="qp-topbar-popper" @command="goTo">
                    <el-avatar>
                        <span>Q</span>
                    </el-avatar>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item class="qp-dropdown-text" disabled>
                                <div>
                                    <div>Connecté en tant que</div>
                                    <div>Qamuy Sinen</div>
                                </div>
                            </el-dropdown-item>
                            <el-divider />
                            <el-dropdown-item :command="{name:'MeProfil'}" :disabled="$route.name=='MeProfil'||true">
                                <span>Mon profil</span>
                            </el-dropdown-item>
                            <el-dropdown-item :command="{name:'MeProjects'}" :disabled="$route.name=='MeProjects'">
                                <span>Mes projets</span>
                            </el-dropdown-item>
                            <el-dropdown-item :command="{name:'MeTasks'}" :disabled="$route.name=='MeTasks'">
                                <span>Mes tâches</span>
                            </el-dropdown-item>
                            <el-divider />
                            <el-dropdown-item :command="{name:'Settings'}" :disabled="$route.name=='Settings'">
                                <span>Paramètres</span>
                            </el-dropdown-item>
                            <el-divider />
                            <el-dropdown-item :command="{name:'AuthLogout'}" :disabled="$route.name=='AuthLogout'||true">
                                <span>Déconnexion</span>
                            </el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
            </div>
        </div>
    </div>
</template>

<style scoped>
    #qp-topbar {
        background-color: var(--qp-topbar-bg);
        font-size: 0;
        line-height: 0;
        display: flex;
        align-items: center;
        justify-content: space-between;
        grid-column: 2 / 4;
        grid-row: 2 / 3;
    }
    /* ===--- RIGHT ---=== */
    #qp-topbar-right {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding: 0;
    }
    .qp-topbar-item {
        padding: 0 16px;
    }
    .qp-topbar-item .el-avatar {
        --el-avatar-size: 32px;
        background-color: var(--qp-primary);
        opacity: 0.8;
        transition: opacity 0.3s;
    }
    .qp-topbar-item .el-avatar:hover {
        opacity: 1;
    }
    .qp-topbar-item .el-badge {
        --el-bg-color: var(--qp-topbar-bg);
        --el-badge-font-size: 9px;
        --el-badge-size: 14px;
        --el-badge-padding: 4px;
    }
    .qp-topbar-item .el-button {
        background-color: transparent;
        border-color: transparent;
        font-size: 20px;
        height: auto;
        padding: 2px 4px;
    }
    .qp-topbar-item .el-dropdown .el-tooltip__trigger {
        cursor: pointer;
    }
</style>
