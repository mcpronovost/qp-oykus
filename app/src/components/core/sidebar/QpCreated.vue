<script setup>

    const listFeatures = [1, 2]

</script>

<template>
    <li v-for="(item, n) in listFeatures" :key="`created-${n}`" class="qp-sidebar-nav-list-item">
        <el-tooltip placement="left" content="Le monde perdu de Rhansidor">
            <el-button size="large" circle>
                <el-avatar :src="''">
                    <span v-text="item"></span>
                </el-avatar>
            </el-button>
        </el-tooltip>
    </li>
</template>