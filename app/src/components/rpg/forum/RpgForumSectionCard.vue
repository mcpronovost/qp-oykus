<script setup lang="ts">
const props = defineProps({
    rpg: {
        type: Object,
        required: true
    },
    section: {
        type: Object,
        required: true
    }
})
</script>

<template>
    <el-card v-if="props.rpg && props.section" :id="`rpg-${props.rpg.slug}-forum-section-${props.section.id}`" class="rpg-forum-category-section">
        <div class="rpg-forum-category-section-title" @click="$router.push({path:`/rpg/${props.rpg.slug}/s${props.section.id}-${$f.qpSlugify(props.section.title)}`})">
            <h3>
                <span v-text="props.section.title"></span>
            </h3>
        </div>
        <div class="rpg-forum-category-section-lastauthor">
            <el-avatar v-if="props.section.last_message" :src="props.section.last_message.author.avatar" :size="120" :style="`background-color:${props.section.last_message.author.avatar ? 'transparent' : rpg.primary_color};color:#fff;`">
                <span v-text="props.section.last_message.author.initial"></span>
            </el-avatar>
            <div v-if="props.section.last_message" class="rpg-forum-category-section-track"></div>
        </div>
        <div v-if="props.section.last_message" class="rpg-forum-category-section-lastmessage">
            <div class="rpg-forum-category-section-lastmessage-title">
                <span v-text="props.section.last_message.topic.title"></span>
            </div>
            <div class="rpg-forum-category-section-lastmessage-date">
                <span v-text="$f.qpDate(props.section.last_message.created_at)"></span>
            </div>
        </div>
    </el-card>
</template>
