<script setup lang="ts">
import { computed, onMounted, useSlots } from "vue";
import { storeToRefs } from "pinia";
import { storeApp } from "../plugins/store";

const slots = useSlots()
const props = defineProps({
    sidenavTitle: {
        type: String,
        required: false
    },
    sideviewTitle: {
        type: String,
        required: false
    }
})

const useStoreApp = storeApp()
const { isSidenavShow, isSideviewShow } = storeToRefs(useStoreApp)
const { toggleSidenavShow, toggleSideviewShow, updateMainviewWidth } = useStoreApp

const mainClasses = computed(() => {
    if ("sidenav" in slots && "sideview" in slots && isSidenavShow.value && isSideviewShow.value) {
        return "qp-bothside-show"
    } else if ("sidenav" in slots && isSidenavShow.value) {
        return "qp-sidenav-show"
    } else if ("sideview" in slots && isSideviewShow.value) {
        return "qp-sideview-show"
    }
    return ""
})

onMounted(() => {
    const ElQpMainview = document.getElementById("qp-mainview")
    if (ElQpMainview) {
        new ResizeObserver((entries) => {
            updateMainviewWidth(entries[0].contentRect.width)
        }).observe(ElQpMainview)
    }
})
</script>

<template>
    <main :class="mainClasses">
        <div v-if="'sidenav' in slots" id="qp-sidenav">
            <div id="qp-sidenav-toggle-open">
                <el-button @click="toggleSidenavShow()">
                    <el-icon class="mdi mdi-arrow-collapse-right" />
                </el-button>
            </div>
            <el-scrollbar v-if="isSidenavShow" height="100%">
                <div id="qp-sidenav-toggle">
                    <el-button @click="toggleSidenavShow()">
                        <el-icon class="mdi mdi-arrow-collapse-left" />
                    </el-button>
                </div>
                <div v-if="props.sidenavTitle" id="qp-sidenav-header">
                    <span v-text="props.sidenavTitle"></span>
                </div>
                <div id="qp-sidenav-wrapper">
                    <slot name="sidenav"></slot>
                </div>
            </el-scrollbar>
        </div>
        <div id="qp-mainview">
            <el-scrollbar height="100%">
                <slot></slot>
            </el-scrollbar>
        </div>
        <div v-if="'sideview' in slots" id="qp-sideview">
            <div id="qp-sideview-toggle-open">
                <el-button @click="toggleSideviewShow()">
                    <el-icon class="mdi mdi-arrow-collapse-left" />
                </el-button>
            </div>
            <el-scrollbar v-if="isSideviewShow" height="100%">
                <div id="qp-sideview-toggle">
                    <el-button @click="toggleSideviewShow()">
                        <el-icon class="mdi mdi-arrow-collapse-right" />
                    </el-button>
                </div>
                <div v-if="props.sideviewTitle" id="qp-sideview-header">
                    <span v-text="props.sideviewTitle"></span>
                </div>
                <div id="qp-sideview-wrapper">
                    <slot name="sideview"></slot>
                </div>
            </el-scrollbar>
        </div>
    </main>
</template>

<style scoped>
#qp-main main {
    display: grid;
    grid-template-columns: 0 auto 0;
    width: 100%;
    height: 100%;
    position: relative;
}

#qp-main main.qp-bothside-show {
    grid-template-columns: 300px auto 300px;
}

#qp-main main.qp-sidenav-show {
    grid-template-columns: 300px auto 0;
}

#qp-main main.qp-sideview-show {
    grid-template-columns: 0 auto 300px;
}

/* ===---=== */
#qp-sidenav-toggle,
#qp-sideview-toggle {
    position: absolute;
    top: 24px;
    right: 0;
}

#qp-sidenav-toggle .el-button,
#qp-sideview-toggle .el-button,
#qp-sidenav-toggle-open .el-button,
#qp-sideview-toggle-open .el-button {
    background-color: transparent;
    border-color: transparent;
    color: #6e6f6e;
}

#qp-sidenav-toggle .el-button:hover,
#qp-sideview-toggle .el-button:hover,
#qp-sidenav-toggle-open .el-button:hover,
#qp-sideview-toggle-open .el-button:hover {
    color: var(--qp-primary);
}

#qp-sidenav-header,
#qp-sideview-header {
    font-size: 24px;
    line-height: 120%;
    padding: 24px 48px 12px 24px;
}

#qp-sidenav-wrapper,
#qp-sideview-wrapper {
    padding: 24px;
}

/* ===---=== */
#qp-sidenav {
    background-color: var(--qp-sidenav-bg);
    grid-column: 1 / 2;
    grid-row: 1 / 2;
    width: 0;
    height: calc(100vh - 49px);
    position: relative;
}

#qp-sidenav-toggle-open {
    position: absolute;
    top: -40px;
    left: 100%;
    z-index: 4;
}

#qp-main main.qp-bothside-show #qp-sidenav,
#qp-main main.qp-sidenav-show #qp-sidenav {
    width: auto;
}

#qp-main main.qp-bothside-show #qp-sidenav #qp-sidenav-toggle-open,
#qp-main main.qp-sidenav-show #qp-sidenav #qp-sidenav-toggle-open {
    display: none;
}

/* ===---=== */
#qp-mainview {
    grid-column: 2 / 3;
    grid-row: 1 / 2;
    height: calc(100vh - 49px);
}

/* ===---=== */
#qp-sideview {
    background-color: var(--qp-sideview-bg);
    grid-column: 3 / 4;
    grid-row: 1 / 2;
    width: 0;
    height: calc(100vh - 49px);
    position: relative;
}

#qp-sideview-toggle-open {
    position: absolute;
    top: 24px;
    right: 100%;
    z-index: 4;
}

#qp-main main.qp-bothside-show #qp-sideview,
#qp-main main.qp-sideview-show #qp-sideview {
    width: auto;
}

#qp-main main.qp-bothside-show #qp-sideview #qp-sideview-toggle-open,
#qp-main main.qp-sideview-show #qp-sideview #qp-sideview-toggle-open {
    display: none;
}

@media (max-width: 1199px) {
    #qp-main main {
        grid-template-columns: auto !important;
    }

    #qp-main main.qp-bothside-show #qp-sidenav,
    #qp-main main.qp-sidenav-show #qp-sidenav {
        box-shadow: -2px 0 2px rgba(0, 0, 0, 0.1);
        width: calc(100vw - 128px);
        max-width: 260px;
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        z-index: 2;
    }

    #qp-mainview {
        grid-column: 1 / 2 !important;
    }

    #qp-main main.qp-bothside-show #qp-sideview,
    #qp-main main.qp-sideview-show #qp-sideview {
        box-shadow: -2px 0 2px rgba(0, 0, 0, 0.1);
        width: calc(100vw - 128px);
        max-width: 260px;
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        z-index: 1;
    }
}
</style>
