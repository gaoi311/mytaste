<template>
    <el-container>
        <el-header>
            <Header></Header>
        </el-header>
        <el-container>
            <el-aside width="300px">
                <el-row style="margin-top: 50px">
                    <el-col :span="24" style="text-align: center">
                        <el-avatar :src="uavatar"></el-avatar>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="24" style="text-align: center">
                        <p>欢迎，{{uname}}&nbsp;&nbsp;<router-link to="/self/info"><i style="color: #ff9c38;" class="el-icon-edit"></i></router-link></p>
                    </el-col>
                </el-row>
            </el-aside>
            <el-main>
                <div>
                    <el-row>
                        <el-col><h3>我的足迹</h3></el-col>
                    </el-row>
                    <div>
                        <el-row>
                            <el-col :span="24">
                                <ul class="scenic-list clearfix">
                                    <li class="scenes_list" v-for="scene in wentScenes" :key="scene.id">
                                        <router-link class="img_a" :to="'/scene/' + scene.id" target="_blank"
                                                     style="color: #333;font-size: 14px;">
                                            <div class="img">
                                                <img :src="mainPhotoSrc(scene.main_photo)" width="192" height="130">
                                            </div>
                                            <h3>{{scene.name}}</h3>
                                        </router-link>
                                    </li>
                                </ul>
                            </el-col>
                        </el-row>
                        <el-pagination
                                v-if="wantScenesCount"
                                background
                                layout="prev, pager, next"
                                :page-size="pageSize"
                                :total="wentScenesCount"
                                @current-change="handleCurrentChange2"
                                style="text-align: center; margin-top: 20px;margin-bottom: 40px">
                        </el-pagination>
                    </div>
                    <hr>
                    <div>
                        <el-row>
                            <el-col :span="24">
                                <ul class="scenic-list clearfix">
                                    <li class="scenes_list" v-for="hotel in wentHotels" :key="hotel.id">
                                        <router-link class="img_a" :to="'/hotel/' + hotel.id" target="_blank"
                                                     style="color: #333;font-size: 14px;">
                                            <div class="img">
                                                <img :src="mainPhotoSrc(hotel.main_photo)" width="192" height="130">
                                            </div>
                                            <h3>{{hotel.name}}</h3>
                                        </router-link>
                                    </li>
                                </ul>
                            </el-col>
                        </el-row>
                        <el-pagination
                                v-if="wentHotelsCount"
                                background
                                layout="prev, pager, next"
                                :page-size="pageSize"
                                :total="wentHotelsCount"
                                @current-change="handleCurrentChange4"
                                style="text-align: center; margin-top: 20px;margin-bottom: 40px">
                        </el-pagination>
                    </div>
                </div>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
    import Header from "@/components/Common/Header";

    export default {
        name: "User",
        data() {
            return {
                uid: 0,
                uname: "",
                uavatar: "",
                pageSize: 4,
                // wantScenesCount: 0,
                // wantScenesPage: 1,
                // wantScenes: [],

                wentScenesCount: 0,
                wentScenesPage: 1,
                wentScenes: [],

                // wantHotelsCount: 0,
                // wantHotelsPage: 1,
                // wantHotels: [],

                wentHotelsCount: 0,
                wentHotelsPage: 1,
                wentHotels: []
            }
        },
        computed: {
            mainPhotoSrc() {
                return mainPhoto => {
                    return `${this.$settings.HOST}${mainPhoto}`;
                }
            }
        },
        methods: {
            getUserInfo() {
                this.uid = sessionStorage.uid || localStorage.uid;
                this.uname = sessionStorage.uname || localStorage.uname;
                this.uavatar = `${this.$settings.HOST}` + (sessionStorage.uavatar || localStorage.uavatar);
            },
            // getUserWantScenes(id) {
            //     this.$axios({
            //         url: `${this.$settings.HOST}/user/loved_scene/`,
            //         method: "GET",
            //         params: {
            //             type: 1,
            //             user: id,
            //             page: this.wantScenesPage,
            //             page_size: this.pageSize
            //         }
            //     }).then(response => {
            //         this.wantScenes = response.data.results;
            //         this.wantScenesCount = response.data.count;
            //     }).catch(error => {
            //         alert(error.response.data);
            //     })
            // },
            getUserWentScenes(id) {
                this.$axios({
                    url: `${this.$settings.HOST}/user/loved_scene/`,
                    method: "GET",
                    params: {
                        type: 2,
                        user: id,
                        page: this.wentPage,
                        page_size: this.pageSize
                    }
                }).then(response => {
                    this.wentScenes = response.data.results;
                    this.wentScenesCount = response.data.count;
                }).catch(error => {
                    alert(error.response.data);
                })
            },
            // getUserWantHotels(id) {
            //     this.$axios({
            //         url: `${this.$settings.HOST}/user/loved_hotel/`,
            //         method: "GET",
            //         params: {
            //             type: 1,
            //             user: id,
            //             page: this.wantHotelsPage,
            //             page_size: this.pageSize
            //         }
            //     }).then(response => {
            //         this.wantHotels = response.data.results;
            //         this.wantHotelsCount = response.data.count;
            //     }).catch(error => {
            //         alert(error.response.data);
            //     })
            // },
            getUserWentHotels(id) {
                this.$axios({
                    url: `${this.$settings.HOST}/user/loved_hotel/`,
                    method: "GET",
                    params: {
                        type: 2,
                        user: id,
                        page: this.wentHotelsPage,
                        page_size: this.pageSize
                    }
                }).then(response => {
                    this.wentHotels = response.data.results;
                    this.wentHotelsCount = response.data.count;
                }).catch(error => {
                    alert(error.response.data);
                })
            },
            // handleCurrentChange1(page) {
            //     this.wantScenesPage = page;
            //     this.getUserWantScenes(this.id);
            // },
            handleCurrentChange2(page) {
                this.wentPage = page;
                this.getUserWentScenes(this.id);
            },
            // handleCurrentChange3(page) {
            //     this.wantHotelsPage = page;
            //     this.getUserWantHotels(this.id);
            // },
            handleCurrentChange4(page) {
                this.wentHotelsPage = page;
                this.getUserWentHotels(this.id);
            },
        },
        created() {
            this.getUserInfo();
            // this.getUserWantScenes(this.uid);
            this.getUserWentScenes(this.uid);
            // this.getUserWantHotels(this.uid);
            this.getUserWentHotels(this.uid);
        },
        components: {
            Header
        },
    }
