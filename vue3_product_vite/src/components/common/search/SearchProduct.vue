<template>
  <div>
    <div class="search" @click="DialogOpen">搜索</div>
    <search-dialog ref="Dialog"></search-dialog>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import SearchDialog from "../search/SearchDialog.vue"

let Dialog = ref(null)

let DialogOpen = () => {
  (Dialog.value as any).dialogVisible = true
  console.log((Dialog.value as any).dialogVisible)
}
</script>

<style lang="scss" scoped>
.search {
  width: 125px;
  height: 50px;
  background-color: #4e6ef2;
  user-select: none;
  color: white;
  border-radius: 5px;
  line-height: 50px;
  text-align: center;
  font-size: var(--font--size2);
  margin-left: 50%;
  transform: translateX(-50%);
  transition:all 0.5s ease-out;
}
.search:hover {
    background-color: var(--color--text);
    border-radius: 5px;
  }
</style>