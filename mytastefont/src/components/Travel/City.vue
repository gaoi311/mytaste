<template>
    <el-container>
        <el-header>
            <Header></Header>
        </el-header>
        <el-main>

            <!--开始-->

            <el-row>
                <el-col :span="16" :offset="3">
                    <h1>{{city.name}}</h1>
                </el-col>
                <el-col :span="2" style="margin-top: 30px">
                    <el-link type="primary" href="#">加入收藏</el-link>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="18" :offset="3">
                    <el-tabs v-model="activeName" @tab-click="handleClick">
                        <el-tab-pane label="景点" name="first"></el-tab-pane>
                        <el-tab-pane label="酒店" name="second"></el-tab-pane>
                        <el-tab-pane label="攻略" name="third"></el-tab-pane>
                        <el-tab-pane label="驴友说" name="fourth"></el-tab-pane>
                    </el-tabs>
                </el-col>
            </el-row>

            <div v-show="activeName==='first'">
                <el-row>
                    <el-col :span="18" :offset="3">
                        <h2>景点概括</h2>
                        <p>{{city.summary}}</p>
                    </el-col>
                </el-row>
                <hr>
                <el-row>
                    <el-col :span="18" :offset="3">
                        <ul class="scenic-list clearfix">
                            <li class="scenes_list" v-for="scene in scenes" :key="scene.id">
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
            </div>

            <div v-show="activeName==='second'">
                xxxxxxxh
            </div>
            <div v-show="activeName==='third'">
                xxxxxxxt
            </div>
            <div v-show="activeName==='fourth'">
                xxxxxxxs
            </div>

            <el-pagination
                    background
                    layout="prev, pager, next"
                    :page-size="pageSize"
                    :total="scenesCount"
                    @current-change="handleCurrentChange"
                    style="text-align: center">
            </el-pagination>

        </el-main>
    </el-container>
</template>

<script>
    import Header from "@/components/Common/Header";
    import CityHeader from "@/components/Common/CityHeader";

    export default {
        name: "City",
        data() {
            return {
                pageSize: 8,
                scenesCount: 0,
                page: 1,
                city: undefined,
                activeName: 'first',
                scenes: [],
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
            getCity(id) {
                this.$axios({
                    url: `${this.$settings.HOST}/city/${id}/`,
                    methods: "GET",
                }).then(response => {
                    this.city = response.data;
                }).catch(error => {
                    alert(error.response.data);
                })
            },
            getScenes(id) {
                this.$axios({
                    url: `${this.$settings.HOST}/scenes/${id}/`,
                    methods: "GET",
                    params: {
                        page: this.page,
                        page_size: this.pageSize
                    }
                }).then(response => {
                    this.scenes = response.data.results;
                    this.scenesCount = response.data.count;
                }).catch(error => {
                    alert(error.response.data);
                })
            },
            handleCurrentChange(page) {
                this.page = page;
                this.getScenes(this.id);
            },
            handleClick(tab, event) {
            }
        },
        created() {
            this.id = this.$route.params.id;
            this.getCity(this.id);
            this.getScenes(this.id);
        },
        components: {
            // CityHeader,
            Header
        }
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