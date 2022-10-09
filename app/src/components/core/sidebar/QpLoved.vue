<script setup>

    const listFeatures = []

</script>

<template>
    <li v-if="listFeatures.length" class="qp-sidebar-nav-list-item">
        <el-icon size="large">
            <i class="mdi mdi-heart-outline"></i>
        </el-icon>
    </li>
    <li v-for="(item, n) in listFeatures" :key="`loved-${n}`" class="qp-sidebar-nav-list-item">
        <el-tooltip placement="left" content="Le monde perdu de Rhansidor">
            <el-button size="large" circle>
                <el-avatar :src="''">
                    <span v-text="item"></span>
                </el-avatar>
            </el-button>
        </el-tooltip>
    </li>
</template>