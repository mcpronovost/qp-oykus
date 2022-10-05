<script setup>
    import { reactive } from "vue";
    import { storeToRefs } from "pinia";
    import { storeApp, storePlayer } from "@/plugins/store";
    import QpPage from "@/components/core/QpPage.vue";

    const useStoreApp = storeApp()
    const { theme } = storeToRefs(useStoreApp)
    const { toggleTheme } = useStoreApp

    const useStorePlayer = storePlayer()
    const { playername } = storeToRefs(useStorePlayer)

    const sideview = reactive({
        open: true
    })

    const toggleAppTheme = () => {
        toggleTheme()
    }
</script>

<template>
    <QpPage :open="sideview.open">
        <el-row :gutter="20">
            <el-col>
                <el-card>
                    aaa {{ theme }}
                </el-card>
            </el-col>
        </el-row>
        <el-row :gutter="20">
            <el-col :span="10">
                <el-card>
                    <el-button @click="toggleAppTheme()">click me {{ playername }}</el-button>
                </el-card>
            </el-col>
            <el-col :span="14">
                <el-card>
                    {{ useStorePlayer.$state }}
                </el-card>
            </el-col>
        </el-row>
        <template #sideview>
            bbvx
        </template>
    </QpPage>
</template>
