<script setup>
import QpPage from "@/components/QpPage.vue";
</script>

<template>
    <QpPage>
        <div class="qp-container qp-centered">
            <el-row>
                <el-col style="text-align:center;">
                    <el-result :title="$t('Leaderboard')" :sub-title="$t('UnderDevelopment')">
                        <template #icon>
                            <el-icon class="mdi mdi-hammer-wrench" :size="120" color="var(--qp-base-color)" />
                        </template>
                    </el-result>
                </el-col>
            </el-row>
        </div>
    </QpPage>
</template>
