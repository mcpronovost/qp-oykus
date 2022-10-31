<script setup lang="ts">
import { h, onMounted, onBeforeUnmount, ref } from "vue";
import { storeToRefs } from "pinia";
import { API, HEADERS } from "../plugins/store/index";
import { useI18n } from "vue-i18n";
import { useRoute } from "vue-router";
import { storeUser } from "../plugins/store";
import { ElMessage, ElMessageBox } from "element-plus";
import QpQuestsCharacter from "../components/quests/QuestsCharacter.vue";
import QpQuestsHistory from "../components/quests/QuestsHistory.vue";
import wood from "@/assets/img/items/wood-pile.svg";
import acorn from "@/assets/img/items/acorn.svg";
import oakleaf from "@/assets/img/items/oak-leaf.svg";

const { t } = useI18n()

const route = useRoute()

const pk = ref<number>(0)

const useStoreUser = storeUser()
const { rat, lang, id } = storeToRefs(useStoreUser)

const isLoading = ref<boolean>(false)
const isLoadingQuest = ref<boolean>(false)
const hasError = ref<string|null>(null)

const quest = ref<any>(null)
const questInterval = ref<any>(null)
const questProgression = ref<any>(0)
const character = ref<any>(null)
const questlogs = ref<Array<any>>([])

const doQuestProgression = () => {
    if (quest.value && quest.value.current) {
        let start = new Date(quest.value.current.start).getTime()
        let end = new Date(quest.value.current.end).getTime() - start
        let now = new Date().getTime() - start
        let r = (now * 100) / end
        if (r > 100) {
            clearInterval(questInterval.value)
            questProgression.value = 100
        }
        else questProgression.value = parseFloat(r.toFixed(2))
    } else questProgression.value = 0
}

