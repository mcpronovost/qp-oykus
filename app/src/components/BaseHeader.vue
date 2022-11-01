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
    heading: {
        type: Number,
        required: false,
        default: 1
    },
    titleSize: {
        type: String,
        required: false
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
                <h1 v-if="heading == 1 && props.title" class="qp-header-title" :style="titleSize?`font-size:${titleSize};`:''">
                    <span v-text="props.title"></span>
                </h1>
                <h2 v-else-if="heading == 2 && props.title" class="qp-header-title" :style="titleSize?`font-size:${titleSize};`:''">
                    <span v-text="props.title"></span>
                </h2>
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
    padding: 20px 0 0;
    margin: 0;
}
h1.qp-header-title {
    font-size: 72px;
    line-height: 120%;
}
h2.qp-header-title {
    font-size: 52px;
    line-height: 120%;
}
.qp-header-title {
    font-family: "Quicksand", sans-serif;
    font-weight: 300;
    padding: 0;
    margin: 0 0 24px;
}
.qp-header-content p {
    font-size: 14px;
    line-height: 150%;
    max-width: 800px;
    opacity: 0.8;
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
    margin: 20px 2px;
}
</style>
