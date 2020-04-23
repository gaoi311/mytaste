<template>
    <el-tabs v-model="activeName" @tab-click="handleClick">
        <el-tab-pane label="景点" name="first">景点</el-tab-pane>
        <el-tab-pane label="酒店" name="second">酒店</el-tab-pane>
        <el-tab-pane label="火车票" name="third">火车票</el-tab-pane>
        <el-tab-pane label="攻略" name="fourth">攻略</el-tab-pane>
    </el-tabs>
</template>
<script>
    export default {
        name: 'CityHeader',
        data() {
            return {
                activeName: 'first'
            };
        },
        methods: {
            handleClick(tab, event) {
                console.log(tab, event);
            }
        }
    };
</script>