<script setup lang="ts">
import { qpcode } from "@mcpronovost/qpfilters";
const props = defineProps({
    rpg: {
        type: Object,
        required: true
    },
    message: {
        type: Object,
        required: true
    }
})
</script>

<template>
    <el-card v-if="props.rpg && props.message" :id="`rpg-${props.rpg.slug}-forum-message-${props.message.id}`" class="rpg-forum-topic-message">
        <div class="rpg-forum-topic-message-banner">
            <div class="rpg-forum-topic-message-author-avatar">
                <el-avatar :src="props.message.author?.avatar" :size="180" :style="`background-color:${props.rpg.primary_color};color:#fff;`">
                    <span v-text="props.message.author?.initial"></span>
                </el-avatar>
            </div>
            <div class="rpg-forum-topic-message-author-name">
                <h3 v-text="props.message.author?.name"></h3>
            </div>
        </div>
        <div class="rpg-forum-topic-message-content">
            <div class="rpg-forum-topic-message-content-wrapper">
                <div class="rpg-forum-topic-message-content-text">
                    <div v-html="qpcode(props.message.content)"></div>
                </div>
            </div>
        </div>
    </el-card>
</template>