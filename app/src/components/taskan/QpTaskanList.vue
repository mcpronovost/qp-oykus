<script setup>
    import QpTaskanItem from "@/components/taskan/QpTaskanItem.vue";

    const props = defineProps(["title", "type", "items"])

    const title = (props.title ? props.title : (props.type ? (
        props.type == "todo" ? "À faire" :
        props.type == "inprogress" ? "En cours" :
        props.type == "completed" ? "Terminé" : ""
    ) : ""))
</script>

<template>
    <div class="qp-taskan-list">
        <header class="qp-taskan-list-header">
            <h3 v-text="`${title} (${props.items.length})`"></h3>
            <el-button size="small" text>
                <el-icon class="mdi mdi-plus" />
                <span>Ajouter une tâche</span>
            </el-button>
        </header>
        <QpTaskanItem v-for="(item, n) in props.items" :key="`qp-taskan-item-${n}`" :item="item" />
    </div>
</template>

<style scoped>
    .qp-taskan-list {
        background-color: transparent;
        padding: 0;
    }
    .qp-taskan-list-header {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
        padding: 3px 6px 16px;
    }
    .qp-taskan-list-header h3 {
        color: var(--qp-card-color);
        font-size: 14px;
        font-weight: 600;
        line-height: 120%;
        opacity: 0.5;
        padding: 0;
        margin: 0;
    }
    .qp-taskan-list-header .el-button {
        margin: 0 -10px 0 0;
    }
    .qp-taskan-list-header .el-button .el-icon {
        background-color: rgba(255, 255, 255, 0.06);
        border-radius: 100%;
        font-size: 9px;
        padding: 2px;
        margin: 0 0 1px;
    }
</style>
