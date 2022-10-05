<script setup>
    import QpNavbar from "@/components/core/QpNavbar.vue";
    import QpSidebar from "@/components/core/QpSidebar.vue";
</script>

<template>
    <div id="qp-app">
        <div id="qp-appbar"></div>
        <QpNavbar />
        <div id="qp-topbar">
            topbar
        </div>
        <div id="qp-main">
            <router-view :key="$route.fullPath" />
        </div>
        <QpSidebar />
    </div>
</template>

<style scoped>
    #qp-app {
        display: grid;
        grid-template-columns: 64px auto 64px;
        grid-template-rows: 1px 48px auto;
        width: 100vw;
        min-width: 400px;
        height: 100vh;
    }
    @media (max-width: 1199px) {
        #qp-app {
            grid-template-columns: 64px auto 64px;
        }
    }
    #qp-appbar {
        background-color: #89A411;
        grid-column: 1 / 4;
        grid-row: 1 / 2;
        height: 4px;
    }
    #qp-topbar {
        background-color: #222322;
        display: flex;
        align-items: center;
        justify-content: center;
        grid-column: 2 / 4;
        grid-row: 2 / 3;
    }
</style>
