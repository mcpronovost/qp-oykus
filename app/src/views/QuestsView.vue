<script setup lang="ts">
import { ref } from "vue";

const isLoading = ref<boolean>(false)
const hasError = ref<string|null>(null)
</script>

<template>
    <qp-page>
        <div v-if="!isLoading && !hasError" class="qp-container">
        <qp-header :title="$t('Quests')" />
        <el-row>
            <el-col :span="24" :md="8" :lg="6" class="qp-center">
                <el-card>
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
                </el-card>
                <br />
                <el-button size="small">
                    <span>Changer de personnage</span>
                </el-button>
            </el-col>
            <el-col :span="24" :md="16" :lg="18">
                <el-card>
                    <h2>Couper du bois</h2>
                    <p>Lorem ipsum dolor sit amet.</p>
                    <div>
                        <el-progress color="var(--qp-primary-dark-2)" :percentage="33" :stroke-width="12" :show-text="false" />
                    </div>
                </el-card>
            </el-col>
        </el-row>
        </div>
        <qp-notfound v-else-if="!isLoading" />
    </qp-page>
</template>
