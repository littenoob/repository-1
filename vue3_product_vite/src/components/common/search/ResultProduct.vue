<template>
  <el-table v-loading="loading" class="table" size="large" :header-row-style="rowStyle" :row-style="rowStyle" :data="filterTableData"
    style="width: 100%" border highlight-current-row @current-change="handleCurrentChange">
    <el-table-column prop="date" label="日期" width="180" />
    <el-table-column prop="brand" label="品牌" width="180" />
    <el-table-column prop="type" label="类型" width="540" />
    <el-table-column prop="price" label="价格" width="180" />
    <el-table-column prop="isHot" label="火爆程度" />
    <el-table-column align="right">
      <template #header>
        <el-input v-model="search" size="large" placeholder="Type to search" />
      </template>
    </el-table-column>
  </el-table>
  <div class="footer">
    <el-pagination class="pagination" background layout="prev, pager, next" :total="total" v-model:currentPage="page"
      :disabled="disabled" @current-change="pageChange" />
  </div>

</template>

<script lang="ts" setup>
import { onBeforeMount, reactive, ref, watchEffect, computed, Ref,watch, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import { SearchphoneResult } from '@/api/price'

interface phone {
  date: string
  brand: string
  type: string
}
const router = useRouter()
const route = useRoute()
let tableData = ref([])
let phoneResult = ref([])
let total = ref(0)
let page = ref(1)
const disabled = ref(false)
const loading = ref(true)
const pageChange = (val: number) => {
  console.log(`current page: ${val}`)
  page.value = val
}
const searchResult = () => {
  console.log()
  SearchphoneResult(route.query.Content as any)?.then(res => {
    if (typeof res === 'string') {
      phoneResult.value = JSON.parse(res)
      total.value = phoneResult.value.length
      tableData.value = phoneResult.value.slice(0, 10)
      console.log(tableData.value)
    }
  })
}
onMounted(() => {
  searchResult
  loading.value = false
})
watchEffect(searchResult)
watch(page, (page:number,prevpage:number) => {
  tableData.value = phoneResult.value.slice((page-1)*10,(page-1)*10+10)
})
const handleCurrentChange = (val: phone) => {
  console.log(val)
  router.push({path:'productDateShow',query:{
    'brand':val?.brand,
    'type':val?.type,
  }})
}
const search = ref('')
const filterTableData = computed(() =>
  tableData.value.filter(
    (data: phone) =>
      !search.value ||
      data.type.toLowerCase().includes(search.value.toLowerCase())
  )
)

const rowStyle = {
  height: '7vh'
}

</script>

<style lang="scss">
.footer {
  margin-top: 5vh;
  position: relative;

  .pagination {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
}

.table {
  font-size: 1rem;
}
</style>