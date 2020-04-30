<template>
    <el-container>
        <el-aside width="300px">
        </el-aside>
        <el-container>
            <el-header>
                <el-row>
                    <el-col :span="24">
                        <router-link :to="'/city/' + 1"><h3>当地游 | 畅享娱乐</h3></router-link>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="18">
                        <el-tabs v-model="activeName" @tab-click="handleClick">
                            <el-tab-pane label="景点" name="first"></el-tab-pane>
                            <el-tab-pane label="酒店" name="second"></el-tab-pane>
                        </el-tabs>
                    </el-col>
                    <el-col :span="2" style="margin-top: 28px; margin-left: 20px;text-align: center">
                        <router-link :to="'/' + module + '/' + city" target="_blank">更多{{title}}</router-link>
                    </el-col>
                </el-row>
            </el-header>
            <el-main style="margin-top: 15px; margin-left: -40px">
                <!--开始-->

                <el-row v-show="activeName==='first'">
                    <el-col :span="24">
                        <ul class="scenic-list clearfix">
                            <li class="scenes_list" v-for="scene in localSceneList" :key="scene.id">
                                <router-link class="img_a" :to="'/scene/' + scene.id" target="_blank"
                                             style="color: #333;font-size: 14px;">
                                    <div class="img">
                                        <img :src="scene.main_photo" width="192" height="130">
                                    </div>
                                    <h3>{{scene.name}}</h3>
                                </router-link>
                            </li>
                        </ul>
                    </el-col>
                </el-row>


                <el-row v-show="activeName==='second'">
                    <el-col :span="24">
                        <ul class="scenic-list clearfix">
                            <li class="scenes_list" v-for="hotel in localHotelList" :key="hotel.id">
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
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
    export default {
        name: "LocalTravelModule",
        data() {
            return {
                activeName: 'first',
                localSceneList: [],
                localHotelList: [],
                country: "中国",
                province: 1,
                city: 1,
                module: "scenes",
                title: '景点'
            }
        },
        computed: {
            mainPhotoSrc() {
                return function (mainPhoto) {
                    return `${this.$settings.HOST}${mainPhoto}`;
                }
            }
        },
        methods: {
            getLocalSceneList() {
                this.$axios({
                    url: `${this.$settings.HOST}/scenes/`,
                    method: "GET",
                    params: {
                        province: this.province,
                        city: this.city
                    }
                }).then(response => {
                    this.localSceneList = response.data;
                }).catch(error => {
                    alert(error.response.data);
                })
            },
            getLocalHotelList() {
                this.$axios({
                    url: `${this.$settings.HOST}/hotels/`,
                    method: "GET",
                    params: {
                        city: this.city
                    }
                }).then(response => {
                    this.localHotelList = response.data;
                }).catch(error => {
                    alert(error.response.data);
                })
            },
            handleClick(tab, event) {
                if (tab.name === 'first') {
                    this.title = "景点";
                    this.module = "scenes";
                    this.getLocalSceneList();
                } else if (tab.name === 'second') {
                    this.title = "酒店";
                    this.module = "hotels";
                    this.getLocalHotelList();
                }
            }
        },
        created() {
            this.province = localStorage.getItem('province', 1);
            this.city = localStorage.getItem('city', 1);
            this.getLocalSceneList();
        }
    }
</script>

<style scoped>
    * {
        text-decoration: none;
    }

    a:link {
        color: #000000;
        text-decoration: none;
    }

    a:visited {
        color: #000000;
        text-decoration: none;
    }

    a:hover {
        color: #000000;
        text-decoration: none;
    }

    li {
        height: 50px;
    }

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