<script setup lang="ts">
//
</script>

<template>
    <el-menu router :default-active="`${$route.path}`">
        <el-menu-item :index="`/settings`">
            <el-icon class="mdi mdi-cog-outline" />
            <span v-text="$t('UserAccount')"></span>
        </el-menu-item>
        <el-menu-item index="/settings/profile">
            <el-icon class="mdi mdi-account-outline" />
            <span v-text="$t('Profile')"></span>
        </el-menu-item>
        <el-menu-item index="/settings/notifications">
            <el-icon class="mdi mdi-bell-outline" />
            <span v-text="$t('Notifications')"></span>
        </el-menu-item>
    </el-menu>
</template>
