<script setup>
    import { House } from "@element-plus/icons-vue";
</script>

<template>
    <div id="qp-navbar">
        <el-scrollbar height="100%">
            <nav class="qp-navbar-nav">
                <ul class="qp-navbar-nav-list">
                    <li class="qp-navbar-nav-list-item">
                        <el-button circle>
                            <i class="mdi mdi-apps mdi-24px"></i>
                        </el-button>
                    </li>
                    <li class="qp-navbar-nav-list-item">
                        <el-button circle>
                            <i class="mdi mdi-chart-box-outline mdi-24px"></i>
                        </el-button>
                    </li>
                    <li class="qp-navbar-nav-list-item">
                        <el-button circle>
                            <i class="mdi mdi-order-bool-descending-variant mdi-24px"></i>
                        </el-button>
                    </li>
                    <li class="qp-navbar-nav-list-item">
                        <el-button circle>
                            <i class="mdi mdi-podium-gold mdi-24px"></i>
                        </el-button>
                    </li>
                </ul>
                <ul class="qp-navbar-nav-list">
                    <li class="qp-navbar-nav-list-item">
                        <el-button circle>
                            <i class="mdi mdi-tune mdi-24px"></i>
                        </el-button>
                    </li>
                </ul>
            </nav>
        </el-scrollbar>
    </div>
</template>

<style scope>
    #qp-navbar {
        background-color: #1C1D1C;
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
    .qp-navbar-nav-list-item .el-button,
    .qp-navbar-nav-list-item .el-button:hover,
    .qp-navbar-nav-list-item .el-button:focus,
    .qp-navbar-nav-list-item .el-button:active {
        background-color: transparent;
        border-color: transparent;
    }
</style>
