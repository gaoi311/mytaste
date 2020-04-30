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
        <el-menu-item index="3">
            <router-link :to="'/hotels/' + city" style="text-decoration: none">酒店民宿</router-link>
        </el-menu-item>

        <el-cascader
                size="mini"
                style="width: 120px; margin-top: 17px"
                placeholder="地区"
                :options="options"
                v-model="address"
                :props="{expandTrigger: 'hover'}"
                @change="handleChange"
        ></el-cascader>

        <!--<el-menu-item index="5">-->
            <!--<router-link to="/" style="text-decoration: none">火车票</router-link>-->
        <!--</el-menu-item>-->
        <el-menu-item index="6" v-if="!utoken" style="float: right;margin-right: 100px;margin-left: -20px">
            <router-link to="/register" style="text-decoration: none" target="_blank">注册</router-link>
        </el-menu-item>
        <el-menu-item disabled index="7" v-if="!utoken" style="float: right">
            <span>|</span>
        </el-menu-item>
        <el-menu-item index="8" v-if="!utoken" style="float: right; margin-right: -20px">
            <router-link to="/login" style="text-decoration: none" target="_blank">登录</router-link>
        </el-menu-item>
        <el-submenu index="9" v-if="utoken" style="width: 20px;float: right;margin-right: 100px;margin-left: -25px">
            <template slot="title">
                <el-avatar size="medium" :title="uname" :src="uavatar"></el-avatar>
            </template>
            <el-menu-item index="10-1">
                <router-link to="/self" style="text-decoration: none">我的迈味</router-link>
            </el-menu-item>
            <el-menu-item index="10-2">
                <span @click="logoutHandler">退出登录</span>
            </el-menu-item>
        </el-submenu>
    </el-menu>
</template>


<script>
    let id;
    export default {
        name: "Header",
        data() {
            return {
                activeIndex: '1',
                utoken: '',
                uid: '',
                uname: '',
                uavatar: '',

                address: [],
                options: [
                    {
                        value: '1',
                        label: '北京',
                        children: [
                            {
                                value: '1',
                                label: '北京',
                            }
                        ],
                    },
                    {
                        value: '2',
                        label: '天津',
                        children: [
                            {
                                value: '2',
                                label: '天津',
                            }
                        ]
                    },
                    {
                        value: '3',
                        label: '上海',
                        children: [
                            {
                                value: '3',
                                label: '上海',
                            }
                        ]
                    },
                    {
                        value: '4',
                        label: '重庆',
                        children: [
                            {
                                value: '4',
                                label: '重庆',
                            }
                        ]
                    },
                    {
                        value: '13',
                        label: '安徽',
                        children: [
                            {
                                value: '110',
                                label: '合肥',
                            },
                            {
                                value: '111',
                                label: '芜湖',
                            },
                            {
                                value: '112',
                                label: '蚌埠',
                            },
                            {
                                value: '113',
                                label: '淮南',
                            },
                            {
                                value: '114',
                                label: '马鞍山',
                            },
                            {
                                value: '115',
                                label: '淮北',
                            },
                            {
                                value: '116',
                                label: '铜陵',
                            },
                            {
                                value: '117',
                                label: '安庆',
                            },
                            {
                                value: '118',
                                label: '黄山',
                            },
                            {
                                value: '119',
                                label: '滁州',
                            },
                            {
                                value: '120',
                                label: '阜阳',
                            },
                            {
                                value: '121',
                                label: '宿州',
                            },
                            {
                                value: '122',
                                label: '巢湖',
                            },
                            {
                                value: '123',
                                label: '六安',
                            },
                            {
                                value: '124',
                                label: '亳州',
                            },
                            {
                                value: '125',
                                label: '池州',
                            },
                            {
                                value: '126',
                                label: '宣城',
                            },
                        ]
                    }
                ],
            }
        },
        methods: {
            handleSelect(key, keyPath) {
                // this.activeIndex = key;
            },
            checkUserLogin() {
                this.utoken = localStorage.getItem('utoken', "");
                this.uid = localStorage.getItem('uid', "");
                this.uname = localStorage.getItem('uname', "");
                this.uavatar = `${this.$settings.HOST}` + localStorage.getItem('uavatar', "");
                this.$emit('user', this.uid);
            },
            logoutHandler() {
                localStorage.removeItem("utoken");
                localStorage.removeItem("uid");
                localStorage.removeItem("uname");
                localStorage.removeItem("uavatar");
                this.checkUserLogin();
                this.$router.push('/');
            },
            handleChange(value) {
                localStorage.setItem('province', value[0]);
                localStorage.setItem('city', value[1]);
                this.$router.go(0);
            }
        },
        created() {
            this.checkUserLogin();
            this.city = localStorage.getItem('city', 1);
            this.address = [localStorage.getItem('province', 1), localStorage.getItem('city', 1)];
        }
    }
</script>

<style scoped>

</style>
