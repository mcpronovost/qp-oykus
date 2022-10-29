<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { storeToRefs } from "pinia";
import { ElMessage } from "element-plus";
import { API, HEADERS } from "../plugins/store/index";
import QpChartRadar from "@/components/charts/ChartRadar.vue";
import { useI18n } from "vue-i18n";
import { storeUser } from "../plugins/store";

const { t } = useI18n()

const useStoreUser = storeUser()
const { rat, lang } = storeToRefs(useStoreUser)

const isLoading = ref<boolean>(false)
const hasError = ref<string|null>(null)

const isLoadingCharacter = ref<boolean>(false)
const hasErrorCharacter = ref<string|null>(null)
const character = ref<any>(null)

const listCharacterAttributes = computed<Array<any>>(() => {
    return [
        [t('Strength'), character.value.attributes?.strength | 0],
        [t('Constitution'), character.value.attributes?.constitution | 0],
        [t('Perception'), character.value.attributes?.perception | 0],
        [t('Willpower'), character.value.attributes?.willpower | 0],
        [t('Intelligence'), character.value.attributes?.intelligence | 0],
        [t('Dexterity'), character.value.attributes?.dexterity | 0]
    ]
})

const doCharacterDetail = async (pk: Number) => {
    isLoadingCharacter.value = true
    hasErrorCharacter.value = null
    // ===---
    let f = await fetch(`${API}/characters/${pk}/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {
        let r = await f.json()
        character.value = r
        isLoadingCharacter.value = false
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else if (f.status === 404) ElMessage.error("not found")
        else ElMessage.error("AnErrorOccurred")
        isLoadingCharacter.value = false
        hasErrorCharacter.value = `${f.status}`
    }
}

onMounted(() => {
    doCharacterDetail(1)
})

</script>

<template>
    <qp-page :sidenav-title="$t('Character')">
        <template #sidenav>
            <div v-if="!hasErrorCharacter && !isLoadingCharacter && character" class="qp-center">
                <div>
                    <el-avatar :size="120" :style="`background-color:${character.rpg?.primary_color};color:#fff;`">
                        <span v-text="character.initial"></span>
                    </el-avatar>
                </div>
                <div>
                    <span v-text="character.name"></span>
                </div>
                <div>
                    <span>Ladkani, Kshirsagar</span>
                </div>
                <div>
                    <span>Humaine, 32 ans</span>
                </div>
                <el-row>
                    <el-col :span="8">
                        <el-progress type="circle" :percentage="(character.resistances?.physical/8)*100">
                            <template #default>
                                <div class="qp-center" v-text="character.resistances?.physical"></div>
                            </template>
                        </el-progress>
                    </el-col>
                    <el-col :span="8">
                        <el-progress type="circle" :percentage="(character.resistances?.mental/8)*100">
                            <template #default>
                                <div class="qp-center" v-text="character.resistances?.mental"></div>
                            </template>
                        </el-progress>
                    </el-col>
                    <el-col :span="8">
                        <el-progress type="circle" :percentage="(character.resistances?.spiritual/8)*100">
                            <template #default>
                                <div class="qp-center" v-text="character.resistances?.spiritual"></div>
                            </template>
                        </el-progress>
                    </el-col>
                </el-row>
                <qp-chart-radar :levels="6" :data="listCharacterAttributes" />
                <el-button text size="small">
                    <span>Changer de personnage</span>
                </el-button>
            </div>
            <div v-else-if="isLoadingCharacter" v-loading="isLoadingCharacter" element-loading-background="transparent" style="height:200px"></div>
            <div v-else-if="hasErrorCharacter">
                <el-alert type="error" :closable="false">
                    <p v-html="hasErrorCharacter"></p>
                </el-alert>
            </div>
        </template>
        <div v-if="!isLoading && !hasError" class="qp-container">
            <qp-header :title="`Couper du bois`" />
            <el-row>
                <el-col>
                    <el-card>
                        <p v-text="`Couper et débiter les grands chênes de la région pour en récupérer les ressources.`"></p>
                    </el-card>
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
                <el-col :span="24" :md="10">
                    <el-button size="large" type="primary" class="qp-block qp-w100">
                        <span>Commencer</span>
                    </el-button>
                </el-col>
            </el-row>
        </div>
        <qp-notfound v-else-if="!isLoading" />
    </qp-page>
</template>
