<script setup lang="ts">
import { qpdate, qpslug } from "@mcpronovost/qpfilters";
const props = defineProps({
    rpg: {
        type: Object,
        required: true
    },
    topic: {
        type: Object,
        required: true
    }
})
</script>

<template>
    <el-card v-if="props.rpg && props.topic" :id="`rpg-${props.rpg.slug}-forum-topic-${props.topic.id}`" class="rpg-forum-section-topic">
        <div class="rpg-forum-section-topic-banner">
            <div class="rpg-forum-section-topic-banner-author">
                <el-image :src="props.topic.author?.avatar" fit="cover">
                    <template #error><span></span></template>
                </el-image>
            </div>
            <div v-if="props.topic.author" class="rpg-forum-section-topic-banner-lastauthor">
                <el-avatar :src="props.topic.author.avatar" :size="110" :style="`background-color:${props.rpg.primary_color};color:#fff;`">
                    <span v-text="props.topic.author.initial"></span>
                </el-avatar>
            </div>
        </div>
        <div class="rpg-forum-section-topic-title" @click="$router.push({path:`/rpg/${props.rpg.slug}/t${props.topic.id}-${qpslug(props.topic.title)}`})">
            <h3>
                <span v-text="props.topic.title"></span>
            </h3>
        </div>
        <div class="rpg-forum-section-topic-footer">
            <div class="rpg-forum-section-topic-date">
                <el-icon class="mdi mdi-clock-outline el-icon--left" />
                <span v-text="qpdate(props.topic.created_at)"></span>
            </div>
            <div class="rpg-forum-section-topic-counts">
                <span v-text="0"></span>
                <el-icon class="mdi mdi-message-text-outline el-icon--right" />
            </div>
        </div>
    </el-card>
</template>