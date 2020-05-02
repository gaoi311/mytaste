<template>
    <el-container>
        <el-header>
            <Header></Header>
        </el-header>
        <el-main id="top">
            <div>
                <el-row>
                    <el-col :span="3" :offset="6">
                        <el-select
                                @change="getScenes"
                                v-model="typeValue"
                                style="margin-left: 20px;"
                                clearable
                                placeholder="景点类型">
                            <el-option
                                    v-for="item in typeOption"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-col>
                    <el-col :span="3">
                        <el-select
                                @change="getScenes"
                                v-model="gradeValue"
                                style="margin-left: 20px;"
                                clearable
                                placeholder="景区等级">
                            <el-option
                                    v-for="item in gradeOption"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-col>
                    <el-col :span="3">
                        <el-select
                                @change="getScenes"
                                v-model="orderValue"
                                style="margin-left: 20px;"
                                clearable
                                placeholder="排序">
                            <el-option
                                    v-for="item in orderOption"
                                    :key="item.value"
                                    :label="item.label"
                                    :value="item.value">
                            </el-option>
                        </el-select>
                    </el-col>
                </el-row>
                <div class="hotel-item clearfix _j_hotel_item" style="width: 65%;margin-left: 200px"
                     v-for="scene in scenes" :key="scene.id">
                    <div class="hotel-pic">
                        <router-link :to="'/scene/' + scene.id" target="_blank">
                            <img :src="mainPhotoSrc(scene.main_photo)"
                                 style="width: 280px;">
                        </router-link>
                    </div>
                    <div class="hotel-title">
                        <div class="title">
                            <h3>
                                <router-link :to="'/scene/' + scene.id" target="_blank"
                                             style="font-size: 26px; font-weight: bold">{{scene.name}}
                                </router-link>
                            </h3>
                            <p>{{scene.ename}}</p>
                            <span v-if="scene.ticket"
                                  style="margin-left: 480px;margin-bottom: 100px">{{scene.ticket}}元</span>
                            <br>
                        </div>
                    </div>
                    <div class="hotel-info airbnb-info" style="margin-left: -10px; margin-top: -30px">
                        <ul class="nums clearfix" style="list-style: none; margin-left: -30px">
                            <li>
                                <span>{{grade2Stars(scene.grade)}}</span>
                            </li>
                            <li class="divide"></li>
                            <li>
                                <el-rate
                                        :value="parseFloat(scene.score)"
                                        disabled
                                        show-score
                                        text-color="#ff9900">
                                </el-rate>
                            </li>
                        </ul>
                        <p style="margin-left: 10px">热度 <span
                                style="font-size: 24px;color: #c0a16b">{{scene.hot}}</span></p>
                        <div class="location" style="margin-left: 8px;margin-top: 20px">
                            <i class="el-icon-location"></i><span>{{scene.address.slice(0, 20)}}</span>
                        </div>
                    </div>
                    <div class="hotel-btns">
                        <div class="btn-tel">

                            <el-link class="btn-detail" type="primary" style="text-decoration: none" target="_blank"
                                     :href="'/scene/' + scene.id + '#comment'">
                                <span style="font-size: 20px">{{scene.comment_num}}</span>
                            </el-link>
                            条评论
                        </div>
                    </div>
                    <div class="hotel-btns" style="margin-top: 15px">
                        <div class="btn-tel">
                            <a :href="'/scene/' + scene.id" target="_blank">
                                <el-button size="small" type="primary">查看详情</el-button>
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <el-pagination
                    background
                    layout="prev, pager, next"
                    :page-size="pageSize"
                    :total="scenesCount"
                    @current-change="handleCurrentChange"
                    style="text-align: center; margin-top: 20px;margin-bottom: 40px">
            </el-pagination>
        </el-main>
        <el-footer>
            <Footer></Footer>
        </el-footer>
    </el-container>
</template>

