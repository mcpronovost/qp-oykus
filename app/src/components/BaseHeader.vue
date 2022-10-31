<script setup lang="ts">
const props = defineProps({
    title: {
        type: String,
        required: false
    },
    content: {
        type: String,
        required: false
    },
    titleSize: {
        type: String,
        required: false,
        default: "72px"
    },
    hideDivider: {
        type: Boolean,
        required: false
    }
})
</script>

<template>
    <el-row>
        <el-col>
            <header class="qp-header">
                <h1 v-if="props.title" class="qp-header-title" :style="`font-size:${titleSize};`">
                    <span v-text="props.title"></span>
                </h1>
                <div v-if="props.content" class="qp-header-content">
                    <p v-text="props.content"></p>
                </div>
                <hr v-if="!hideDivider" class="qp-header-divider" />
            </header>
        </el-col>
    </el-row>
</template>

<style scoped>
.qp-header {
    padding: 32px 0 0;
    margin: 0;
}
.qp-header-title {
    font-family: "Quicksand", sans-serif;
    font-size: 72px;
    font-weight: 300;
    line-height: 120%;
    padding: 0;
    margin: 0 0 24px;
}
.qp-header-content p {
    padding: 0;
    margin: 0 2px 24px;
}
.qp-header-divider {
    background-color: var(--qp-primary);
    border: none;
    display: block;
    width: 72px;
    height: 2px;
    padding: 0;
    margin: 32px 2px;
}
</style>
