<script setup lang="ts">
import { ref, onMounted } from "vue";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";
import { API, HEADERS } from "../../plugins/store/index";
import { storeUser } from "../../plugins/store";

const router = useRouter()

const useStoreUser = storeUser()
const { rat } = storeToRefs(useStoreUser)
const { cleanUser } = useStoreUser

const isLoadingLogout = ref(false)
const hasErrorLogout = ref()

const doLogout = async () => {
    isLoadingLogout.value = true
    // ===---
    await fetch(`${API}/logout/`, {
        method: "POST",
        headers: HEADERS(rat.value),
        body: null
    })
    cleanUser()
    router.push({name: "Home"})
}

onMounted(() => {
    doLogout()
})
</script>

<template>
    <el-row id="qp-auth-logout">
        <el-col>
            <el-card class="qp-center">
                <h1 v-text="$t('Logout')"></h1>
                <el-alert v-if="hasErrorLogout" type="error" show-icon :closable="false">
                    <p v-html="hasErrorLogout"></p>
                </el-alert>
                <div class="qp-form-submit">
                    <el-button type="primary" :loading="isLoadingLogout" @click="doLogout()">
                        <span v-text="$t('LogoutMe')"></span>
                    </el-button>
                </div>
            </el-card>
        </el-col>
    </el-row>
</template>

<style scoped>
#qp-auth-logout .el-card {
    border-bottom: 2px solid var(--qp-primary);
    width: 300px;
}
#qp-auth-logout .el-alert {
    margin: 32px auto 0;
}
#qp-auth-logout .qp-form-submit {
    margin: 32px 12px 32px;
}
</style>