<script>
    import Header from "@/components/Common/Header";
    import Footer from "@/components/Common/Footer";

    export default {
        name: "SceneList",
        data() {
            return {
                id: 0,
                pageSize: 10,
                scenesCount: 0,
                page: 1,
                scenes: [],

                typeOption: [
                    {value: '2', label: '自然'},
                    {value: '3', label: '文化'},
                    {value: '4', label: '历史'},
                    {value: '5', label: '建筑'},
                    {value: '6', label: '公园'},
                    {value: '7', label: '休闲'},
                    {value: '1', label: '其他'},
                ],

                gradeOption: [
                    {value: '2', label: 'A'},
                    {value: '3', label: 'AA'},
                    {value: '4', label: 'AAA'},
                    {value: '5', label: 'AAAA'},
                    {value: '6', label: 'AAAAA'},
                ],

                orderOption: [
                    {value: '-hot', label: '热度最高'},
                    {value: '-score', label: '评分最高'},
                    {value: '-comment_num', label: '评论数最多'},
                ],

                gradeValue: '',
                typeValue: '',
                orderValue: ''
            }
        },
        computed: {
            mainPhotoSrc() {
                return mainPhoto => {
                    return `${this.$settings.HOST}${mainPhoto}`;
                }
            },
            grade2Stars() {
                return grade => {
                    let star = "暂无评级";
                    switch (grade) {
                        case 2:
                            star = "A";
                            break;
                        case 3:
                            star = "AA";
                            break;
                        case 4:
                            star = "AAA";
                            break;
                        case 5:
                            star = "AAAA";
                            break;
                        case 6:
                            star = "AAAAA";
                            break;
                    }
                    return star
                }
            }
        },
        methods: {
            getScenes() {
                this.$axios({
                    url: `${this.$settings.HOST}/scenes/${this.id}/`,
                    method: "GET",
                    params: {
                        page: this.page,
                        page_size: this.pageSize,
                        scene_type: this.typeValue,
                        scene_grade: this.gradeValue,
                        scene_order: this.orderValue
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
                location.href = '#top';
                this.getScenes(this.id);
            },
        },
        created() {
            this.id = this.$route.params.id;
            this.getScenes();
        },
        components: {
            Footer,
            Header
        }
    }
</script>

<style scoped>
    .divide {
        border-left: solid 2px #ccc;
        height: 15px;
        vertical-align: middle;
        display: inline-block;
        margin-left: 10px;
        margin-right: 10px;
    }

    .hotel-item {
        padding: 10px 0;
        border-bottom: 1px solid #ececec;
        position: relative;
        transition: all 400ms
    }

    .hotel-pic {
        float: left;
        display: inline;
        width: 330px;
        height: 180px;
        position: relative
    }

    .hotel-pic img {
        border-radius: 5px;
        width: 330px;
        height: 180px;
    }

    .hotel-title {
        overflow: hidden
    }

    .hotel-title h3 {
        margin-right: 5px;
        line-height: 30px;
        font-size: 18px;
        font-weight: normal;
        display: inline
    }

    .hotel-title h3 a {
        color: #666
    }

    .hotel-title span {
        font-size: 14px;
        color: #999;
        vertical-align: middle
    }

    .hotel-title .title {
        float: left
    }

    .hotel-info {
        float: left;
        width: 315px;
        margin-right: 20px
    }

    .hotel-info .nums {
        margin: 15px 0 5px;
        color: #999;
        line-height: 15px;
    }

    .hotel-info .nums li {
        float: left
    }

    .hotel-info .rating em {
        font-size: 18px
    }

    .hotel-info .rating strong {
        font-size: 14px;
        color: #666;
        font-weight: normal
    }

    .hotel-info .nums a {
        color: #999
    }

    .hotel-info .nums em {
        font-style: normal;
        font-size: 14px;
        color: #ff8a00
    }

    .hotel-info .location {
        color: #999;
        line-height: 20px
    }

    .hotel-info .location a {
        color: #666
    }

    .hotel-info .location em {
        font-style: normal;
        color: #fa9f00
    }

    .airbnb-info .airbnb-icons span {
        float: left;
        text-align: center;
        width: 25%;
        white-space: nowrap
    }

    .airbnb-info .airbnb-icons i {
        display: inline-block;
        width: 18px;
        height: 17px;
        overflow: hidden
    }

    .btn-tel {
        padding: 6px 0;
        line-height: 24px;
        font-size: 14px;
        color: #333;
        text-align: right
    }

    .hotel-other .collect a {
        display: inline-block
    }

    .hotel-other .collect i {
        display: inline-block;
        float: left;
        margin: 2px 5px 0 0;
        width: 12px;
        height: 12px;
    }

    .hotel-other .btn-addCollect i {
        background-position: -130px -50px
    }

    .hotel-other .btn-cancelCollect i {
        background-position: -145px -50px
    }
</style>