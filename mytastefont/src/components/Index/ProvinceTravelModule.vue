<template>
    <el-container>
        <el-aside width="300px">
            111
        </el-aside>
        <el-container>
            <el-header>
                <el-row>
                    <el-col :span="24">
                        <h3>省内游 | 畅享娱乐</h3>
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
                        <a href="" target="_blank">更多景点</a>
                    </el-col>
                </el-row>
            </el-header>
            <el-main style="margin-top: 15px; margin-left: -40px">
                <!--开始-->

                <el-row v-show="activeName==='first'">
                    <el-col :span="24">
                        <ul class="scenic-list clearfix">
                            <li class="scenes_list" v-for="scene in provinceSceneList" :key="scene.id">
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

            </el-main>
        </el-container>
    </el-container>
</template>

<script>
    export default {
        name: "ProvinceTravelModule",
        data() {
            return {
                activeName: 'first',
                provinceSceneList: [],
                country: "中国",
                province: "安徽",
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
            getProvinceSceneList() {
                this.$axios({
                    url: `${this.$settings.HOST}/scenes/`,
                    method: "GET",
                    params: {
                        country: this.country,
                        province: this.province,
                        order: "-hot"
                    }
                }).then(response => {
                    this.provinceSceneList = response.data;
                }).catch(error => {
                    alert(error.response.data);
                })
            },
            handleClick(tab, event) {
            }
        },
        created() {
            this.getProvinceSceneList();
        }
    }
</script>

<style scoped>
    * {
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