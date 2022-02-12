<template>
    <el-container>
        <el-header>
            <component-header></component-header>
        </el-header>
        <el-main>Main</el-main>
        <el-footer>Footer</el-footer>
    </el-container>
</template>

<script>
import ComponentHeader from '../src/components/ComponentHeader.vue'

export default {
    name: 'main',
    components: {
        ComponentHeader
    },
    data() {
        return {
        }
    }
}
</script>
<style lang="less" scoped>
    body {
        padding: 0px;
        margin: 0px;
    }
    .el-header{
        background-color: black;
        
    }
    .el-main{
        padding-top: 0;
        height: 700px;
        background-color: rgb(47, 119, 201);
    }
</style>