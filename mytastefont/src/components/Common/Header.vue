<template>
    <div>
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
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
            <el-menu-item index="3">
                <router-link to="/" style="text-decoration: none">旅游攻略</router-link>
            </el-menu-item>
            <el-submenu index="4">
                <template slot="title" style="text-decoration: none">去旅行</template>
                <el-menu-item index="4-1">
                    <router-link to="/">当地游</router-link>
                </el-menu-item>
                <el-menu-item index="4-2">
                    <router-link to="/">省内游</router-link>
                </el-menu-item>
                <el-menu-item index="4-3">
                    <router-link to="/">国内游</router-link>
                </el-menu-item>
                <el-menu-item index="4-4">
                    <router-link to="/">结伴游</router-link>
                </el-menu-item>
            </el-submenu>
            <el-menu-item index="5">
                <router-link to="/" style="text-decoration: none">火车票</router-link>
            </el-menu-item>
            <el-menu-item index="6">
                <router-link to="/" style="text-decoration: none">酒店民宿</router-link>
            </el-menu-item>
            <el-menu-item index="7">
                <router-link to="/" style="text-decoration: none">驴友说</router-link>
            </el-menu-item>
            <el-menu-item index="8" v-show="!token" style="float: right;margin-right: 100px;margin-left: -20px">
                <router-link to="/register" style="text-decoration: none" target="_blank">注册</router-link>
            </el-menu-item>
            <el-menu-item index="9" v-show="!token" style="float: right">
                <span>|</span>
            </el-menu-item>
            <el-menu-item index="10" v-show="!token" style="float: right; margin-right: -20px">
                <router-link to="/login" style="text-decoration: none" target="_blank">登录</router-link>
            </el-menu-item>
            <el-submenu index="11" v-show="token" style="float: right;margin-right: 100px;margin-left: -25px">
                <template slot="title"><img :src="avator"></template>
                <el-menu-item index="11-1">
                    <router-link to="/self/feet">我的足迹</router-link>
                </el-menu-item>
                <el-menu-item index="11-2">
                    <router-link to="/self/route">我的路线</router-link>
                </el-menu-item>
                <el-menu-item index="11-3">
                    <span @click="logoutHandler">退出登录</span>
                </el-menu-item>
            </el-submenu>
        </el-menu>
    </div>
</template>


<script>
    export default {
        name: "Header",
        data() {
            return {
                activeIndex: '1',
                is_login: '0',
                token: '',
                avator: ''
            }
        },
        props: ['activeIndexParent'],
        methods: {
            handleSelect(key, keyPath) {
                // this.activeIndex = key;
                this.$emit('headerValue', key);
            },
            check_user_login() {
                this.token = sessionStorage.token || localStorage.token;
                return this.token;
            },
            get_user_avator() {
                console.log(sessionStorage.avator);
                this.avator = "http://api.mytaste.com/upload/" + (sessionStorage.avator || localStorage.avator);
                console.log(this.avator);
                return this.avator;
            },
            logoutHandler() {
                localStorage.removeItem("token");
                localStorage.removeItem("id");
                localStorage.removeItem("username");
                sessionStorage.removeItem("token");
                sessionStorage.removeItem("id");
                sessionStorage.removeItem("username");
                this.check_user_login();
            }
        },
        created() {
            console.log(this.avator);
            this.check_user_login();
            this.get_user_avator();
        }
    }
</script>

<style scoped>

</style>
