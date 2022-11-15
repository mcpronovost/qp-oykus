<script setup lang="ts">
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import { ElMessage } from "element-plus";
import { API, HEADERS } from "../../../plugins/store/index";
import { storeUser } from "../../../plugins/store";
import QpRpgForumMessageCard from "../../../components/rpg/forum/RpgForumMessageCard.vue";

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
const topic = ref<any>(null)

const initRpg = () => {
    isLoading.value = true
    rpg.value = props.rpg
    initTopic()
}

const initTopic = async () => {
    isLoading.value = true
    hasError.value = null
    let slug = rpg.value.slug
    let pk = route.params.topic_pk
    // ===---
    let f = await fetch(`${API}/rpg/${slug}/forum/topics/${pk}/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {
        let r = await f.json()
        document.title = `${r.title} - ${rpg.value.name}`
        topic.value = r
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
    <div v-if="!isLoading && !hasError && rpg && topic" class="qp-container">
        <qp-header :title="topic.title" :content="topic.description" :heading="2" title-size="52px" />
        <div class="el-forum-breadcrumb">
            <ul class="el-forum-breadcrumb-list">
                <li v-for="(bread, n) in topic.breadcrumb" :key="`qp-bread-${n}`" class="el-forum-breadcrumb-item">
                    <span @click="$router.push({path:bread.path})" v-text="bread.name"></span>
                </li>
            </ul>
        </div>
        <div class="qp-forum-topic">
            <el-row>
                <el-col v-for="(message, n) in topic.messages" :key="`rpg-forum-message-${n}`" :span="24">
                    <QpRpgForumMessageCard :rpg="rpg" :message="message" />
                </el-col>
                <el-col v-for="(message, n) in topic.messages" :key="`rpg-forum-message-${n}`" :span="24">
                    <QpRpgForumMessageCard :rpg="rpg" :message="message" />
                </el-col>
            </el-row>
        </div>
    </div>
    <qp-notfound v-else-if="!isLoading" />
</template>