const doQuestDetail = async (update = false) => {
    if (!update) isLoading.value = true
    hasError.value = null
    if (!update) quest.value = null
    // ===---
    try {
        let f = await fetch(`${API}/quests/${pk.value}/`, {
            method: "GET",
            headers: HEADERS(rat.value, lang.value)
        })
        if (f.status === 200) {
            let r = await f.json()
            quest.value = r
            character.value = r.characters[0]
            if (r.current) {
                questInterval.value = setInterval(() => {
                    doQuestProgression()
                }, 1000)
            }
            doQuestLogsList(update)
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

const doQuestLogsList = async (update = false) => {
    if (!update) isLoading.value = true
    hasError.value = null
    if (!update) questlogs.value = []
    // ===---
    try {
        let f = await fetch(`${API}/quests/${pk.value}/logs/`, {
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

const doQuestStart = async () => {
    doQuestProgression()
    isLoadingQuest.value = true
    // ===---
    try {
        let data = new FormData()
        if (id.value) data.append("user", id.value.toString())
        data.append("quest", pk.value.toString())
        data.append("character", character.value.id.toString())
        // ===---
        let f = await fetch(`${API}/quests/${pk.value}/start/`, {
            method: "POST",
            headers: HEADERS(rat.value, lang.value),
            body: data
        })
        if (f.status === 200) {
            doQuestDetail(true)
            isLoadingQuest.value = false
        } else {
            if (f.status === 401) throw t("YouAreNotAuthorizedToDoThat")
            else if (f.status === 404) throw t("ContentNotFound")
            else throw t("AnErrorOccurred")
        }
    } catch (e) {
        if (typeof(e) === "string") ElMessage.error(`${e}`)
        else ElMessage.error(t("AnErrorOccurred"))
        isLoadingQuest.value = false
    }
}

const doQuestEnd = async () => {
    doQuestProgression()
    isLoadingQuest.value = true
    // ===---
    try {
        let data = new FormData()
        if (id.value) data.append("user", id.value.toString())
        data.append("quest", pk.value.toString())
        data.append("character", quest.value.current.character.id.toString())
        data.append("questlog", quest.value.current.id.toString())
        // ===---
        let f = await fetch(`${API}/quests/${pk.value}/end/`, {
            method: "POST",
            headers: HEADERS(rat.value, lang.value),
            body: data
        })
        if (f.status === 200) {
            let r = await f.json()
            if (r.valid) {
                let title = t("QuestFailed")
                let msg = t("YouFailedTheQuest")
                let popclass = "qp-quest-popfail"
                let vtext = <Array<any>>[]
                if (r.is_success) {
                    title = t("QuestSuccessful")
                    msg = t("YouSuccessfullyCompletedTheQuest")
                    popclass = "qp-quest-popsuccess"
                }
                Object.entries(r.rewards_currencies).forEach(([k, v]) => {
                    if (k == "exp") {
                        vtext.push(
                            h("li", null, `${v} exp`)
                        )
                    } else {
                        vtext.push(
                            h("li", null, [
                                h("el-icon", {class: `el-icon el-icon--left ${k}`}),
                                h("span", null, `${v}`)
                            ])
                        )
                    }
                })
                ElMessageBox({
                    title: title,
                    message: h("div", null, [
                        h("div", {class: "qp-quest-poptext"}, msg),
                        h("div", {class: "el-divider el-divider--horizontal"}, ""),
                        h("div", {class: "qp-quest-poptitle"}, t("RewardsReceived")),
                        h("ul", {class: "qp-quest-popcurrencies"}, vtext)
                    ]),
                    center: true,
                    autofocus: false,
                    customClass: popclass
                })
                doQuestDetail(true)
            }
            isLoadingQuest.value = false
        } else {
            if (f.status === 401) throw t("YouAreNotAuthorizedToDoThat")
            else if (f.status === 404) throw t("ContentNotFound")
            else throw t("AnErrorOccurred")
        }
    } catch (e) {
        if (typeof(e) === "string") ElMessage.error(`${e}`)
        else ElMessage.error(t("AnErrorOccurred"))
        isLoadingQuest.value = false
    }
}

onMounted(() => {
    pk.value = parseInt(route.params.pk.toString())
    doQuestDetail()
})

onBeforeUnmount(() => {
    clearInterval(questInterval.value)
})

</script>

<template>
    <qp-page :sidenav-title="$t('Character')" :sideview-title="$t('History')">
        <template #sidenav v-if="!isLoading && !hasError">
            <QpQuestsCharacter :quest="quest" :character="character" />
        </template>
        <template #sideview v-if="!isLoading && !hasError">
            <QpQuestsHistory :logs="questlogs" />
        </template>
        <div v-if="!isLoading && !hasError && quest" class="qp-container">
            <qp-header :title="quest.title" :content="`${quest.section.categorie}, ${quest.section.title}`" />
            <el-row>
                <el-col>
                    <el-card>
                        <p v-text="quest.description"></p>
                    </el-card>
                </el-col>
                <el-col v-if="!quest.current" :span="24">
                    <el-card class="qp-quest-rewards">
                        <h2 class="qp-quest-rewards-title">
                            <span v-text="$t('Rewards')"></span>
                        </h2>
                        <div class="qp-quest-rewards-currencies">
                            <div>
                                <span v-text="`${quest.reward_exp} exp`"></span>
                            </div>
                            <div v-for="(currency, n) in quest.reward_currencies" :key="`qp-reward-currency-${n}`">
                                <el-icon :class="`el-icon--left ${currency.icon}`" />
                                <span v-if="currency.amount_min != currency.amount_max" v-text="`${currency.amount_min}-${currency.amount_max}`"></span>
                                <span v-else v-text="`${currency.amount_min}`"></span>
                            </div>
                        </div>
                        <div class="qp-quest-rewards-items">
                            <div>
                                <el-avatar :src="wood" shape="square" />
                                <span>3-10</span>
                            </div>
                            <div>
                                <el-avatar :src="acorn" shape="square" />
                                <span>1-2</span>
                            </div>
                            <div>
                                <el-avatar :src="oakleaf" shape="square" />
                                <span>1-2</span>
                            </div>
                        </div>
                    </el-card>
                </el-col>
                <el-col v-if="!quest.current" :span="24">
                    <el-button size="large" type="primary" :disabled="!character" :loading="isLoadingQuest" @click="doQuestStart()">
                        <span v-text="$t('StartQuest')"></span>
                    </el-button>
                </el-col>
                <el-col v-if="quest.current" :span="24">
                    <el-progress v-if="questProgression < 100" :percentage="questProgression > 0 ? questProgression : 50" :indeterminate="questProgression === 0" :duration="1" :stroke-width="24" :show-text="questProgression > 0" :text-inside="true" :color="'var(--qp-primary-dark-3)'" />
                    <el-button v-else-if="questProgression >= 100" type="primary" size="large" :loading="isLoadingQuest" class="qp-block qp-w100" @click="doQuestEnd()">
                        <span v-text="$t('CompleteQuest')"></span>
                    </el-button>
                </el-col>
            </el-row>
        </div>
        <qp-loading v-else-if="isLoading" />
        <div v-else-if="!character">
            <div class="qp-container qp-centered">
                <el-row>
                    <el-col style="text-align:center;">
                        <el-result :title="$t('Error')" :sub-title="$t('NoCharacterAvailable')">
                            <template #icon>
                                <el-icon class="mdi mdi-emoticon-sad-outline" :size="120" />
                            </template>
                        </el-result>
                    </el-col>
                </el-row>
            </div>
        </div>
        <qp-notfound v-else />
    </qp-page>
</template>

<style scoped>
.qp-quest-rewards-title {
    color: var(--qp-secondary);
    font-family: "Quicksand", sans-serif;
    font-size: 28px;
    font-weight: 400;
    line-height: 120%;
    letter-spacing: 2px;
    margin: 0 0 24px;
}
.qp-quest-rewards-currencies {
    margin: 24px 0;
}
.qp-quest-rewards-currencies div {
    display: inline-block;
    margin: 0 48px 0 0;
}
.qp-quest-rewards-items {
    margin: 24px 0 0;
}
.qp-quest-rewards-items div {
    background-color: var(--qp-card-bg-light-1);
    display: inline-block;
    position: relative;
    padding: 8px 12px;
    margin: 0 20px 0 0;
}
.qp-quest-rewards-items div span:not(.el-avatar) {
    color: var(--qp-primary);
    font-size: 10px;
    line-height: 120%;
    position: absolute;
    right: 3px;
    bottom: 1px;
}
.qp-quest-rewards-items .el-avatar {
    --el-avatar-bg-color: transparent;
    --el-avatar-size: 28px;
}
</style>

<style>
body .el-message-box.qp-quest-popsuccess {
    --el-border-color-lighter: var(--qp-success-dark-2);
}
body .el-message-box.qp-quest-popfail {
    --el-border-color-lighter: var(--qp-error-dark-2);
}
.qp-quest-popsuccess .el-divider,
.qp-quest-popfail .el-divider {
    margin: 24px 0 0;
}
.qp-quest-poptext {
    font-size: 16px;
    font-weight: 400;
    margin: 12px 0 24px;
}
.qp-quest-poptitle {
    font-family: "Quicksand", sans-serif;
    font-size: 16px;
    font-weight: 400;
    letter-spacing: 2px;
    margin: 24px 0 0;
}
.qp-quest-popcurrencies {
    list-style: none;
    padding: 0;
    margin: 0;
}
.qp-quest-popcurrencies li {
    list-style: none;
    display: inline-block;
    padding: 0;
    margin: 24px 20px;
}
</style>
