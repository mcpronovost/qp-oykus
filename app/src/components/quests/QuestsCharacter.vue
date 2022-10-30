<script setup lang="ts">
import { computed } from "vue";
import { useI18n } from "vue-i18n";
import QpChartRadar from "@/components/charts/ChartRadar.vue";

const { t } = useI18n()

const props = defineProps({
    quest: {
        type: Object,
        default: () => {}
    },
    character: {
        type: Object,
        default: () => {}
    }
})

const character = computed(() => {
    if (props.character) {
        return props.character
    } else if (props.quest?.current?.character) {
        return props.quest.current.character
    } else {
        return null
    }
})

const listCharacterAttributes = computed<Array<any>>(() => {
    if (character.value) {
        return [
            [t('Strength'), character.value.attributes?.strength | 0],
            [t('Constitution'), character.value.attributes?.constitution | 0],
            [t('Perception'), character.value.attributes?.perception | 0],
            [t('Willpower'), character.value.attributes?.willpower | 0],
            [t('Intelligence'), character.value.attributes?.intelligence | 0],
            [t('Dexterity'), character.value.attributes?.dexterity | 0]
        ]
    }
    return []
})
</script>

<template>
    <div v-if="character" class="qp-center">
        <div>
            <el-avatar :size="120" :src="character.avatar" :style="`background-color:${character.avatar ? 'transparent' : character.rpg?.primary_color};color:#fff;`">
                <span v-text="character.initial"></span>
            </el-avatar>
        </div>
        <div class="qp-questcharacter-name">
            <span v-text="character.name"></span>
        </div>
        <div class="qp-questcharacter-identity">
            <span v-text="`${character.race}`"></span>
        </div>
        <el-row class="qp-questcharacter-resistances">
            <el-col :span="8">
                <span v-text="$t('Physical')"></span>
                <el-progress type="circle" :percentage="(character.resistances?.physical/8)*100">
                    <template #default>
                        <div class="qp-center" v-text="character.resistances?.physical"></div>
                    </template>
                </el-progress>
            </el-col>
            <el-col :span="8">
                <span v-text="$t('Mental')"></span>
                <el-progress type="circle" :percentage="(character.resistances?.mental/8)*100">
                    <template #default>
                        <div class="qp-center" v-text="character.resistances?.mental"></div>
                    </template>
                </el-progress>
            </el-col>
            <el-col :span="8">
                <span v-text="$t('Spiritual')"></span>
                <el-progress type="circle" :percentage="(character.resistances?.spiritual/8)*100">
                    <template #default>
                        <div class="qp-center" v-text="character.resistances?.spiritual"></div>
                    </template>
                </el-progress>
            </el-col>
        </el-row>
        <qp-chart-radar v-if="listCharacterAttributes.length" :levels="6" :data="listCharacterAttributes" />
        <el-row v-if="props.quest?.skills && character.skills" class="qp-quest-character-skills">
            <el-col v-for="(skill, n) in props.quest.skills" :key="`quest-character-skill-${n}`">
                <div class="qp-quest-character-skills-header">
                    <span v-text="character.skills[skill].name"></span>
                    <span v-text="$t('Lvl', [character.skills[skill].level])"></span>
                </div>
                <el-progress :percentage="(character.skills[skill].exp/character.skills[skill].next)*100" :stroke-width="4" :show-text="false" />
            </el-col>
        </el-row>
        <div v-if="!props.quest.current && props.quest.characters.length > 1">
            <el-button text size="small">
                <span>Changer de personnage</span>
            </el-button>
        </div>
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
.qp-quest-character-skills {
    font-size: 12px;
    line-height: 120%;
    margin: 24px 0 0;
}
.qp-quest-character-skills-header {
    color: var(--qp-secondary);
    text-align: left;
    display: flex;
    flex-direction: row;
    align-items: flex-end;
    justify-content: space-between;
    margin: 0 0 6px;
}
.qp-quest-character-skills-header span + span {
    text-align: right;
}
</style>
