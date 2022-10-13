<script setup lang="ts">
import type { UploadRawFile, UploadInstance, UploadProps, FormInstance, FormRules } from "element-plus";
import type { ProjectsCreateForm } from "../../types/projects";
import { computed, reactive, ref } from "vue";
import { storeToRefs } from "pinia";
import { useI18n } from "vue-i18n";
import { useRouter } from "vue-router";
import { ElMessage } from "element-plus";
import { API, HEADERS } from "../../plugins/store/index";
import { storeUser } from "../../plugins/store";

const { t } = useI18n()

const router = useRouter()

const useStoreUser = storeUser()
const { rat, lang } = storeToRefs(useStoreUser)
const { updateUser } = useStoreUser

const props = defineProps(["show"])
const emits = defineEmits(["close"])

const isLoading = ref<boolean>(false)
const hasError = ref<string|null>(null)
const refProject = ref<FormInstance>()
const refProjectIcon = ref<UploadInstance>()
const formProject = reactive<ProjectsCreateForm>({
    name: "",
    caption: "",
    description: "",
    primary_color: "#33391d",
    secondary_color: "#ffffff",
    icon: null,
    icon_file: null
})

const rulesProject = reactive<FormRules>({
    name: [
        { required: true, message: t("Thisfieldisrequired"), trigger: "blur" },
        { min: 1, max: 32, message: t("LengthshouldbebetweenXandX", [1, 32]), trigger: "blur" }
    ],
    caption: [
        { min: 0, max: 120, message: t("LengthshouldbebetweenXandX", [0, 120]), trigger: "blur" }
    ]
})

const initial = computed(() => {
    if (formProject.name) {
        let values = formProject.name.split(" ").map((k) => k[0])
        let initials = values.slice(0,2).join("").toUpperCase()
        return initials
    } else {
        return ""
    }
})

const doChangeIcon: UploadProps["onChange"] = (event) => {
    if (event && event.raw) {
        if (!["image/jpeg","image/png"].includes(event.raw.type)) {
            ElMessage.error(t("FileFormatMustBeJPGORPNG"))
            return false
        } else if (event.raw.size / 1024 > 50) {
            ElMessage.error(t("FileSizeCanNotExceed", ["50ko"]))
            return false
        }
        formProject.icon_file = URL.createObjectURL(event.raw)
        formProject.icon = event.raw
    } else { return false}
    return true
}

const doExceedIcon: UploadProps["onExceed"] = (files) => {
    const file = files[0] as UploadRawFile
    refProjectIcon.value?.clearFiles()
    refProjectIcon.value?.handleStart(file)
}

const doSubmitProject = async () => {
    isLoading.value = true
    hasError.value = null
    await refProject.value?.validate((valid) => {
        if (valid) {
            doCreateProject()
        } else {
            isLoading.value = false
        }
    })
}

const doCreateProject = async () => {
    isLoading.value = true
    hasError.value = null
    // ===---
    let data = new FormData()
    data.append("name", formProject.name)
    data.append("caption", formProject.caption)
    data.append("description", formProject.description)
    data.append("primary_color", formProject.primary_color)
    if (formProject.icon) data.append("icon", formProject.icon)
    // ===---
    let f = await fetch(`${API}/projects/create/`, {
        method: "POST",
        headers: HEADERS(rat.value, lang.value),
        body: data
    })
    if (f.status === 201) {
        isLoading.value = false
        updateUser()
        goTo({name: "Projects"})
        doClose()
    } else if (f.status === 429) {
        let r = await f.json()
        hasError.value = r.msg
        isLoading.value = false
    } else {
        hasError.value = t("AnErrorOccurred")
        isLoading.value = false
    }
}

const doClose = () => {
    isLoading.value = false
    hasError.value = null
    refProject.value?.resetFields()
    emits("close")
}

const goTo = (obj: any) => {
    router.push(obj)
}
</script>

<template>
    <el-dialog v-model="show" :title="$t('CreateNewProject')" @close="doClose()" class="qp-dialog-projects-create">
        <el-form ref="refProject" :model="formProject" :rules="rulesProject" status-icon class="qp-form-projects-create">
            <el-row>
                <el-col :span="24" :md="12" :lg="14">
                    <el-form-item prop="name">
                        <el-input v-model="formProject.name" :placeholder="$t('Name')" />
                    </el-form-item>
                    <el-form-item prop="caption">
                        <el-input v-model="formProject.caption" :placeholder="$t('Caption')" />
                    </el-form-item>
                    <el-form-item prop="description">
                        <el-input v-model="formProject.description" :placeholder="$t('Description')" type="textarea" :rows="6" />
                    </el-form-item>
                </el-col>
                <el-col :span="24" :md="12" :lg="10">
                    <el-form-item prop="icon_file" class="qp-form-projects-create-icon">
                        <el-avatar :src="formProject.icon_file" :size="120" :style="`background-color:${formProject.icon_file ? 'transparent' : formProject.primary_color};color:${formProject.secondary_color};`">
                            <span v-text="initial"></span>
                        </el-avatar>
                    </el-form-item>
                    <el-form-item :label="$t('PrimaryColour')" prop="primary_color">
                        <el-color-picker v-model="formProject.primary_color" />
                    </el-form-item>
                    <el-form-item class="qp-justify-content-center" prop="icon">
                        <el-upload ref="refProjectIcon" action="#" accept="image/jpeg,image/png" :auto-upload="false" :show-file-list="false" :limit="1" :on-change="doChangeIcon" :on-exceed="doExceedIcon">
                            <el-button>
                                <span v-text="$t('UploadAnIcon')"></span>
                            </el-button>
                        </el-upload>
                    </el-form-item>
                </el-col>
                <el-col v-if="hasError" :span="24">
                    <el-alert type="error" show-icon :closable="false">
                        <p v-html="hasError"></p>
                    </el-alert>
                </el-col>
            </el-row>
        </el-form>
        <template #footer>
            <span class="dialog-footer">
                <el-button :disabled="isLoading" @click="doClose()">
                    <span v-text="$t('Cancel')"></span>
                </el-button>
                <el-button type="primary" :loading="isLoading" @click="doSubmitProject()">
                    <span v-text="$t('Create')"></span>
                </el-button>
            </span>
        </template>
    </el-dialog>
</template>

<style>
.qp-dialog-projects-create {
    --el-dialog-width: 90%;
    max-width: 700px;
}
.qp-form-projects-create-icon {
    text-align: center;
    margin: 0 0 32px;
}
.qp-form-projects-create-icon > .el-form-item__content {
    justify-content: center;
}
.qp-form-projects-create-icon .el-avatar {
    color: #fff;
    font-size: 32px;
    line-height: 100%;
    text-align: center;
}
.qp-form-projects-create .el-color-picker,
.qp-form-projects-create .el-color-picker__trigger {
    width: 100%;
}
.qp-justify-content-center > .el-form-item__content {
    justify-content: center;
}
</style>
