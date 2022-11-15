<script setup lang="ts">
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import { ElMessage } from "element-plus";
import { API, HEADERS } from "../../../plugins/store/index";
import { storeUser } from "../../../plugins/store";
import QpRpgForumMessageCard from "../../../components/rpg/forum/RpgForumMessageCard.vue";
import router from "@/plugins/router";

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
const messages = ref<Array<any>>([])
const messages_total = ref<number>(0)
const messages_size = ref<number>(1)
const message_page = ref<number>(1)

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
        initMessages(route.query?.page ? route.query.page.toString() : null)
    } else {
        if (f.status === 401) ElMessage.error("not authorized")
        else if (f.status === 404) ElMessage.error("not found")
        else ElMessage.error("AnErrorOccurred")
        isLoading.value = false
        hasError.value = `${f.status}`
    }
}

const initMessages = async (page: string|null) => {
    isLoading.value = true
    hasError.value = null
    let slug = rpg.value.slug
    let pk = route.params.topic_pk
    let query = page ? `?page=${page}` : ""
    // ===---
    let f = await fetch(`${API}/rpg/${slug}/forum/topics/${pk}/messages/${query}`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {
        let r = await f.json()
        messages.value = r.results
        messages_total.value = r.count
        messages_size.value = r.size
        if (page) router.replace({path: router.currentRoute.value.path, query: {page: page}})
        if (page && page != "last") message_page.value = parseInt(page)
        else if (page && page == "last") message_page.value = Math.ceil(r.count / r.size)
        else message_page.value = 1
        if (page && page == "last" && messages.value.length) {
            setTimeout(() => {
                let id: number = messages.value[messages.value.length - 1].id
                let el: HTMLElement|null = document.getElementById(`rpg-${slug}-forum-message-${id}`)
                if (el) el.scrollIntoView({behavior: "smooth"})
            }, 100)
        }
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
                <el-col v-for="(message, n) in messages" :key="`rpg-forum-message-${n}`" :span="24">
                    <QpRpgForumMessageCard :rpg="rpg" :message="message" />
                </el-col>
                <el-col>
                    <el-pagination background hide-on-single-page layout="prev, pager, next" v-model:current-page="message_page" :page-size="messages_size" :total="messages_total" @current-change="initMessages" />
                </el-col>
            </el-row>
        </div>
    </div>
    <qp-notfound v-else-if="!isLoading" />
</template>
