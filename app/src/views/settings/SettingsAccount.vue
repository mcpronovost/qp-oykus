<script setup lang="ts">
import type { FormInstance, FormRules } from "element-plus";
import type { SettingsAccountForm } from "../../types/settings";
import { reactive, ref } from "vue";
import { storeToRefs } from "pinia";
import { useI18n } from "vue-i18n";
import { ElMessage } from "element-plus";
import { API, HEADERS, storeUser } from "../../plugins/store";

const { t, locale } = useI18n()

const useStoreUser = storeUser()
const { rat, username, email, lang } = storeToRefs(useStoreUser)
const { updateUser } = useStoreUser

const isLoading = ref<boolean>(false)
const hasError = ref<string|null>(null)

const isLoadingSend = ref<boolean>(false)
const hasErrorSend = ref<string|null>(null)
const refAccount = ref<FormInstance>()
const formAccount = reactive<SettingsAccountForm>({
    username: username.value,
    email: email.value,
    lang: lang.value,
    timezone: "America/Toronto"
})

const rulesProject = reactive<FormRules>({
    username: [
        { required: true, message: t("Thisfieldisrequired"), trigger: "blur" }
    ],
    email: [
        { required: true, message: t("Thisfieldisrequired"), trigger: "blur" }
    ],
    lang: [
        { required: true, message: t("Thisfieldisrequired"), trigger: "blur" }
    ],
    timezone: [
        { required: true, message: t("Thisfieldisrequired"), trigger: "blur" }
    ]
})

const handleChangeLang = (value: string) => {
    locale.value = value
}

const doResetAccount = () => {
    refAccount.value?.resetFields()
    locale.value = lang.value
}

const doSubmitAccount = async () => {
    isLoadingSend.value = true
    hasErrorSend.value = null
    await refAccount.value?.validate((valid) => {
        if (valid) {
            doSendAccount()
        } else {
            isLoadingSend.value = false
        }
    })
}

const doSendAccount = async () => {
    isLoadingSend.value = true
    hasErrorSend.value = null
    // ===---
    let data = new FormData()
    data.append("lang", formAccount.lang)
    data.append("timezone", formAccount.timezone)
    // ===---
    let f = await fetch(`${API}/me/settings/account/edit/`, {
        method: "PATCH",
        headers: HEADERS(rat.value, lang.value),
        body: data
    })
    if (f.status === 200) {
        updateUser()
        ElMessage.success(t("SettingsSuccessfullyUpdated"))
        isLoadingSend.value = false
    } else {
        hasErrorSend.value = t("AnErrorOccurred")
        isLoadingSend.value = false
    }
}
</script>

<template>
    <div v-if="!isLoading && !hasError" class="qp-container">
        <qp-header :title="$t('UserAccount')" />
        <el-row>
            <el-col>
                <el-card>
                    <el-form ref="refAccount" :model="formAccount" :rules="rulesProject" label-position="top">
                        <el-row>
                            <el-col :span="24" :md="12">
                                <el-form-item :label="$t('Username')" prop="username">
                                    <el-input :value="username" disabled readonly />
                                </el-form-item>
                            </el-col>
                            <el-col :span="24" :md="12">
                                <el-form-item :label="$t('Email')" prop="email">
                                    <el-input :value="email" disabled readonly />
                                </el-form-item>
                            </el-col>
                            <el-col :span="24" :md="12">
                                <el-form-item :label="$t('Language')" prop="lang">
                                    <el-select v-model="formAccount.lang" @change="handleChangeLang">
                                        <el-option :label="$t('French')" value="fr" />
                                        <el-option :label="$t('English')" value="en" />
                                    </el-select>
                                </el-form-item>
                            </el-col>
                            <el-col :span="24" :md="12">
                                <el-form-item :label="$t('Timezone')" prop="timezone">
                                    <el-select v-model="formAccount.timezone">
                                        <el-option :label="$t('America/Toronto')" value="America/Toronto" />
                                        <el-option :label="$t('Europe/Paris')" value="Europe/Paris" />
                                    </el-select>
                                </el-form-item>
                            </el-col>
                        </el-row>
                        <el-row>
                            <el-col v-if="hasErrorSend" :span="24">
                                <el-alert type="error" show-icon :closable="false">
                                    <p v-html="hasErrorSend"></p>
                                </el-alert>
                            </el-col>
                            <el-col class="qp-right">
                                <el-button :disabled="isLoadingSend" @click="doResetAccount()">
                                    <span v-text="$t('Reset')"></span>
                                </el-button>
                                <el-button type="primary" :loading="isLoadingSend" @click="doSubmitAccount()">
                                    <span v-text="$t('Save')"></span>
                                </el-button>
                            </el-col>
                        </el-row>
                    </el-form>
                </el-card>
            </el-col>
        </el-row>
    </div>
    <qp-notfound v-else-if="!isLoading" />
</template>
