<script setup lang="ts">
//
</script>

<template>
    <div class="qp-container qp-centered">
        <el-row>
            <el-col style="text-align:center;">
                <el-result :title="$t('Error')" :sub-title="$t('ContentNotFound')">
                    <template #icon>
                        <el-icon class="mdi mdi-emoticon-sad-outline" :size="120" />
                    </template>
                </el-result>
            </el-col>
        </el-row>
    </div>
</template>
