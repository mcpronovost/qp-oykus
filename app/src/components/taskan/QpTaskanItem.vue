<script setup>

    const props = defineProps(["item"])

    const percent = (props.item.completed * 100) / props.item.total

    const listProgressColours = [
        { color: '#a52f2f', percentage: 34 },
        { color: '#bb902f', percentage: 67 },
        { color: '#139595', percentage: 100 },
        { color: '#139518', percentage: 101 },
    ]

</script>

<template>
    <article class="qp-taskan-item">
        <header class="qp-taskan-item-header">
            <h4 v-text="props.item.title"></h4>
            <p v-text="props.item.caption"></p>
            <el-dropdown trigger="click" placement="bottom-end">
                <el-button circle>
                    <el-icon class="mdi mdi-playlist-edit" />
                </el-button>
                <template #dropdown>
                    <el-dropdown-menu>
                        <el-dropdown-item>
                            <span>Modifier</span>
                        </el-dropdown-item>
                        <el-dropdown-item>
                            <span>Supprimer</span>
                        </el-dropdown-item>
                    </el-dropdown-menu>
                </template>
            </el-dropdown>
        </header>
        <div class="qp-taskan-content">
            <el-button text>
                <el-icon class="mdi mdi-format-list-bulleted-square el-icon--left" />
                <span>Progression</span>
            </el-button>
            <span v-text="`${props.item.completed} / ${props.item.total}`"></span>
            <el-progress :percentage="percent" :color="listProgressColours" :show-text="false" />
        </div>
    </article>
</template>

<style scoped>
    .qp-taskan-item {
        background-color: var(--qp-card-light-bg);
        padding: 12px;
    }
    .qp-taskan-item + .qp-taskan-item {
        margin-top: 12px;
    }
    .qp-taskan-item-header {
        position: relative;
        padding: 0 5px;
    }
    .qp-taskan-item h4 {
        font-size: 14px;
        font-weight: 600;
        line-height: 120%;
        padding: 6px 0;
        margin: 0;
    }
    .qp-taskan-item p {
        font-size: 14px;
        font-weight: 400;
        line-height: 120%;
        padding: 0;
        margin: 0;
    }
    .qp-taskan-item-header .el-dropdown {
        position: absolute;
        top: 0;
        right: 0;
    }
    .qp-taskan-item-header .el-button {
        font-size: 20px;
        line-height: 100%;
        height: auto;
        position: absolute;
        top: 0;
        right: 0;
        opacity: 0.8;
        padding: 2px;
    }
    .qp-taskan-content {
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        padding: 12px 0;
    }
    .qp-taskan-content > .el-button {
        font-size: 14px;
        line-height: 120%;
        text-align: left;
        flex: 0 1 auto;
        padding: 5px;
    }
    .qp-taskan-content > span {
        font-size: 12px;
        font-weight: 600;
        line-height: 120%;
        text-align: right;
        flex: 1 1 50%;
        padding: 0 5px;
    }
    .qp-taskan-content > .el-progress {
        flex: 1 1 100%;
        margin: 4px 0 0;
    }
</style>
