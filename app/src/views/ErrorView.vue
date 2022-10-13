<script setup lang="ts">
//
</script>

<template>
    <qp-page>
        <div class="qp-container qp-centered">
            <el-row>
                <el-col style="text-align:center;">
                    <el-result icon="error" :title="$t('ContentNotFound')">
                        <template #extra>
                            <el-button @click="$router.push({name:'Home'})">
                                <span v-text="$t('BackToHome')"></span>
                            </el-button>
                        </template>
                    </el-result>
                </el-col>
            </el-row>
        </div>
    </qp-page>
</template>
