<script setup>
import QpPage from "@/components/QpPage.vue";
</script>

<template>
    <QpPage>
        <div class="qp-container qp-centered">
            <el-row>
                <el-col style="text-align:center;">
                    <el-result icon="error" :title="$t('ContentNotFound')">
                    </el-result>
                </el-col>
            </el-row>
        </div>
    </QpPage>
</template>
