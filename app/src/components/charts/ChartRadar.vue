<script setup lang="ts">
import { computed, onMounted, ref } from "vue";

const props = defineProps({
    levels: {
        type: Number,
        default: 6
    },
    data: {
        type: Array as () => Array<any>,
        default: () => []
    }
})

const chart = ref()
const levels = computed(() => {
    return props.levels + 1
})
const radians = computed(() => {
    return props.data.length
})

const setChart = () => {
    let s = chart.value.clientWidth
    var ctx = chart.value.getContext("2d");
    ctx.canvas.width = s
    ctx.canvas.height = s

    // radians
    for (let i = 0; i <= levels.value; i++) {
        let r = ((s/2) / levels.value) * i
        ctx.beginPath();
        ctx.moveTo((s/2 + (r * Math.cos((radians.value - 2) * 2 * Math.PI / radians.value))), (s/2 + (r * Math.sin((radians.value - 2) * 2 * Math.PI / radians.value))));
        for (let dot = 0; dot <= radians.value; dot++) {
            let point = dot + (radians.value - 2)
            let x = (s/2 + (r * Math.cos(point * 2 * Math.PI / radians.value)))
            let y = (s/2 + (r * Math.sin(point * 2 * Math.PI / radians.value)))
            ctx.lineTo(x, y);
            if (i == levels.value && dot < radians.value) {
                ctx.fillStyle = "#666";
                if (x > s/2 && y > s/3 && y < s/3 * 2) {
                    ctx.textAlign = "right";
                } else if (x < s/2 && y > s/3 && y < s/3 * 2) {
                    ctx.textAlign = "left";
                } else {
                    ctx.textAlign = "center";
                }
                ctx.fillText(props.data[dot][0], x, y);
            }
        }
        ctx.strokeStyle = "rgba(255, 255, 255, 0.08)";
        ctx.stroke();
    }

    // divider
    for (let dot = 0; dot <= radians.value; dot++) {
        ctx.beginPath();
        ctx.moveTo((s/2 + (s/2 * Math.cos(dot * 2 * Math.PI / radians.value))), (s/2 + (s/2 * Math.sin(dot * 2 * Math.PI / radians.value))));
        ctx.lineTo(s/2, s/2);
        ctx.strokeStyle = "rgba(255, 255, 255, 0.04)";
        ctx.stroke();
    }

    // filled-shape
    ctx.beginPath();
    for (let ps = 0; ps < radians.value; ps++) {
        let data = props.data[ps][1]
        let value = ((s/2) / levels.value) * data
        let point = ps + (radians.value - 2)
        let x = (s/2 + (value * Math.cos(point * 2 * Math.PI / radians.value)))
        let y = (s/2 + (value * Math.sin(point * 2 * Math.PI / radians.value)))
        if (ps <= 0) {
            ctx.moveTo(x, y);
        }
        ctx.lineTo(x, y);
        if (ps == radians.value - 1) {
            data = props.data[0][1]
            value = ((s/2) / levels.value) * data
            point = (radians.value - 2)
            x = (s/2 + (value * Math.cos(point * 2 * Math.PI / radians.value)))
            y = (s/2 + (value * Math.sin(point * 2 * Math.PI / radians.value)))
            ctx.lineTo(x, y);
        }
    }
    ctx.strokeStyle = "rgba(137, 164, 17, 0.8)";
    ctx.lineWidth = 2;
    ctx.fillStyle = "rgba(137, 164, 17, 0.2)";
    ctx.fill();
    ctx.stroke();
}

onMounted(() => {
    setChart()
})
</script>

<template>
    <canvas ref="chart" width="800" height="800" style="width:100%;max-width:200px;"></canvas>
</template>
