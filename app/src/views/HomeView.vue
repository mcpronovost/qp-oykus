<script setup>
    import { storeToRefs } from "pinia";
    import { storeApp, storePlayer } from "@/plugins/store";
    import QpPage from "@/components/core/QpPage.vue";
    import QpTaskanList from "@/components/taskan/QpTaskanList.vue";

    const useStoreApp = storeApp()
    const { toggleSidenavShow, toggleSideviewShow } = useStoreApp

    const useStorePlayer = storePlayer()
    const { playername } = storeToRefs(useStorePlayer)

    const listTaskansTodo = [
        {
            title: "Corriger le règlement",
            completed: 0,
            total: 1
        },
        {
            title: "Rédiger le bestiaire",
            completed: 0,
            total: 1
        },
        {
            title: "Rédiger l'herbier",
            completed: 0,
            total: 1
        }
    ]

    const listTaskansInProgress = [
        {
            title: "Rédiger le règlement",
            completed: 1,
            total: 4
        },
        {
            title: "Corriger le contexte",
            completed: 3,
            total: 6
        }
    ]

    const listTaskansCompleted = [
        {
            title: "Rédiger le contexte",
            completed: 4,
            total: 4
        }
    ]
</script>

<template>
    <QpPage>
        <div class="qp-container">
            <el-row>
                <el-col>
                    <el-card>
                        Hello {{ playername }}
                        <el-button @click="toggleSidenavShow()">toggle sidenav</el-button>
                        <el-button @click="toggleSideviewShow()">toggle sideview</el-button>
                    </el-card>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="24" :md="12" :xl="8">
                    <QpTaskanList :type="'todo'" :items="listTaskansTodo" />
                </el-col>
                <el-col :span="24" :md="12" :xl="8">
                    <QpTaskanList :type="'inprogress'" :items="listTaskansInProgress" />
                </el-col>
                <el-col :span="24" :xl="8">
                    <QpTaskanList :type="'completed'" :items="listTaskansCompleted" />
                </el-col>
            </el-row>
        </div>
        <template #sidenav-title>
            Projets
        </template>
        <template #sidenav>
            sidenav
        </template>
        <template #sideview-title>
            sideview
        </template>
        <template #sideview>
            sideview
        </template>
    </QpPage>
</template>
