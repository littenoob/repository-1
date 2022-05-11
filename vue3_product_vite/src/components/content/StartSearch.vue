<template>
    <div class="outer">
        <div class="contain">
            <p class="">搜索产品</p>
            <el-image class="logo" :src="logo"></el-image>
        </div>
        <div class="news-column">
            <p>新闻</p>
            <el-scrollbar height="75vh">
                <p v-for="item in news_list" :key="item" class="scrollbar-demo-item">{{ item }}</p>
            </el-scrollbar>
        </div>
    </div>


</template>
<script setup lang="ts">
import { reactive, ref } from 'vue'
import logo from '@/assets/imgs/logo.png'
import request from '@/api/request';

const index = new Array(20).fill('魅族旗舰魅族17再次降价仅需1799')
const news_list = reactive(index)

</script>

<style lang="scss" scoped>
.outer {
    height: 100%;

    .scrollbar-demo-item {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 50px;
        margin: 10px;
        text-align: center;
        border-radius: 4px;
        background: var(--el-color-primary-light-9);
        color: var(--el-color-primary);
    }

    .news-column {
        margin-top: -80vh;
        margin-right: 40px;
        float: right;
        background-color: #ffffff;
        text-align: center;
    }
    .news-column::after{
            clear: both;
            display: table;
            content: " ";
        }

}

.contain {
    background-color: #ffffff;
    margin: 0 auto;
    width: 60%;
    height: 800px;
    text-align: center;
    font-size: 50px;
    color: var(--color--text);
    border: 1px solid #d0d7d1;
    border-radius: 6px;


    .logo {
        max-width: 60%;
        max-height: 60%;
    }
}
</style>