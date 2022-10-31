<script setup lang="ts">
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRoute } from "vue-router";
import { ElMessage } from "element-plus";
import { API, HEADERS } from "../../../plugins/store/index";
import { storeUser } from "../../../plugins/store";

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
    let f = await fetch(`${API}/forums/${pk}/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {
        let r = await f.json()
        forum.value = r
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
    <div v-if="!isLoading && !hasError && rpg" class="qp-container">
        <section v-for="(category, n) in forum.categories" :key="`rpg-forum-category-${n}`">
            <qp-header :title="category.title" title-size="52px" />
            <el-row>
                <el-col v-for="(section, nn) in category.sections" :key="`rpg-forum-section-${n}-${nn}`">
                    <el-card>
                        <pre>{{section}}</pre>
                    </el-card>
                </el-col>
            </el-row>
        </section>
    </div>
    <qp-notfound v-else-if="!isLoading" />
</template>
