<script setup>
    import { User } from "@element-plus/icons-vue";
</script>

<template>
    <div id="qp-sidebar">
        <el-scrollbar height="calc(100vh - 49px)">
            <nav class="qp-sidebar-nav">
                <ul class="qp-sidebar-nav-list">
                    <li class="qp-sidebar-nav-list-item">
                        <el-tooltip placement="left" content="Qalatlán">
                            <el-button size="large" circle>
                                <el-avatar :src="''">
                                    <span>Q</span>
                                </el-avatar>
                            </el-button>
                        </el-tooltip>
                    </li>
                    <li class="qp-sidebar-nav-list-item">
                        <el-tooltip placement="left" content="Hobeon">
                            <el-button size="large" circle>
                                <el-avatar :src="''">
                                    <span>H</span>
                                </el-avatar>
                            </el-button>
                        </el-tooltip>
                    </li>
                    <li class="qp-sidebar-nav-list-item">
                        <el-icon size="large">
                            <i class="mdi mdi-heart-outline"></i>
                        </el-icon>
                    </li>
                    <li class="qp-sidebar-nav-list-item">
                        <el-tooltip placement="left" content="Le monde perdu de Rhansidor">
                            <el-button size="large" circle>
                                <el-avatar :src="''">
                                    <span>R</span>
                                </el-avatar>
                            </el-button>
                        </el-tooltip>
                    </li>
                </ul>
                <ul class="qp-sidebar-nav-list">
                    <li class="qp-sidebar-nav-list-item">
                        <el-button circle>
                            <i class="mdi mdi-plus mdi-24px"></i>
                        </el-button>
                    </li>
                    <li class="qp-sidebar-nav-list-item">
                        <el-button circle>
                            <i class="mdi mdi-compass-outline mdi-24px"></i>
                        </el-button>
                    </li>
                </ul>
            </nav>
        </el-scrollbar>
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
        padding: 6px 0;
        margin: 0;
    }
    .qp-sidebar-nav-list-item > .el-icon {
        margin: 14px 0 12px;
    }
    .qp-sidebar-nav-list-item .el-button,
    .qp-sidebar-nav-list-item .el-button:hover,
    .qp-sidebar-nav-list-item .el-button:focus,
    .qp-sidebar-nav-list-item .el-button:active {
        background-color: transparent;
        border-color: transparent;
    }
    .qp-sidebar-nav-list-item .el-button {
        opacity: 0.6;
        transition: opacity 0.3s;
    }
    .qp-sidebar-nav-list-item .el-button:hover {
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
