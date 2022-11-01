<script setup lang="ts">
const props = defineProps({
    rpg: {
        type: Object || null,
        required: true
    }
})
</script>

<template>
    <el-menu v-if="props.rpg" router :default-active="`${$route.path}`" class="rpg-sidenav-menu">
        <el-menu-item :index="`/rpg/${props.rpg.slug}/rules`" class="rpg-sidenav-menu-item">
            <el-icon class="mdi mdi-scale-balance" />
            <span v-text="$t('TheRules')"></span>
        </el-menu-item>
        <el-menu-item :index="`/rpg/${props.rpg.slug}/informations`" class="rpg-sidenav-menu-item">
            <el-icon class="mdi mdi-script-text" />
            <span v-text="$t('Informations')"></span>
        </el-menu-item>
        <el-menu-item :index="`/rpg/${props.rpg.slug}`" class="rpg-sidenav-menu-item">
            <el-icon class="mdi mdi-forum-outline" />
            <span v-text="$t('Forum')"></span>
        </el-menu-item>
        <el-menu-item :index="`/rpg/${props.rpg.slug}/community`" class="rpg-sidenav-menu-item">
            <el-icon class="mdi mdi-account-group" />
            <span v-text="$t('Community')"></span>
        </el-menu-item>
    </el-menu>
</template>