</script>

<style scoped>
    .scenes_list {
        float: left;
        width: 192px;
        height: 174px;
        display: inline;
        margin: 15px 30px 0 0
    }

    .scenes_list .img_a .img {
        height: 130px;
        overflow: hidden
    }

    .scenes_list .img_a h3 {
        text-align: center;
        border: 1px solid #eee;
        height: 43px;
        font-size: 14px;
        line-height: 42px;
        padding: 0 10px;
        margin: 0 0 0 0;
        overflow: hidden;
        font-weight: normal;
    }
</style>
<!--<div>-->
<!--<el-row>-->
<!--<el-col><h3>我的收藏</h3></el-col>-->
<!--</el-row>-->
<!--<div>-->
<!--<el-row>-->
<!--<el-col :span="24">-->
<!--<ul class="scenic-list clearfix">-->
<!--<li class="scenes_list" v-for="scene in wantScenes" :key="scene.id">-->
<!--<router-link class="img_a" :to="'/scene/' + scene.id" target="_blank"-->
<!--style="color: #333;font-size: 14px;">-->
<!--<div class="img">-->
<!--<img :src="mainPhotoSrc(scene.main_photo)" width="192" height="130">-->
<!--</div>-->
<!--<h3>{{scene.name}}</h3>-->
<!--</router-link>-->
<!--</li>-->
<!--</ul>-->
<!--</el-col>-->
<!--</el-row>-->
<!--<el-pagination-->
<!--v-if="wantScenesCount"-->
<!--background-->
<!--layout="prev, pager, next"-->
<!--:page-size="pageSize"-->
<!--:total="wantScenesCount"-->
<!--@current-change="handleCurrentChange1"-->
<!--style="text-align: center; margin-top: 20px;margin-bottom: 40px">-->
<!--</el-pagination>-->
<!--</div>-->
<!--<div>-->
<!--<el-row>-->
<!--<el-col :span="24">-->
<!--<ul class="scenic-list clearfix">-->
<!--<li class="scenes_list" v-for="hotel in wantHotels" :key="hotel.id">-->
<!--<router-link class="img_a" :to="'/hotel/' + hotel.id" target="_blank"-->
<!--style="color: #333;font-size: 14px;">-->
<!--<div class="img">-->
<!--<img :src="mainPhotoSrc(hotel.main_photo)" width="192" height="130">-->
<!--</div>-->
<!--<h3>{{hotel.name}}</h3>-->
<!--</router-link>-->
<!--</li>-->
<!--</ul>-->
<!--</el-col>-->
<!--</el-row>-->
<!--<el-pagination-->
<!--v-if="wantHotelsCount"-->
<!--background-->
<!--layout="prev, pager, next"-->
<!--:page-size="pageSize"-->
<!--:total="wantHotelsCount"-->
<!--@current-change="handleCurrentChange3"-->
<!--style="text-align: center; margin-top: 20px;margin-bottom: 40px">-->
<!--</el-pagination>-->
<!--</div>-->
<!--</div>-->