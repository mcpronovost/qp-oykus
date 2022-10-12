<script setup>
import router from "@/plugins/router";

const goTo = (obj) => {
    router.push(obj)
}
</script>

<template>
    <qp-page>
        <div class="qp-container qp-centered">
            <el-row>
                <el-col style="text-align:center;">
                    <el-result icon="error" :title="$t('ContentNotFound')">
                        <template #extra>
                            <el-button @click="goTo({name:'Home'})">
                                <span v-text="$t('BackToHome')"></span>
                            </el-button>
                        </template>
                    </el-result>
                </el-col>
            </el-row>
        </div>
    </qp-page>
</template>
