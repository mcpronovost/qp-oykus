<script setup lang="ts">
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useI18n } from "vue-i18n";
import { useRoute } from "vue-router";
import { API, HEADERS } from "../../../plugins/store/index";
import { storeUser } from "../../../plugins/store";
import QpRpgForumSectionCard from "../../../components/rpg/forum/RpgForumSectionCard.vue";

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
    let slug = props.rpg.slug
    // ===---
    try {
        let f = await fetch(`${API}/rpg/${slug}/forum/`, {
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
                        <QpRpgForumSectionCard :rpg="rpg" :section="section" />
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
