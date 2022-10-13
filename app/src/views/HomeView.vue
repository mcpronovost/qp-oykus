<script setup lang="ts">
import logo from "@/assets/img/logo.png";
</script>

<template>
    <qp-page>
        <div class="qp-container qp-centered">
            <el-row>
                <el-col style="text-align:center;">
                    <el-avatar :src="logo" :size="200" />
                </el-col>
            </el-row>
        </div>
    </qp-page>
</template>
