<script setup lang="ts">
import { ref } from "vue";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";
import { Bell, Message } from "@element-plus/icons-vue";
import { storeUser } from "../../plugins/store";
import { API, HEADERS } from "../../plugins/store/index";

const router = useRouter()

const useStoreUser = storeUser()
const { rat, username, name, avatar, notifications, lang } = storeToRefs(useStoreUser)
const { updateUser } = useStoreUser

const isLoadingNotifications = ref<boolean>(false)

const doNotificationSeen = async (id: number) => {
    isLoadingNotifications.value = true
    let f = await fetch(`${API}/notifications/${id}/seen/`, {
        method: "PATCH",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {updateUser()}
    isLoadingNotifications.value = false
}

const doNotificationAllSeen = async () => {
    isLoadingNotifications.value = true
    let f = await fetch(`${API}/notifications/seen/`, {
        method: "PATCH",
        headers: HEADERS(rat.value, lang.value)
    })
    if (f.status === 200) {updateUser()}
    isLoadingNotifications.value = false
}

const goTo = (obj: any) => {
    router.push(obj)
}
</script>

<template>
    <div id="qp-topbar">
        <div id="qp-topbar-left">
            <!---->
        </div>
        <div id="qp-topbar-center">
            <!---->
        </div>
        <div v-if="rat" id="qp-topbar-right">
            <div class="qp-topbar-item">
                <el-badge :value="0" :hidden="true">
                    <el-button :icon="Message" round disabled></el-button>
                </el-badge>
            </div>
            <div v-if="notifications" class="qp-topbar-item">
                <el-dropdown :hide-on-click="false" trigger="click" placement="bottom-end" @command="doNotificationSeen" popper-class="qp-topbar-popper qp-topbar-popper-notifications">
                    <el-badge :value="notifications.length" :hidden="notifications.length < 1">
                        <el-button :icon="Bell" round></el-button>
                    </el-badge>
                    <template #dropdown>
                        <el-dropdown-menu v-loading="isLoadingNotifications">
                            <el-row>
                                <el-col :span="12" class="qp-left">
                                    <span v-text="$t('Notifications')"></span>
                                </el-col>
                                <el-col :span="12" class="qp-right">
                                    <el-link v-if="notifications.length > 1" :underline="false" @click="doNotificationAllSeen()">
                                        <span v-text="$t('MarkAllAsRead')"></span>
                                    </el-link>
                                </el-col>
                            </el-row>
                            <el-scrollbar v-if="notifications.length" :max-height="210">
                                <el-dropdown-item v-for="(notification, n) in notifications" :key="`notification-${n}`" :command="notification.id">
                                    <el-alert :type="notification.has_type ? notification.has_type : 'info'" :closable="false">
                                        <div v-if="notification.initial || notification.has_type" class="qp-topbar-popper-notifications-icon">
                                            <el-avatar :src="notification.icon" :size="32" :style="`background-color:${notification.icon ? 'transparent' : notification.primary_color};color:#fff;`">
                                                <span v-if="notification.initial" v-text="notification.initial"></span>
                                                <el-icon v-else :class="`mdi ${
                                                    notification.has_type == 'success' ? 'mdi-check-circle-outline'
                                                    : notification.has_type == 'error' ? 'mdi-alert-circle-outline'
                                                    : 'mdi-bell'
                                                }`" :style="`color:var(--qp-${notification.has_type});`" />
                                            </el-avatar>
                                        </div>
                                        <div>
                                            <p v-text="notification.content"></p>
                                        </div>
                                    </el-alert>
                                </el-dropdown-item>
                            </el-scrollbar>
                            <el-row v-else>
                                <el-col class="qp-center">
                                    <el-card>
                                        <el-result :title="$t('NoNotificationYet')">
                                            <template #icon>
                                                <el-icon :size="48" class="mdi mdi-sleep" />
                                            </template>
                                        </el-result>
                                    </el-card>
                                </el-col>
                            </el-row>
                        </el-dropdown-menu>
                        <el-button v-if="false" text>
                            <span v-text="$t('ShowAllNotifications')"></span>
                        </el-button>
                    </template>
                </el-dropdown>
            </div>
            <div class="qp-topbar-item qp-player">
                <el-dropdown trigger="click" placement="bottom-end" popper-class="qp-topbar-popper" @command="goTo">
                    <el-avatar :src="avatar">
                        <span v-text="name?.charAt(0)"></span>
                    </el-avatar>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item class="qp-dropdown-text" disabled>
                                <div>
                                    <div v-text="$t('SignedInAs')"></div>
                                    <div v-text="username"></div>
                                </div>
                            </el-dropdown-item>
                            <el-divider />
                            <el-dropdown-item :command="{name:'Profile'}" :disabled="$route.name=='Profile'">
                                <span v-text="$t('MyProfile')"></span>
                            </el-dropdown-item>
                            <el-dropdown-item :command="{name:'Projects'}" :disabled="$route.name=='Projects'">
                                <span v-text="$t('MyProjects')"></span>
                            </el-dropdown-item>
                            <el-dropdown-item :command="{name:'Tasks'}" :disabled="$route.name=='Tasks'">
                                <span v-text="$t('MyTasks')"></span>
                            </el-dropdown-item>
                            <el-divider />
                            <el-dropdown-item :command="{name:'Settings'}" :disabled="$route.name=='Settings'">
                                <span v-text="$t('Settings')"></span>
                            </el-dropdown-item>
                            <el-divider />
                            <el-dropdown-item :command="{name:'AuthLogout'}" :disabled="$route.name=='AuthLogout'">
                                <span v-text="$t('Logout')"></span>
                            </el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
            </div>
        </div>
        <div v-else id="qp-topbar-right">
            <div class="qp-topbar-item">
                <el-button @click="goTo({name:'AuthLogin'})">
                    <el-icon class="mdi mdi-login-variant el-icon--left" />
                    <span v-text="$t('Login')"></span>
                </el-button>
            </div>
            <div class="qp-topbar-item">
                <el-button @click="goTo({name:'AuthRegister'})">
                    <el-icon class="mdi mdi-card-account-details-outline el-icon--left" />
                    <span v-text="$t('Register')"></span>
                </el-button>
            </div>
        </div>
    </div>
</template>

<style scoped>
    #qp-topbar {
        background-color: var(--qp-topbar-bg);
        font-size: 0;
        line-height: 0;
        display: flex;
        align-items: center;
        justify-content: space-between;
        grid-column: 2 / 4;
        grid-row: 2 / 3;
    }
    /* ===--- RIGHT ---=== */
    #qp-topbar-right {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        padding: 0;
    }
    .qp-topbar-item {
        padding: 0 16px;
    }
    .qp-topbar-item .el-avatar {
        --el-avatar-size: 32px;
        background-color: var(--qp-primary);
        color: #fff;
        opacity: 0.8;
        transition: opacity 0.3s;
    }
    .qp-topbar-item .el-avatar:hover {
        opacity: 1;
    }
    .qp-topbar-item .el-badge {
        --el-bg-color: var(--qp-topbar-bg);
        --el-badge-font-size: 9px;
        --el-badge-size: 14px;
        --el-badge-padding: 4px;
    }
    .qp-topbar-item .el-button {
        background-color: transparent!important;
        border-color: transparent!important;
        font-size: 16px;
        height: auto;
        padding: 2px 4px;
    }
    .qp-topbar-item .el-button.is-round {
        font-size: 20px;
    }
    .qp-topbar-item .el-dropdown .el-tooltip__trigger {
        cursor: pointer;
    }
</style>
