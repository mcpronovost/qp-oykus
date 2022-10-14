<script setup lang="ts">
import type { UploadRawFile, UploadInstance, UploadProps, FormInstance, FormRules } from "element-plus";
import type { SettingsProfileForm } from "../../types/settings";
import { reactive, ref } from "vue";
import { storeToRefs } from "pinia";
import { useI18n } from "vue-i18n";
import { ElMessage } from "element-plus";
import { Picture } from "@element-plus/icons-vue";
import { API, HEADERS, storeUser } from "../../plugins/store";

const { t, locale } = useI18n()

const useStoreUser = storeUser()
const { rat, name, initial, avatar, lang } = storeToRefs(useStoreUser)
const { updateUser } = useStoreUser

const isLoading = ref<boolean>(false)
const hasError = ref<string|null>(null)

const isLoadingSend = ref<boolean>(false)
const hasErrorSend = ref<string|null>(null)
const refProfile = ref<FormInstance>()
const refProfileAvatar = ref<UploadInstance>()
const formProfile = reactive<SettingsProfileForm>({
    name: name.value,
    avatar: null,
    avatar_file: avatar.value
})

const rulesProject = reactive<FormRules>({
    name: [
        { required: true, message: t("Thisfieldisrequired"), trigger: "blur" }
    ]
})

const checkAvatarSizes = (file: UploadRawFile) => {
    let url = URL.createObjectURL(file)
    return new Promise(function(resolve, reject){
        let img = new Image()
        img.onload = function(){
            if (img.width !== 200 || img.height !== 200) {
                reject(false)
            } else {resolve(true)}
        }
        img.onerror = function(){reject(false)}
        img.src = url
    })
}

const doChangeAvatar: UploadProps["onChange"] = async (event) => {
    if (event && event.raw) {
        let checkAvatar = await checkAvatarSizes(event.raw).then((r) => {return r}).catch((r) => {return r})
        if (!checkAvatar) {
            ElMessage.error(t("ImageSizeMustBe", ["200x200"]))
            return false
        }
        if (!["image/jpeg","image/png"].includes(event.raw.type)) {
            ElMessage.error(t("FileFormatMustBeJPGORPNG"))
            return false
        } else if (event.raw.size / 1024 > 50) {
            ElMessage.error(t("FileSizeCanNotExceed", ["50ko"]))
            return false
        }
        formProfile.avatar = event.raw
        formProfile.avatar_file = URL.createObjectURL(event.raw)
    } else { return false}
    return true
}

const doExceedAvatar: UploadProps["onExceed"] = (files) => {
    const file = files[0] as UploadRawFile
    refProfileAvatar.value?.clearFiles()
    refProfileAvatar.value?.handleStart(file)
}

const doResetProfile = () => {
    refProfile.value?.resetFields()
    formProfile.avatar = null
    formProfile.avatar_file = avatar.value
    locale.value = lang.value
}

const doSubmitProfile = async () => {
    isLoadingSend.value = true
    hasErrorSend.value = null
    await refProfile.value?.validate((valid) => {
        if (valid) {
            doSendProfile()
        } else {
            isLoadingSend.value = false
        }
    })
}

const doSendProfile = async () => {
    isLoadingSend.value = true
    hasErrorSend.value = null
    // ===---
    let data = new FormData()
    data.append("name", `${formProfile.name}`)
    if (formProfile.avatar) {
        data.append("avatar", formProfile.avatar)
    }
    // ===---
    let f = await fetch(`${API}/me/settings/profile/edit/`, {
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
        <qp-header :title="$t('Profile')" />
        <el-form ref="refProfile" :model="formProfile" :rules="rulesProject" label-position="top">
            <el-row>
                <el-col :span="24" :md="10">
                    <div class="qp-settings-heading">
                        <el-card class="qp-h100">
                            <div class="qp-settings-heading-wrapper">
                                <el-avatar :src="formProfile.avatar_file" :size="120">
                                    <span v-text="initial"></span>
                                </el-avatar>
                            </div>
                        </el-card>
                    </div>
                </el-col>
                <el-col :span="24" :sm="12" :md="7">
                    <el-upload ref="refProfileAvatar" action="#" accept="image/jpeg,image/png" :auto-upload="false" :show-file-list="false" :limit="1" :on-change="doChangeAvatar" :on-exceed="doExceedAvatar" class="qp-settings-upload-btncard">
                        <el-card class="qp-settings-btncard">
                            <div class="qp-settings-btncard-wrapper">
                                <el-icon :size="32" color="var(--qp-secondary)">
                                    <Picture />
                                </el-icon>
                                <p class="qp-settings-btncard-title" v-text="$t('ChangeAvatar')"></p>
                                <p class="qp-settings-btncard-caption" v-text="$t('Dimensions:', ['200x200'])"></p>
                            </div>
                        </el-card>
                    </el-upload>
                </el-col>
                <el-col :span="24" :sm="12" :md="7">
                    <el-card class="qp-settings-btncard">
                        <div class="qp-settings-btncard-wrapper">
                            <p v-text="`(${$t('soon')})`"></p>
                        </div>
                    </el-card>
                </el-col>
                <el-col>
                    <el-card>
                        <el-row>
                            <el-col :span="24" :md="24">
                                <el-form-item :label="$t('Name')" prop="name">
                                    <el-input v-model="formProfile.name" />
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
                                <el-button :disabled="isLoadingSend" @click="doResetProfile()">
                                    <span v-text="$t('Reset')"></span>
                                </el-button>
                                <el-button type="primary" :loading="isLoadingSend" @click="doSubmitProfile()">
                                    <span v-text="$t('Save')"></span>
                                </el-button>
                            </el-col>
                        </el-row>
                    </el-card>
                </el-col>
            </el-row>
        </el-form>
    </div>
    <qp-notfound v-else-if="!isLoading" />
</template>

<style>
.qp-settings-heading {
    height: 100%;
}
.qp-settings-heading-wrapper {
    text-align: center;
    height: 100%;
}
.qp-settings-upload-btncard {
    height: 100%;
}
.qp-settings-upload-btncard .el-upload {
    display: block;
    width: 100%;
    height: 100%;
}
.qp-settings-btncard {
    text-align: center;
    height: 100%;
}
.qp-settings-btncard:hover {
    box-shadow: 0 4px 4px rgba(0, 0, 0, 0.04)!important;
    cursor: pointer;
    transform: translateY(-4px);
}
.qp-settings-btncard:active {
    opacity: 0.6;
}
.qp-settings-btncard .el-card__body {
    box-sizing: border-box;
    height: 100%;
}
.qp-settings-btncard-wrapper {
    box-sizing: border-box;
    color: var(--qp-secondary);
    font-size: 14px;
    line-height: 120%;
    display: flex;
    height: 100%;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 12px 0;
}
.qp-settings-btncard .el-icon {
    margin: 0 0 12px;
}
.qp-settings-btncard p {
    padding: 0;
    margin: 0;
}
.qp-settings-btncard-title {
    color: var(--qp-card-color);
    font-size: 16px;
    line-height: 120%;
    transition: color 0.3s;
}
.qp-settings-btncard:hover .qp-settings-btncard-title {
    color: var(--qp-primary);
}
.qp-settings-btncard-caption {
    font-size: 14px;
    line-height: 120%;
}
</style>
