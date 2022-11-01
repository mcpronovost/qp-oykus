<script setup lang="ts">
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useI18n } from "vue-i18n";
import { useRoute } from "vue-router";
import { ElMessage } from "element-plus";
import { API, HEADERS } from "../../../plugins/store/index";
import { storeUser } from "../../../plugins/store";

const { t } = useI18n()

const route = useRoute()

const useStoreUser = storeUser()
const { rat, lang } = storeToRefs(useStoreUser)

const props = defineProps({
    rpg: {
        type: Object,
        required: true
    }
})

const isLoading = ref<boolean>(false)
const hasError = ref<string|null>(null)

const rpg = ref<any>(null)
const forum = ref<any>(null)

const initRpg = () => {
    isLoading.value = true
    rpg.value = props.rpg
    initForum()
}

const initForum = async () => {
    isLoading.value = true
    hasError.value = null
    let pk = props.rpg.forum
    // ===---
    try {
        let f = await fetch(`${API}/forums/${pk}/`, {
            method: "GET",
            headers: HEADERS(rat.value, lang.value)
        })
        if (f.status === 200) {
            let r = await f.json()
            document.title = `${rpg.value.name}`
            forum.value = r
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

onMounted(() => {initRpg()})
</script>

<template>
    <div v-if="!isLoading && !hasError && rpg && forum">
        <div class="qp-container">
            <section v-for="(category, n) in forum.categories" :key="`rpg-forum-category-${n}`">
                <qp-header :title="category.title" :heading="2" />
                <el-row>
                    <el-col v-for="(section, nn) in category.sections" :key="`rpg-forum-section-${n}-${nn}`" :span="24" :md="section.width">
                        <el-card class="rpg-forum-category-section">
                            <div class="rpg-forum-category-section-title">
                                <h3>
                                    <span v-text="section.title" @click="$router.push({path:`/rpg/${rpg.slug}/s${section.id}-${$f.qpSlugify(section.title)}`})"></span>
                                </h3>
                            </div>
                            <div class="rpg-forum-category-section-lastmessage">
                                <el-avatar v-if="section.last_message" :src="section.last_message.author.avatar" :size="120" :style="`background-color:${section.last_message.author.avatar ? 'transparent' : rpg.primary_color};color:#fff;`">
                                    <span v-text="section.last_message.author.initial"></span>
                                </el-avatar>
                                <el-avatar v-if="section.id==4" :size="120" :style="`background-color:${rpg.primary_color};color:#fff;`">
                                    <span v-text="'PWQ'"></span>
                                </el-avatar>
                            </div>
                            <div class="rpg-forum-category-section-track">
                                track
                            </div>
                            <div class="rpg-forum-category-section-lasttopic">
                                last topic
                            </div>
                        </el-card>
                    </el-col>
                    <el-col v-if="!category.sections.length">
                        <el-alert :title="$t('NoSectionsYet')" type="error" center :closable="false" />
                    </el-col>
                </el-row>
            </section>
            <el-row v-if="!forum.categories.length">
                <el-col>
                    <el-alert :title="$t('NoCategoriesYet')" type="error" center :closable="false" />
                </el-col>
            </el-row>
        </div>
    </div>
    <qp-notfound v-else-if="!isLoading" />
</template>
