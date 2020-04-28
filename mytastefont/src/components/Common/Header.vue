<template>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
             active-text-color="#ffd04b">
        <el-menu-item style="margin-left: 100px">
            <router-link to="/" style="font-size: 30px;text-decoration: none">
                <img height="50px" src="../../../static/image/logo.png" alt="">迈味
            </router-link>
        </el-menu-item>
        <el-menu-item index="1">
            <router-link to="/" style="text-decoration: none">首页</router-link>
        </el-menu-item>
        <el-menu-item index="2">
            <router-link to="/destination" style="text-decoration: none">目的地</router-link>
        </el-menu-item>
        <el-menu-item index="6">
            <router-link to="/hotels/1" style="text-decoration: none">酒店民宿</router-link>
        </el-menu-item>
        <!--<el-submenu index="4">-->
        <!--<template slot="title" style="text-decoration: none">去旅行</template>-->
        <!--<el-menu-item index="4-1">-->
        <!--<router-link to="/">当地游</router-link>-->
        <!--</el-menu-item>-->
        <!--<el-menu-item index="4-2">-->
        <!--<router-link to="/">省内游</router-link>-->
        <!--</el-menu-item>-->
        <!--<el-menu-item index="4-3">-->
        <!--<router-link to="/">国内游</router-link>-->
        <!--</el-menu-item>-->
        <!--</el-submenu>-->
        <el-menu-item index="5">
            <router-link to="/" style="text-decoration: none">火车票</router-link>
        </el-menu-item>
        <el-menu-item index="8" v-if="!utoken" style="float: right;margin-right: 100px;margin-left: -20px">
            <router-link to="/register" style="text-decoration: none" target="_blank">注册</router-link>
        </el-menu-item>
        <el-menu-item disabled index="9" v-if="!utoken" style="float: right">
            <span>|</span>
        </el-menu-item>
        <el-menu-item index="10" v-if="!utoken" style="float: right; margin-right: -20px">
            <router-link to="/login" style="text-decoration: none" target="_blank">登录</router-link>
        </el-menu-item>
        <el-submenu index="11" v-if="utoken" style="width: 20px;float: right;margin-right: 100px;margin-left: -25px">
            <template slot="title">
                <el-avatar size="medium" :title="uname" :src="uavatar"></el-avatar>
            </template>
            <el-menu-item index="11-1">
                <router-link to="/self" style="text-decoration: none">我的迈味</router-link>
            </el-menu-item>
            <el-menu-item index="11-2">
                <span @click="logoutHandler">退出登录</span>
            </el-menu-item>
        </el-submenu>
    </el-menu>
</template>


<script>
    export default {
        name: "Header",
        data() {
            return {
                activeIndex: '1',
                utoken: '',
                uid: '',
                uname: '',
                uavatar: ''
            }
        },
        methods: {
            handleSelect(key, keyPath) {
                // this.activeIndex = key;
            },
            checkUserLogin() {
                this.utoken = sessionStorage.utoken || localStorage.utoken;
                this.uid = sessionStorage.uid || localStorage.uid;
                this.uname = sessionStorage.uname || localStorage.uname;
                this.uavatar = `${this.$settings.HOST}` + (sessionStorage.uavatar || localStorage.uavatar);
                this.$emit('user', this.uid);
            },
            logoutHandler() {
                localStorage.removeItem("utoken");
                localStorage.removeItem("uid");
                localStorage.removeItem("uname");
                localStorage.removeItem("uavatar");
                sessionStorage.removeItem("utoken");
                sessionStorage.removeItem("uid");
                sessionStorage.removeItem("uname");
                sessionStorage.removeItem("uavatar");
                this.checkUserLogin();
                // this.$router.push('/');
            },
        },
        created() {
            this.checkUserLogin();
        }
    }
</script>

<style scoped>

</style>
