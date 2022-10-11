<script setup>
import { storeApp } from "@/plugins/store";
import { storeToRefs } from "pinia";

const useStoreApp = storeApp()
const { isLoading } = storeToRefs(useStoreApp)
</script>

<template>
    <div id="qp-appbar">
        <el-progress :percentage="100" :indeterminate="isLoading" :stroke-width="2" :show-text="false" />
    </div>
</template>

<style>
    #qp-appbar {
        background-color: transparent;
        grid-column: 1 / 4;
        grid-row: 1 / 2;
    }
    #qp-appbar .el-progress-bar__outer,
    #qp-appbar .el-progress-bar__inner {
        border-radius: 0;
    }
</style>
