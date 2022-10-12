<script setup>
import QpRegister from "@/views/auth/RegisterView.vue";
import QpLogin from "@/views/auth/LoginView.vue";
import QpLogout from "@/views/auth/LogoutView.vue";

</script>

<template>
    <qp-page>
        <div class="qp-container qp-centered">
            <QpRegister v-if="$route.name && $route.name == 'AuthRegister'" />
            <QpLogin v-else-if="$route.name && $route.name == 'AuthLogin'" />
            <QpLogout v-else-if="$route.name && $route.name == 'AuthLogout'" />
        </div>
    </qp-page>
</template>

<style>
.qp-form-submit {
    margin: 48px 0 0;
}
.qp-form-submit button {
    margin: 0 auto;
}
.qp-form-switchauth {
    margin: 12px 0 0;
}
.qp-form-switchauth button {
    margin: 0 auto;
}
</style>
