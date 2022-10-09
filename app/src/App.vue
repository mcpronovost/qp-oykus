<script setup>
    import { onMounted } from "vue";
    import QpAppbar from "@/components/core/QpAppbar.vue";
    import QpNavbar from "@/components/core/QpNavbar.vue";
    import QpTopbar from "@/components/core/QpTopbar.vue";
    import QpSidebar from "@/components/core/QpSidebar.vue";

    const setVH = () => {
        let vh = window.innerHeight * 0.01;
        document.documentElement.style.setProperty("--vh", `${vh}px`);
    }

    onMounted(() => {
        setVH()
        addEventListener("resize", () => {
            setVH()
        })
    })
</script>

<template>
    <div id="qp-app" :class="$route.name && $route.name.startsWith('Auth') ? 'qp-app-auth' : ''">
        <QpAppbar />
        <QpNavbar v-if="!$route.name || !$route.name.startsWith('Auth')" />
        <QpTopbar v-if="!$route.name || !$route.name.startsWith('Auth')" />
        <div id="qp-main">
            <router-view :key="$route.fullPath" />
        </div>
        <QpSidebar v-if="!$route.name || !$route.name.startsWith('Auth')" />
    </div>
</template>

<style scoped>
    #qp-app {
        display: grid;
        grid-template-columns: 64px auto 64px;
        grid-template-rows: 1px 48px auto;
        width: 100vw;
        min-width: 300px;
        height: 100vh;
    }
    #qp-app.qp-app-auth {
        grid-template-columns: 0 auto 0;
        grid-template-rows: 1px auto;
    }
    @media (max-width: 767px) {
        #qp-app {
            grid-template-columns: 64px auto;
        }
        #qp-app.qp-app-auth {
            grid-template-columns: 0 auto 0;
        }
    }
</style>
