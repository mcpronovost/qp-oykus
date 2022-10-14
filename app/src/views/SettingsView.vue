<script setup lang="ts">
import QpSettingsSidenav from "../components/settings/SettingsSidenav.vue";
</script>

<template>
    <qp-page :sidenav-title="$t('Settings')">
        <router-view :key="$route.fullPath" />
        <template #sidenav>
            <QpSettingsSidenav />
        </template>
    </qp-page>
</template>
