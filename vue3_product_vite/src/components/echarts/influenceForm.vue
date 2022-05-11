<template>
<div class="influence" ref="influence"></div>
</template>

<script lang="ts" setup>
import {onMounted, reactive, ref} from 'vue'

import * as echarts from 'echarts'

const influence = ref<any>(null)
const option = reactive({
  tooltip: {
    trigger: "item",
    formatter: "{a} <br/>{b}: {c} ({d}%)",
  },
  legend: {
    orient: "vertical",
    x: "left",
    data: [
      "直达",
      "营销广告",
      "搜索引擎",
      "其他",
    ],
  },
  series: [
    {
      name: "访问来源",
      type: "pie",
      selectedMode: "single",
      radius: [0, "30%"],

      label: {
        position: "left",
      },
      labelLine: {
        show: false,
      },
      data: [
        { value: 335, name: "直达", selected: true },
        { value: 679, name: "营销广告" },
        { value: 1548, name: "搜索引擎" },
      ],
    },
    {
      name: "访问来源",
      type: "pie",
      radius: ["40%", "55%"],

      data: [
        { value: 335, name: "直达" },
        { value: 1048, name: "百度" },
        { value: 251, name: "谷歌" },
        { value: 147, name: "必应" },
        { value: 102, name: "其他" },
      ],
    },
  ],
})
onMounted(() => {
    if (influence.value instanceof HTMLElement) {
        let influenceChart = echarts.init(influence.value)
        influenceChart.setOption(option)
    }
})
</script>
<style scoped>
.influence {
    height: 60vh;
}
</style>