<script setup lang="ts">
import { onMounted, ref } from "vue";
import { storeToRefs } from "pinia";
import { API, HEADERS } from "../plugins/store/index";
import QpQuestsCharacter from "../components/quests/QuestsCharacter.vue";
import QpQuestsHistory from "../components/quests/QuestsHistory.vue";
import { useI18n } from "vue-i18n";
import { storeUser } from "../plugins/store";

const { t } = useI18n()

const useStoreUser = storeUser()
const { rat, lang } = storeToRefs(useStoreUser)

const isLoading = ref<boolean>(false)
const hasError = ref<string|null>(null)

const quest = ref<any>(null)
const character = ref<any>(null)
const questlogs = ref<Array<any>>([])

const doQuestDetail = async (pk: Number) => {
    isLoading.value = true
    hasError.value = null
    quest.value = null
    // ===---
    try {
        let f = await fetch(`${API}/quests/${pk}/`, {
            method: "GET",
            headers: HEADERS(rat.value, lang.value)
        })
        if (f.status === 200) {
            let r = await f.json()
            quest.value = r
            doCharacterDetail(1)
        } else {
            if (f.status === 401) throw t("not authorized")
            else if (f.status === 404) throw t("not found")
            else throw t("AnErrorOccurred")
        }
    } catch (e) {
        if (typeof(e) === "string") hasError.value = `${e}`
        else hasError.value = t("AnErrorOccurred")
        isLoading.value = false
    }
}

const doCharacterDetail = async (pk: Number) => {
    isLoading.value = true
    hasError.value = null
    // ===---
    try {
        let f = await fetch(`${API}/characters/${pk}/`, {
            method: "GET",
            headers: HEADERS(rat.value, lang.value)
        })
        if (f.status === 200) {
            let r = await f.json()
            character.value = r
            doQuestLogsList(1)
        } else {
            if (f.status === 401) throw t("not authorized")
            else if (f.status === 404) throw t("not found")
            else throw t("AnErrorOccurred")
        }
    } catch (e) {
        if (typeof(e) === "string") hasError.value = `${e}`
        else hasError.value = t("AnErrorOccurred")
        isLoading.value = false
    }
}

const doQuestLogsList = async (pk: Number) => {
    isLoading.value = true
    hasError.value = null
    questlogs.value = []
    // ===---
    try {
        let f = await fetch(`${API}/quests/${pk}/logs/`, {
            method: "GET",
            headers: HEADERS(rat.value, lang.value)
        })
        if (f.status === 200) {
            let r = await f.json()
            questlogs.value = r.results
            isLoading.value = false
        } else {
            if (f.status === 401) throw t("not authorized")
            else if (f.status === 404) throw t("not found")
            else throw t("AnErrorOccurred")
        }
    } catch (e) {
        if (typeof(e) === "string") hasError.value = `${e}`
        else hasError.value = t("AnErrorOccurred")
        isLoading.value = false
    }
}

onMounted(() => {
    doQuestDetail(1)
})

</script>

<template>
    <qp-page :sidenav-title="$t('Character')" :sideview-title="$t('History')">
        <template #sidenav v-if="!isLoading && !hasError">
            <QpQuestsCharacter :character="character" />
        </template>
        <template #sideview v-if="!isLoading && !hasError">
            <QpQuestsHistory :logs="questlogs" />
        </template>
        <div v-if="!isLoading && !hasError && quest" class="qp-container">
            <qp-header :title="quest.title" />
            <el-row>
                <el-col>
                    <el-card>
                        <p v-text="quest.description"></p>
                    </el-card>
                </el-col>
                <el-col :span="24" :md="10">
                    <el-button size="large" type="primary" :disabled="!character">
                        <span>Commencer</span>
                    </el-button>
                </el-col>
                <el-col :span="24" :md="14">
                    <el-card>
                        <h2>Récompenses</h2>
                        <div>
                            <span>
                                <span>20 exp</span>
                            </span>
                            <span>
                                <el-icon class="mdi mdi-rhombus-split-outline el-icon--left" />
                                <span>1 234</span>
                            </span>
                            <span>
                                <el-icon class="mdi mdi-orbit el-icon--left" />
                                <span>123</span>
                            </span>
                            <span>
                                <el-icon class="mdi mdi-diamond-stone el-icon--left" />
                                <span>12</span>
                            </span>
                            <span>
                                <el-icon class="mdi mdi-gold el-icon--left" />
                                <span>1</span>
                            </span>
                        </div>
                        <div>
                            <el-button size="large" />
                            <el-button size="large" />
                            <el-button size="large" />
                            <el-button size="large" />
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </div>
        <qp-loading v-else-if="isLoading" />
        <qp-notfound v-else />
    </qp-page>
</template>
