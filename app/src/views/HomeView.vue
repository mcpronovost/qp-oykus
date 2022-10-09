<script setup>
import QpPage from "@/components/core/QpPage.vue";
import logo from "@/assets/img/logo.png";
</script>

<template>
    <QpPage>
        <div class="qp-container qp-centered">
            <el-row>
                <el-col style="text-align:center;">
                    <el-avatar :src="logo" :size="200" />
                </el-col>
            </el-row>
        </div>
    </QpPage>
</template>
