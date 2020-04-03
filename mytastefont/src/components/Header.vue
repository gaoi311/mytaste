<template>
    <el-menu :default-active="activeIndex" style="font-weight: bolder;" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item style="margin-left: 100px">
            <router-link to="/" style="font-size: 30px;text-decoration: none">
                <img height="60px" src="../../static/image/logo.png" alt="">迈味
            </router-link>
        </el-menu-item>
        <el-menu-item index="1">
            <router-link to="/" style="text-decoration: none">首页</router-link>
        </el-menu-item>
        <el-menu-item index="2">
            <router-link to="/" style="text-decoration: none">目的地</router-link>
        </el-menu-item>
        <el-menu-item index="3">
            <router-link to="/" style="text-decoration: none">旅游攻略</router-link>
        </el-menu-item>
        <el-submenu index="4">
            <template slot="title" style="text-decoration: none">去旅行</template>
            <el-menu-item index="4-1">
                <router-link to="/">省内游</router-link>
            </el-menu-item>
            <el-menu-item index="4-2">
                <router-link to="/">国内游</router-link>
            </el-menu-item>
            <el-menu-item index="4-3">
                <router-link to="/">国外游</router-link>
            </el-menu-item>
        </el-submenu>
        <el-menu-item index="5">
            <router-link to="/" style="text-decoration: none">机票火车票</router-link>
        </el-menu-item>
        <el-menu-item index="6">
            <router-link to="/" style="text-decoration: none">酒店民宿</router-link>
        </el-menu-item>
        <el-menu-item index="7">
            <router-link to="/" style="text-decoration: none">驴友说</router-link>
        </el-menu-item>
        <el-menu-item index="8" style="float: right;margin-right: 100px;margin-left: -25px">
            <router-link to="/register" style="text-decoration: none">注册</router-link>
        </el-menu-item>
        <el-menu-item index="8" style="float: right">
            <span> | </span>
        </el-menu-item>
        <el-menu-item index="9" style="float: right; margin-right: -25px">
            <router-link to="/login" style="text-decoration: none">登录</router-link>
        </el-menu-item>
        <el-menu-item index="10" style="display: none">
            <router-link to="/self" style="text-decoration: none">我的</router-link>
        </el-menu-item>
    </el-menu>
</template>



<script>
    export default {
        name: "Header",
        data() {
            return {
                activeIndex: '1',
                is_login: '0',
            }
        },
        methods: {
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            }
        },
        created() {
        }
    }
</script>

<style scoped>

</style>