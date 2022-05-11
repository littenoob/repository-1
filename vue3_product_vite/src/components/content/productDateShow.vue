<template>
    <div class="content">
        <main class="showPlace">
            <div class="lineCharts">
                <h1>{{brand}}价格走势</h1>
                <price-move :priceData="priceData"></price-move>
            </div>
            <div class="columnaCharts">
                <h1>柱状主要影响因素</h1>
                <columnar-form></columnar-form>
            </div>
            <div class="cakeCharts">
                <h1>价格走势影响因素</h1>
                <influence-form class="influence"></influence-form>
            </div>
            <div class="evaluation"></div>
        </main>
        <div class="news"></div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref} from 'vue';

import {PriceDays} from '@/api/price'
import columnarForm from '@/components/echarts/columnarForm.vue'
import influenceForm from '@/components/echarts/influenceForm.vue'
import priceMove from '@/components/echarts/priceMove.vue'
import { useRoute } from 'vue-router';
import PriceMove from '@/components/echarts/priceMove.vue';

const route = useRoute()
let priceData = ref<any>([])
let brand = (route.query.type as any).split('（')[0]
onMounted(() => {
    PriceDays(7,brand,route.query.brand as any)?.then(res => {
        console.log(res)
        if (typeof res == 'string') {
            priceData.value = JSON.parse(res)
        }
        else {
            priceData.value = res
        }
    })
})

</script>

<style lang="scss">
.showPlace {
    flex: 1;
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    div {
        text-align: center;
        border-radius: 4px;
        margin: 1em;
        background-color: white;
        h1 {
            margin-top: 2em;
        }
    }
}

.content {
    display: flex;
}
.news {
    margin: 1em 0 1em 1em;
    width: 20em;
    border-radius: 10px;
    background-color: white;
}
</style>