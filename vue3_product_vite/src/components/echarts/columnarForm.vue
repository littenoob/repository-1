<template>
    <div class="columnaCharts" ref="columnar"></div>
</template>
<script lang="ts" setup>
import { onMounted, reactive, ref } from 'vue'

import * as echarts from 'echarts'

const columnar = ref<any>(null)
let colorList = ["#f36c6c", "#e6cf4e", "#20d180", "#0093ff"];
let datas = [
    {
        value: 36,
        name: "汇率",
    },
    {
        value: 54,
        name: "行情",
    },
    {
        value: 29,
        name: "CPU",
    },
    {
        value: 25,
        name: "屏幕",
    },
    {
        value: 85,
        name: "其他",
    },
];
let maxArr = new Array(datas.length).fill(100);
const option = {
    tooltip: {
        trigger: "axis",
        axisPointer: {
            type: "shadow",
        },
    },
    legend: {
        show: false,
    },
    grid: {
        left: 0,
        right: 0,
        containLabel: true,
    },
    xAxis: {
        show: false,
        type: "value",
    },
    yAxis: [
        {
            type: "category",
            inverse: true,
            axisLine: {
                show: false,
            },
            axisTick: {
                show: false,
            },
            axisPointer: {
                label: {
                    show: true,
                    margin: 30,
                },
            },
            data: datas.map((item) => item.name),
            axisLabel: {
                margin: 100,
                fontSize: 14,
                align: "left",
                color: "#333",
                rich: {
                    a1: {
                        color: "#fff",
                        backgroundColor: colorList[0],
                        width: 30,
                        height: 30,
                        align: "center",
                        borderRadius: 2,
                    },
                    a2: {
                        color: "#fff",
                        backgroundColor: colorList[1],
                        width: 30,
                        height: 30,
                        align: "center",
                        borderRadius: 2,
                    },
                    a3: {
                        color: "#fff",
                        backgroundColor: colorList[2],
                        width: 30,
                        height: 30,
                        align: "center",
                        borderRadius: 2,
                    },
                    b: {
                        color: "#fff",
                        backgroundColor: colorList[3],
                        width: 30,
                        height: 30,
                        align: "center",
                        borderRadius: 2,
                    },
                },
                formatter: function (params:any) {
                    var index = datas.map((item) => item.name).indexOf(params);
                    index = index + 1;
                    if (index - 1 < 3) {
                        return ["{a" + index + "|" + index + "}" + "  " + params].join(
                            "\n"
                        );
                    } else {
                        return ["{b|" + index + "}" + "  " + params].join("\n");
                    }
                },
            },
        },
        {
            type: "category",
            inverse: true,
            axisTick: "none",
            axisLine: "none",
            show: true,
            data: datas.map((item) => item.value),
            axisLabel: {
                show: true,
                fontSize: 14,
                color: "#333",
                formatter: "{value}%",
            },
        },
    ],
    series: [
        {
            z: 2,
            name: "value",
            type: "bar",
            barWidth: 20,
            zlevel: 1,
            data: datas.map((item, i) => {
                let itemStyle = {
                    color: i > 3 ? colorList[3] : colorList[i],
                };
                return {
                    value: item.value,
                    itemStyle: itemStyle,
                };
            }),
            label: {
                show: false,
                position: "right",
                color: "#333333",
                fontSize: 14,
                offset: [10, 0],
            },
        },
        {
            name: "背景",
            type: "bar",
            barWidth: 20,
            barGap: "-100%",
            itemStyle: {
                color: "rgba(118, 111, 111, 0.55)",
            },
            data: maxArr,
        },
    ],
};
onMounted(() => {
    console.log(columnar.value)
    if (columnar.value instanceof HTMLElement) {
        let columnarChart = echarts.init(columnar.value)
        columnarChart.setOption(option)
    }
})
</script>
<style scoped>
.columnaCharts {
    height: 60vh;
}
</style>