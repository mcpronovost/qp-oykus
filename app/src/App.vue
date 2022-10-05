<script setup>
</script>

<template>
    <div id="qp-app">
        <div id="qp-appbar"></div>
        <div id="qp-navbar">
            navbar
        </div>
        <div id="qp-topbar">
            topbar
        </div>
        <div id="qp-main">
            <router-view :key="$route.fullPath" />
        </div>
        <div id="qp-sidebar">
            main
        </div>
    </div>
</template>

<style scoped>
    #qp-app {
        display: grid;
        grid-template-columns: 250px auto 64px;
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
    #qp-navbar {
        background-color: #1C1D1C;
        display: flex;
        align-items: flex-start;
        justify-content: center;
        grid-column: 1 / 2;
        grid-row: 2 / 4;
    }
    #qp-topbar {
        background-color: #222322;
        display: flex;
        align-items: center;
        justify-content: center;
        grid-column: 2 / 4;
        grid-row: 2 / 3;
    }
    #qp-sidebar {
        background-color: #2A2B2A;
        display: flex;
        align-items: flex-start;
        justify-content: center;
        grid-column: 3 / 4;
        grid-row: 3 / 4;
    }
</style>
