<script setup>
import { computed } from "vue";
import { storeToRefs } from "pinia";
import { storeApp, storeUser } from "@/plugins/store";
import QpTaskanList from "@/components/taskan/QpTaskanList.vue";

const useStoreApp = storeApp()
const { mainviewWidth } = storeToRefs(useStoreApp)
const { toggleSidenavShow, toggleSideviewShow } = useStoreApp

const useStoreUser = storeUser()
const { username } = storeToRefs(useStoreUser)

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
    },
    {
        title: "Finir le design",
        completed: 0,
        total: 12
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
    },
    {
        title: "Trouver des évènements",
        completed: 5,
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

const taskanSpan = computed(() => {
    return mainviewWidth.value > 1100 ? 8 : mainviewWidth.value > 676 ? 12 : 24
})

</script>

<template>
    <qp-page>
        <div class="qp-container">
            <el-row>
                <el-col>
                    <el-card>
                        Hello {{ username }} - {{ mainviewWidth }}
                        <el-button @click="toggleSidenavShow()">toggle sidenav</el-button>
                        <el-button @click="toggleSideviewShow()">toggle sideview</el-button>
                    </el-card>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="taskanSpan">
                    <QpTaskanList :type="'todo'" :items="listTaskansTodo" />
                </el-col>
                <el-col :span="taskanSpan">
                    <QpTaskanList :type="'inprogress'" :items="listTaskansInProgress" />
                </el-col>
                <el-col :span="taskanSpan">
                    <QpTaskanList :type="'completed'" :items="listTaskansCompleted" />
                </el-col>
            </el-row>
        </div>
    </qp-page>
</template>
