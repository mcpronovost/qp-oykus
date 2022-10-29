<script setup lang="ts">
import { computed } from "vue";
import { useI18n } from "vue-i18n";
import QpChartRadar from "@/components/charts/ChartRadar.vue";

const { t } = useI18n()

const props = defineProps({
    character: {
        type: Object,
        default: () => {}
    }
})

const listCharacterAttributes = computed<Array<any>>(() => {
    if (props.character) {
        return [
            [t('Strength'), props.character.attributes?.strength | 0],
            [t('Constitution'), props.character.attributes?.constitution | 0],
            [t('Perception'), props.character.attributes?.perception | 0],
            [t('Willpower'), props.character.attributes?.willpower | 0],
            [t('Intelligence'), props.character.attributes?.intelligence | 0],
            [t('Dexterity'), props.character.attributes?.dexterity | 0]
        ]
    }
    return []
})
</script>

<template>
    <div v-if="props.character" class="qp-center">
        <div>
            <el-avatar :size="120" :src="props.character.avatar" :style="`background-color:${props.character.avatar ? 'transparent' : props.character.rpg?.primary_color};color:#fff;`">
                <span v-text="props.character.initial"></span>
            </el-avatar>
        </div>
        <div class="qp-questcharacter-name">
            <span v-text="props.character.name"></span>
        </div>
        <div class="qp-questcharacter-identity">
            <span v-text="`${props.character.race}`"></span>
        </div>
        <el-row class="qp-questcharacter-resistances">
            <el-col :span="8">
                <span v-text="$t('Physical')"></span>
                <el-progress type="circle" :percentage="(props.character.resistances?.physical/8)*100">
                    <template #default>
                        <div class="qp-center" v-text="props.character.resistances?.physical"></div>
                    </template>
                </el-progress>
            </el-col>
            <el-col :span="8">
                <span v-text="$t('Mental')"></span>
                <el-progress type="circle" :percentage="(props.character.resistances?.mental/8)*100">
                    <template #default>
                        <div class="qp-center" v-text="props.character.resistances?.mental"></div>
                    </template>
                </el-progress>
            </el-col>
            <el-col :span="8">
                <span v-text="$t('Spiritual')"></span>
                <el-progress type="circle" :percentage="(props.character.resistances?.spiritual/8)*100">
                    <template #default>
                        <div class="qp-center" v-text="props.character.resistances?.spiritual"></div>
                    </template>
                </el-progress>
            </el-col>
        </el-row>
        <qp-chart-radar v-if="listCharacterAttributes.length" :levels="6" :data="listCharacterAttributes" />
        <el-button text size="small">
            <span>Changer de personnage</span>
        </el-button>
    </div>
</template>

<style scoped>
.qp-questcharacter-name {
    font-family: "Quicksand", sans-serif;
    font-size: 24px;
    font-weight: 400;
    line-height: 120%;
    letter-spacing: 2px;
    margin: 12px 0 12px;
}
.qp-questcharacter-identity {
    color: var(--qp-secondary);
    font-size: 14px;
    line-height: 120%;
    margin: 12px 0 24px;
}
.qp-questcharacter-resistances {
    margin: 0 0 24px;
}
.qp-questcharacter-resistances span {
    font-size: 12px;
    line-height: 120%;
    text-align: center;
    word-break: break-word;
    opacity: 0.6;
}
</style>
