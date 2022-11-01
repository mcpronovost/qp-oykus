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
const category = ref<any>(null)

const initRpg = () => {
    isLoading.value = true
    rpg.value = props.rpg
    initCategory()
}

const initCategory = async () => {
    isLoading.value = true
    hasError.value = null
    let pk = route.params.category_pk
    // ===---
    let f = await fetch(`${API}/forums/categories/${pk}/`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {
        let r = await f.json()
        document.title = `${r.title} - ${rpg.value.name}`
        category.value = r
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
    <div v-if="!isLoading && !hasError && rpg && category" class="qp-container">
        <qp-header :title="category.title" :content="category.description" :heading="2" />
        <div class="el-forum-breadcrumb">
            <ul class="el-forum-breadcrumb-list">
                <li v-for="(bread, n) in category.breadcrumb" :key="`qp-bread-${n}`" class="el-forum-breadcrumb-item">
                    <span @click="$router.push({path:bread.path})" v-text="bread.name"></span>
                </li>
            </ul>
        </div>
        <el-row>
            <el-col v-for="(section, n) in category.sections" :key="`rpg-forum-section-${n}`">
                <el-card>
                    <pre>{{section}}</pre>
                </el-card>
            </el-col>
        </el-row>
    </div>
    <qp-notfound v-else-if="!isLoading" />
</template>
