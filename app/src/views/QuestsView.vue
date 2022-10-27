<script setup lang="ts">
import { ref } from "vue";

const isLoading = ref<boolean>(false)
const hasError = ref<string|null>(null)
</script>

<template>
    <qp-page>
        <template #sidenav>
            <div class="qp-center">
                <div>
                    <el-avatar :size="120" :style="`background-color:var(--qp-primary-dark-2);color:#fff;`">
                        <span>QS</span>
                    </el-avatar>
                </div>
                <div>
                    <span>Qamuy Sinen</span>
                </div>
                <div>
                    <span>Ladkani, Kshirsagar</span>
                </div>
                <div>
                    <span>Humaine, 32 ans</span>
                </div>
                <el-button size="small">
                    <span>Changer de personnage</span>
                </el-button>
            </div>
        </template>
        <div v-if="!isLoading && !hasError" class="qp-container">
            <qp-header :title="`Couper du bois`" :content="`Couper et débiter les grands chênes de la région pour en récupérer les ressources.`" />
            <el-row>
                <el-col :span="24" :md="16" :lg="18">
                    <el-card>
                        <el-row>
                            <el-col>
                                <h2>Récompenses</h2>
                            </el-col>
                            <el-col :span="4">
                                <span>20 exp</span>
                            </el-col>
                            <el-col :span="4">
                                <el-icon class="mdi mdi-rhombus-split-outline el-icon--left" />
                                <span>1 234</span>
                            </el-col>
                            <el-col :span="4">
                                <el-icon class="mdi mdi-orbit el-icon--left" />
                                <span>123</span>
                            </el-col>
                            <el-col :span="4">
                                <el-icon class="mdi mdi-diamond-stone el-icon--left" />
                                <span>12</span>
                            </el-col>
                            <el-col :span="4">
                                <el-icon class="mdi mdi-gold el-icon--left" />
                                <span>1</span>
                            </el-col>
                            <el-col>
                                <el-button size="large" />
                                <el-button size="large" />
                                <el-button size="large" />
                                <el-button size="large" />
                            </el-col>
                        </el-row>
                    </el-card>
                </el-col>
            </el-row>
        </div>
        <qp-notfound v-else-if="!isLoading" />
    </qp-page>
</template>
