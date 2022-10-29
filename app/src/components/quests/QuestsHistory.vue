<script setup lang="ts">
import { ref } from "vue";

const props = defineProps({
    logs: {
        type: Array as () => Array<any>,
        default: () => []
    }
})

const listHistory = ref<Array<any>>([
    {
        "character": "Tyryn",
        "start": "2022-10-29 06:00:00",
        "end": "2022-10-28 06:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    },
    {
        "character": "Halim Seðem Sádh Prayishman",
        "start": "2022-10-29 08:00:00",
        "end": "2022-10-30 10:00:30"
    },
    {
        "character": "Abe L. Ley",
        "start": "2022-10-28 10:00:00",
        "end": "2022-10-28 10:00:30"
    }
])

</script>

<template>
    <el-timeline class="qp-quests-history">
        <el-timeline-item
            v-for="(log, n) in props.logs"
            :key="`history-${n}`"
            :timestamp="new Date(log.end) > new Date() ? $f.qpDate(new Date(log.start)) : $f.qpDate(new Date(log.end))"
            :color="!log.is_completed ? '' : log.is_success ? 'var(--qp-primary-dark-2)' : 'var(--qp-error-dark-2)'"
            size="large"
        >
            <div v-text="log.character.name"></div>
        </el-timeline-item>
    </el-timeline>
</template>

<style scoped>
.qp-quests-history {
    font-size: 14px;
    line-height: 120%;
}
</style>
