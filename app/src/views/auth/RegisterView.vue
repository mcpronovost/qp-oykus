<script setup>
import { h, reactive, ref } from "vue";
import { useI18n } from "vue-i18n";
import { API } from "@/plugins/store/index";
import { ElMessageBox } from "element-plus";
import { EditPen, Lock, Message, User } from "@element-plus/icons-vue";
import router from "@/plugins/router";

const { t } = useI18n()

const isLoadingRegister = ref(false)
const hasErrorRegister = ref()
const showRules = ref(false)
const showUsePolicies = ref(false)
const showPrivacyPolicies = ref(false)
const refRegister = ref()

const formRegister = reactive({
    username: "",
    email: "",
    name: "",
    password: "",
    password_confirm: ""
})

const ruleValidatorUsername = (rule, value, callback) => {
    const regstr = /^[A-Za-z0-9_-]+$/
    if (value === "") {
        callback(new Error(t("Thisfieldisrequired")))
    } else if (!value.match(regstr)) {
        callback(new Error(t("Mustonlycontainlettersnumbersandsomecharacters")))
    } else {
        callback()
    }
}

const ruleValidatorEmail = (rule, value, callback) => {
    const regstr = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/
    if (value === "") {
        callback(new Error(t("Thisfieldisrequired")))
    } else if (!value.match(regstr)) {
        callback(new Error(t("Thisemailisinvalid")))
    } else {
        callback()
    }
}

const ruleValidatorName = (rule, value, callback) => {
    const regstr = /^[A-Za-z- ]+$/
    if (value === "") {
        callback(new Error(t("Thisfieldisrequired")))
    } else if (!value.match(regstr)) {
        callback(new Error(t("Mustonlycontainlettersspaceandsomecharacters")))
    } else {
        callback()
    }
}

const ruleValidatorConfirm = (rule, value, callback) => {
    if (value === "") {
        callback(new Error(t("Thisfieldisrequired")))
    } else if (value !== formRegister.password) {
        callback(new Error(t("Thepasswordconfirmationdoesntmatch")))
    } else {
        callback()
    }
}

const rulesRegister = reactive({
    username: [
        { required: true, message: t("Thisfieldisrequired"), trigger: "blur" },
        { min: 5, max: 150, message: t("LengthshouldbebetweenXandX", [5, 150]), trigger: "blur" },
        { validator: ruleValidatorUsername, trigger: "blur"}
    ],
    email: [
        { required: true, message: t("Thisfieldisrequired"), trigger: "blur" },
        { min: 8, max: 254, message: t("LengthshouldbebetweenXandX", [8, 254]), trigger: "blur" },
        { validator: ruleValidatorEmail, trigger: "blur" }
    ],
    name: [
        { required: true, message: t("Thisfieldisrequired"), trigger: "blur" },
        { min: 2, max: 32, message: t("LengthshouldbebetweenXandX", [2, 32]), trigger: "blur" },
        { validator: ruleValidatorName, trigger: "blur"}
    ],
    password: [
        { required: true, message: t("Thisfieldisrequired"), trigger: "blur" },
        { min: 8, max: 254, message: t("LengthshouldbebetweenXandX", [6, 254]), trigger: "blur" }
    ],
    password_confirm: [
        { required: true, message: t("Thisfieldisrequired"), trigger: "blur" },
        { min: 8, max: 254, message: t("LengthshouldbebetweenXandX", [6, 254]), trigger: "blur" },
        { validator: ruleValidatorConfirm, trigger: "blur" }
    ]
})

const doSubmitRegister = async () => {
    isLoadingRegister.value = true
    hasErrorRegister.value = null
    await refRegister.value.validate((valid) => {
        if (valid) {
            ElMessageBox.confirm(
                h("div", null, [
                    h("p", null, t("Byclickingyouacceptrules")),
                    h("div", {class: "qp-center"}, [
                        h("button", {class: "el-button is-text", onClick: () => {
                            showRules.value = true
                        }}, t("ReadTheRules"))
                    ]),
                    h("div", {class: "qp-center"}, [
                        h("button", {class: "el-button is-text", onClick: () => {
                            showUsePolicies.value = true
                        }}, t("ReadUsePolicies"))
                    ]),
                    h("div", {class: "qp-center"}, [
                        h("button", {class: "el-button is-text", onClick: () => {
                            showPrivacyPolicies.value = true
                        }}, t("ReadPrivacyPolicies"))
                    ])
                ]),
                t("Register"),
                {
                    confirmButtonText: t("IAcceptTheRules"),
                    cancelButtonText: t("Cancel"),
                    autofocus: false,
                    closeOnClickModal: false,
                    closeOnPressEscape: false,
                    closeOnHashChange: false
                }
            ).then(() => {
                doRegister()
            }).catch(() => {
                isLoadingRegister.value = false
            })
        } else {
            isLoadingRegister.value = false
        }
    })
}

