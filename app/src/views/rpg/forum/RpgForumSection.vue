<script setup lang="ts">
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import { ElMessage } from "element-plus";
import { API, HEADERS } from "../../../plugins/store/index";
import { storeApp, storeUser } from "../../../plugins/store";
import QpRpgForumTopicCard from "../../../components/rpg/forum/RpgForumTopicCard.vue";

const route = useRoute()

const useStoreApp = storeApp()
const { mainviewWidth } = storeToRefs(useStoreApp)

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
const section = ref<any>(null)

const initRpg = () => {
    isLoading.value = true
    rpg.value = props.rpg
    initSection()
}

const initSection = async () => {
    isLoading.value = true
    hasError.value = null
    let slug = rpg.value.slug
    let pk = route.params.section_pk
    // ===---
    let f = await fetch(`${API}/rpg/${slug}/forum/sections/${pk}/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {
        let r = await f.json()
        document.title = `${r.title} - ${rpg.value.name}`
        section.value = r
        isLoading.value = false
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else if (f.status === 404) ElMessage.error("not found")
        else ElMessage.error("AnErrorOccurred")
        isLoading.value = false
        hasError.value = `${f.status}`
    }
}

onMounted(() => {initRpg()})
</script>

<template>
    <div v-if="!isLoading && !hasError && rpg && section" class="qp-container">
        <qp-header :title="section.title" :content="section.description" :heading="2" title-size="52px" />
        <div class="el-forum-breadcrumb">
            <ul class="el-forum-breadcrumb-list">
                <li v-for="(bread, n) in section.breadcrumb" :key="`qp-bread-${n}`" class="el-forum-breadcrumb-item">
                    <span @click="$router.push({path:bread.path})" v-text="bread.name"></span>
                </li>
            </ul>
        </div>
        <div class="qp-forum-section">
            <div :class="`qp-forum-section-actions ${mainviewWidth < 767 ? 'qp-forum-section-actions-mobile' : mainviewWidth < 1024 ? 'qp-forum-section-actions-minimize' : ''}`">
                <el-col>
                    <el-button type="primary" class="qp-btn-card">
                        <span v-text="$t('NewChapter')"></span>
                    </el-button>
                </el-col>
                <el-col>
                    <el-card>
                        <span v-text="$t('Quests')"></span>
                        <pre>mainviewWidth : {{mainviewWidth }}</pre>
                    </el-card>
                </el-col>
            </div>
            <div :class="`qp-forum-section-topics ${mainviewWidth < 767 ? 'qp-forum-section-topics-mobile' : mainviewWidth < 1024 ? 'qp-forum-section-topics-minimize' : ''}`">
                <el-col v-for="(topic, n) in section.topics" :key="`rpg-forum-topic-${n}`" :span="topic.flag == 3 ? 24 : (mainviewWidth < 1024 ? 24 : mainviewWidth > 1199 ? 8 : 12)">
                    <QpRpgForumTopicCard :rpg="rpg" :topic="topic" />
                </el-col>
            </div>
        </div>
    </div>
    <qp-notfound v-else-if="!isLoading" />
</template>

<style scoped>
.qp-forum-section {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-content: flex-start;
    padding: 0 10px;
}
.qp-forum-section-topics {
    display: flex;
    flex: 1 1 calc(100% - 300px);
    flex-wrap: wrap;
    align-content: flex-start;
    order: 1;
}
.qp-forum-section-topics-minimize {
    flex: 1 1 calc(100% - 300px);
    order: 1;
}
.qp-forum-section-topics-mobile {
    flex: 1 1 100%;
    order: 2;
}
.qp-forum-section-actions {
    flex: 0 0 300px;
    max-width: 300px;
    order: 2;
}
.qp-forum-section-actions-minimize {
    flex: 0 0 300px;
    order: 2;
}
.qp-forum-section-actions-mobile {
    flex: 1 1 100%;
    max-width: 100%;
    order: 1;
}
</style>
