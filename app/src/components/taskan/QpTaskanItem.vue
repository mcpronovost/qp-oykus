<script setup>
    import { useI18n } from "vue-i18n";
    import { ElMessage, ElMessageBox } from "element-plus";

    const { t } = useI18n()

    const props = defineProps(["item"])

    const percent = (props.item.completed * 100) / props.item.total

    const listProgressColours = [
        { color: "#763939", percentage: 34 },
        { color: "#766739", percentage: 67 },
        { color: "var(--qp-primary-dark-2)", percentage: 100 },
        { color: "var(--qp-primary-dark-1)", percentage: 101 },
    ]

    const doDeleteItem = () => {
        ElMessageBox.confirm(
            'proxy will permanently delete the file. Continue?',
            t("DeleteATask"),
            {
                confirmButtonText: "OK",
                cancelButtonText: "Cancel",
                type: "warning"
            }
        ).then(() => {
            ElMessage({
                type: 'success',
                message: 'Delete completed',
            })
        }).catch(() => {
            ElMessage({
                type: 'info',
                message: 'Delete canceled',
            })
        })
    }

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
                        <el-dropdown-item @click="doDeleteItem()">
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
        <footer class="qp-taskan-item-footer">
            <div>aaa</div>
            <div>
                <el-icon class="mdi mdi-comment-text-outline" />
            </div>
        </footer>
    </article>
</template>

<style scoped>
    .qp-taskan-item {
        background-color: var(--qp-card-bg);
        color: var(--qp-card-color);
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
        font-size: 12px;
        line-height: 120%;
        text-align: left;
        flex: 0 1 auto;
        height: auto;
        padding: 2px 3px;
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
    .qp-taskan-item-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 5px;
    }
</style>