const doRegister = async () => {
    isLoadingRegister.value = true
    hasErrorRegister.value = null
    // ===---
    let data = new FormData()
    data.append("username", formRegister.username.trim())
    data.append("email", formRegister.email.trim())
    data.append("name", formRegister.name.trim())
    data.append("password", formRegister.password)
    // ===---
    let f = await fetch(`${API}/register/`, {
        method: "POST",
        body: data
    })
    if (f.status === 200) {
        goTo({name: "AuthLogin"})
    } else if (f.status === 400) {
        hasErrorRegister.value = t("InvalidCredentials")
        isLoadingRegister.value = false
    } else {
        hasErrorRegister.value = t("AnErrorOccurred")
        isLoadingRegister.value = false
    }
}

const goTo = (obj) => {
    router.push(obj)
}
</script>

<template>
    <el-row id="qp-auth-register">
        <el-col>
            <el-card>
                <h1 v-text="$t('Register')"></h1>
                <el-form ref="refRegister" :model="formRegister" :rules="rulesRegister" label-position="top" status-icon>
                    <el-form-item prop="username">
                        <el-input v-model="formRegister.username" :placeholder="$t('Username')" :prefix-icon="User" />
                    </el-form-item>
                    <el-form-item prop="email">
                        <el-input v-model="formRegister.email" :placeholder="$t('Email')" :prefix-icon="Message" />
                    </el-form-item>
                    <el-form-item prop="name">
                        <el-input v-model="formRegister.name" :placeholder="$t('Name')" :prefix-icon="EditPen" />
                    </el-form-item>
                    <el-form-item prop="password">
                        <el-input v-model="formRegister.password" :placeholder="$t('Password')" :prefix-icon="Lock" type="password" />
                    </el-form-item>
                    <el-form-item prop="password_confirm">
                        <el-input v-model="formRegister.password_confirm" :placeholder="$t('PasswordConfirm')" :prefix-icon="Lock" type="password" />
                    </el-form-item>
                    <el-form-item v-if="hasErrorRegister">
                        <el-alert type="error" show-icon :closable="false">
                            <div v-html="hasErrorRegister"></div>
                        </el-alert>
                    </el-form-item>
                    <el-form-item class="qp-form-submit">
                        <el-button type="primary" :loading="isLoadingRegister" @click="doSubmitRegister()">
                            <span v-text="$t('RegisterMe')"></span>
                        </el-button>
                    </el-form-item>
                    <el-form-item class="qp-form-switchauth">
                        <el-button text size="small" :disabled="isLoadingRegister" @click="goTo({name:'AuthLogin'})">
                            <span v-text="$t('Alreadyhaveanaccount')"></span>
                        </el-button>
                    </el-form-item>
                </el-form>
            </el-card>
            <el-dialog v-model="showRules" :title="t('TheRules')">
                <el-scrollbar height="60vh">
                    <div>(en développement)</div>
                </el-scrollbar>
            </el-dialog>
            <el-dialog v-model="showUsePolicies" :title="t('UsePolicies')">
                <el-scrollbar height="60vh">
                    <div>(en développement)</div>
                </el-scrollbar>
            </el-dialog>
            <el-dialog v-model="showPrivacyPolicies" :title="t('PrivacyPolicies')">
                <el-scrollbar height="60vh">
                    <div>(en développement)</div>
                </el-scrollbar>
            </el-dialog>
        </el-col>
    </el-row>
</template>

<style scoped>
#qp-auth-register .el-card {
    border-bottom: 2px solid var(--qp-primary);
}
#qp-auth-register .el-form {
    width: 300px;
    padding: 32px 12px;
}
</style>
