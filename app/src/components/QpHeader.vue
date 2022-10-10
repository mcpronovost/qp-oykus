<script setup>
import { useSlots } from "vue";

const slots = useSlots()
const props = defineProps(["title", "content"])
</script>

<template>
    <header class="qp-header">
        <h1 v-if="props.title" class="qp-header-title">
            <span v-text="props.title"></span>
        </h1>
        <div v-if="props.content" class="qp-header-content">
            <p v-text="props.content"></p>
        </div>
        <hr class="qp-header-divider" />
    </header>
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
