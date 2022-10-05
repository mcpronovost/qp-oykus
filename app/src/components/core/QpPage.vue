<script setup>
    import { useSlots } from "vue";

    const slots = useSlots()
    const props = defineProps(["sidenav-open", "sideview-open"])

    console.log("sidenav" in slots)
</script>

<template>
    <main :class="props.sideviewOpen ? 'qp-open' : ''">
        <div v-if="props.sidenavOpen" id="qp-sidenav">
            <el-scrollbar height="100%">
                <slot name="sidenav"></slot>
            </el-scrollbar>
        </div>
        <div id="qp-mainview">
            <el-scrollbar height="100%">
                <slot></slot>
            </el-scrollbar>
        </div>
        <div v-if="props.sideviewOpen" id="qp-sideview">
            <el-scrollbar height="100%">
                <slot name="sideview"></slot>
            </el-scrollbar>
        </div>
    </main>
</template>
