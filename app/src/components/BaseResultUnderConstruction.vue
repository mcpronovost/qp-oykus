<script setup lang="ts">
const props = defineProps({
    title: {
        type: String,
        required: false
    },
    row: {
        type: Boolean,
        required: false
    }
})
</script>

<template>
    <div :class="props.row ? '' : 'qp-container qp-centered'">
        <el-row>
            <el-col style="text-align:center;">
                <el-result :title="props.title || $t('ContentUnderDevelopment')" :sub-title="$t('ComeBackLater')">
                    <template #icon>
                        <el-icon class="mdi mdi-hammer-wrench" :size="120" color="var(--qp-base-color)" />
                    </template>
                </el-result>
            </el-col>
        </el-row>
    </div>
</template>
