<script setup lang="ts">
import { storeToRefs } from "pinia";
import { storeUser } from "../../plugins/store";
import logo from "@/assets/img/logo.png";

const useStoreUser = storeUser()
const { rat } = storeToRefs(useStoreUser)

const version = (APP_VERSION || "0.1.0")
</script>

<template>
    <div id="qp-navbar">
        <el-scrollbar height="100%">
            <nav class="qp-navbar-nav">
                <ul class="qp-navbar-nav-list">
                    <li class="qp-navbar-nav-list-item qp-logo">
                        <el-button circle @click="$router.push({name:'Home'})">
                            <el-avatar :src="logo">
                                <span>Oykus</span>
                            </el-avatar>
                        </el-button>
                    </li>
                </ul>
                <!---->
                <ul v-if="rat" class="qp-navbar-nav-list">
                    <li class="qp-navbar-nav-list-item">
                        <el-button circle :disabled="$route.name=='Projects'" @click="$router.push({name:'Projects'})">
                            <i class="mdi mdi-apps mdi-24px"></i>
                        </el-button>
                    </li>
                    <li class="qp-navbar-nav-list-item">
                        <el-button circle disabled>
                            <i class="mdi mdi-chart-box-outline mdi-24px"></i>
                        </el-button>
                    </li>
                    <li class="qp-navbar-nav-list-item">
                        <el-button circle :disabled="$route.name=='Tasks'" @click="$router.push({name:'Tasks'})">
                            <i class="mdi mdi-order-bool-descending-variant mdi-24px"></i>
                        </el-button>
                    </li>
                    <li class="qp-navbar-nav-list-item">
                        <el-button circle :disabled="$route.name=='Leaderboard'" @click="$router.push({name:'Leaderboard'})">
                            <i class="mdi mdi-podium-gold mdi-24px"></i>
                        </el-button>
                    </li>
                </ul>
                <!---->
                <ul class="qp-navbar-nav-list">
                    <li v-if="rat" class="qp-navbar-nav-list-item">
                        <el-button circle :disabled="$route.name=='Settings'" @click="$router.push({name:'Settings'})">
                            <i class="mdi mdi-tune mdi-24px"></i>
                        </el-button>
                    </li>
                    <li class="qp-navbar-nav-list-item qp-version">
                        <span v-text="version"></span>
                    </li>
                </ul>
            </nav>
        </el-scrollbar>
    </div>
</template>

<style scope>
    #qp-navbar {
        background-color: var(--qp-navbar-bg);
        display: flex;
        align-items: flex-start;
        justify-content: center;
        grid-column: 1 / 2;
        grid-row: 2 / 4;
    }
    /* ===---=== */
    .qp-navbar-nav {
        display: flex;
        width: 64px;
        height: calc(100vh - 13px);
        flex-direction: column;
        align-items: center;
        justify-content: space-between;
        padding: 6px 0;
    }
    .qp-navbar-nav-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    /* ===---=== */
    .qp-navbar-nav-list-item {
        text-align: center;
        list-style: none;
        padding: 12px 0;
        margin: 0;
    }
    .qp-navbar-nav-list-item.qp-logo {
        padding: 3px 0 12px;
    }
    .qp-navbar-nav-list-item .el-button,
    .qp-navbar-nav-list-item .el-button:hover,
    .qp-navbar-nav-list-item .el-button:focus,
    .qp-navbar-nav-list-item .el-button:active,
    .qp-navbar-nav-list-item .el-button.is-disabled,
    .qp-navbar-nav-list-item .el-button.is-disabled:hover,
    .qp-navbar-nav-list-item .el-button.is-disabled:focus,
    .qp-navbar-nav-list-item .el-button.is-disabled:active {
        background-color: transparent!important;
        border-color: transparent!important;
        width: 32px;
        height: 32px;
    }
    /* ===---=== */
    .qp-navbar-nav-list-item.qp-logo .el-avatar {
        --el-avatar-size: 32px;
        background-color: #2a2b2a;
    }
    .qp-navbar-nav-list-item.qp-version {
        font-size: 9px;
        line-height: 120%;
        color: #6a6b6a;
    }
</style>
