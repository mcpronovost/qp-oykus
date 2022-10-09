<script setup>
import { reactive, ref } from "vue";
import { useI18n } from "vue-i18n";
import { API } from "@/plugins/store/index";
import { storeUser } from "@/plugins/store";
import { Lock, User } from "@element-plus/icons-vue";
import router from "@/plugins/router";

const { t } = useI18n()

const useStoreUser = storeUser()
const { updateRat } = useStoreUser

const isLoadingLogin = ref(false)
const hasErrorLogin = ref()
const refLogin = ref()

const formLogin = reactive({
    username: "",
    password: ""
})

const rulesLogin = reactive({
    username: [
        { required: true, message: t("Thisfieldisrequired"), trigger: "blur" },
        { min: 5, max: 150, message: t("LengthshouldbebetweenXandX", [5, 150]), trigger: "blur" }
    ],
    password: [
        { required: true, message: t("Thisfieldisrequired"), trigger: "blur" },
        { min: 8, max: 254, message: t("LengthshouldbebetweenXandX", [6, 254]), trigger: "blur" }
    ]
})

const doSubmitLogin = async () => {
    isLoadingLogin.value = true
    hasErrorLogin.value = null
    await refLogin.value.validate((valid) => {
        if (valid) {
            doLogin()
        } else {
            isLoadingLogin.value = false
        }
    })
}

const doLogin = async () => {
    isLoadingLogin.value = true
    // ===---
    let data = new FormData()
    data.append("username", formLogin.username)
    data.append("password", formLogin.password)
    // ===---
    let f = await fetch(`${API}/login/`, {
        method: "POST",
        body: data
    })
    if (f.status === 200) {
        let r = await f.json()
        updateRat(r.token)
        goTo({name: "Home"})
    } else if (f.status === 400) {
        hasErrorLogin.value = t("InvalidCredentials")
        isLoadingLogin.value = false
    } else {
        hasErrorLogin.value = t("AnErrorOccurred")
        isLoadingLogin.value = false
    }
}

const goTo = (obj) => {
    router.push(obj)
}
</script>

<template>
    <el-row id="qp-auth-login">
        <el-col>
            <el-card>
                <h1 v-text="$t('Login')"></h1>
                <el-form ref="refLogin" :model="formLogin" :rules="rulesLogin" label-position="top" status-icon>
                    <el-form-item prop="username">
                        <el-input v-model="formLogin.username" :placeholder="$t('Username')" :prefix-icon="User" />
                    </el-form-item>
                    <el-form-item prop="password">
                        <el-input v-model="formLogin.password" :placeholder="$t('Password')" :prefix-icon="Lock" type="password" />
                    </el-form-item>
                    <el-alert v-if="hasErrorLogin" type="error" show-icon :closable="false">
                        <p v-html="hasErrorLogin"></p>
                    </el-alert>
                    <el-form-item class="qp-form-submit">
                        <el-button type="primary" :loading="isLoadingLogin" @click="doSubmitLogin()">
                            <span v-text="$t('LoginMe')"></span>
                        </el-button>
                    </el-form-item>
                    <el-form-item class="qp-form-switchauth">
                        <el-button text size="small" :disabled="isLoadingLogin" @click="goTo({name:'AuthRegister'})">
                            <span v-text="$t('Donthaveanaccount')"></span>
                        </el-button>
                    </el-form-item>
                </el-form>
            </el-card>
        </el-col>
    </el-row>
</template>

<style scoped>
#qp-auth-login .el-card {
    border-bottom: 2px solid var(--qp-primary);
}
#qp-auth-login .el-form {
    width: 300px;
    padding: 32px 12px;
}
</style>
