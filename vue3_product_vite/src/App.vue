<template>
  <div class="page">
    <header class="header">
      <search-product></search-product>
      <history-nav></history-nav>
    </header>
    <section class="main">
      <div class="main-content"><router-view /></div>
    </section>
  </div>
    
  
</template>

<script setup lang="ts">
import { } from 'vue'

import SearchProduct from '@/components/common/search/SearchProduct.vue'
import HistoryNav from '@/components/common/HistoryNav.vue'


</script>
<style lang="scss">
@import '@/assets/css/base.css';

html,
body {
  background-color: #f4f5f5;
}

.page {
  height: 100vh;
}

.header {
  height: 80px;
  box-shadow: 0 0 2px rgb(0 0 0 / 25%);
  background-color: #ffffff;
}

.main {
  height: calc(100% - 110px);
  .main-content {
    margin-top: 30px;
  }
}
</style>
