<script setup>
    const props = defineProps(["open"])
</script>

<template>
    <main :class="props.open ? 'qp-open' : ''">
        <div id="qp-mainview">
            <el-scrollbar height="100%">
                <slot></slot>
            </el-scrollbar>
        </div>
        <div v-if="props.open" id="qp-sideview">
            <el-scrollbar height="100%">
                <slot name="sideview"></slot>
            </el-scrollbar>
        </div>
    </main>
</template>
