<template>
  <el-dialog v-model="dialogVisible" title="Tips" width="30%">
    <div>
      <el-input
        v-model="searchContent"
        class=""
        placeholder="Type something"
      />
      <el-button type="primary" @click="SearchTo(searchContent,id)">搜索</el-button>
      <el-button @click="CancelSearch">取消</el-button>      
    </div>
  </el-dialog>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { useRouter } from "vue-router";
let searchContent = ref("");
let dialogVisible = ref(false);
let router = useRouter();
const CancelSearch = () => {
  dialogVisible.value = false;
  searchContent.value = "";
};
let id = ref(0)
const SearchTo = (Content: string,id:number) => {
  dialogVisible.value = false;
  router.push({ path: "resultProduct",query: { Content } });
  
};
defineExpose({
  dialogVisible
})
</script>