<script setup>
import QpPage from "@/components/core/QpPage.vue";
import QpSidenav from "@/components/projects/QpSidenav.vue";
</script>

<template>
    <QpPage :sidenav-title="$t('Projects')">
        <div class="qp-container">
            aaa
        </div>
        <template #sidenav>
            <QpSidenav />
        </template>
    </QpPage>
</template>
