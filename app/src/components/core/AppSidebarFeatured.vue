<script setup lang="ts">
import { onMounted, ref } from "vue";
import { storeToRefs } from "pinia";
import { storeUser } from "../../plugins/store";
import { API, HEADERS } from "../../plugins/store/index";

const useStoreUser = storeUser()
const { rat, lang } = storeToRefs(useStoreUser)

const listFeatured = ref<Array<any>>([])

const getFeaturedProjects = async () => {
    let f = await fetch(`${API}/rpg/?limit=6`, {
        method: "GET",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {
        let r = await f.json()
        listFeatured.value = r.results
    }
}

onMounted(() => {
    getFeaturedProjects()
})
</script>

<template>
    <li v-if="listFeatured.length" class="qp-sidebar-nav-list-item">
        <el-icon size="large">
            <i class="mdi mdi-star-outline"></i>
        </el-icon>
    </li>
    <li v-for="(obj, n) in listFeatured" :key="`featured-${n}`" class="qp-sidebar-nav-list-item">
        <el-tooltip placement="left" :content="obj.name">
            <el-button size="large" circle @click="$router.push({name:'RpgForum', params:{slug:`${obj.slug}`}})">
                <el-avatar :src="obj.icon" :size="40" :style="`background-color:${obj.icon ? 'transparent' : obj.primary_color};color:#fff;`">
                    <span v-text="obj.initial"></span>
                </el-avatar>
            </el-button>
        </el-tooltip>
    </li>
</template>