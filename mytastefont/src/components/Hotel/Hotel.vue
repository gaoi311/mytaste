<template>
    <el-container>
        <el-header>
            <Header v-on:user="getUser"></Header>
        </el-header>
        <el-main>
            <el-row id="summary">
                <el-col :span="18" :offset="3">
                    <el-row>
                        <el-col :span="24">
                            <h1>{{hotel.name}}</h1>
                        </el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="20">
                            <span>{{hotel.ename}}</span><span
                                style="margin-left: 30px">{{number2Grade(hotel.grade)}}</span>
                            <p>周边：{{hotel.around}}</p>
                        </el-col>
                        <el-col :span="2">
                            <span style="font-size: 28px;font-weight: bolder;color: #2e6da4;">{{hotel.score}}分</span>
                        </el-col>
                        <el-col :span="2">
                            <p>评论数{{hotel.comment_num}}</p>
                            <p style="margin-top: -10px">{{hotel.score_comment}}</p>
                        </el-col>
                    </el-row>

                    <el-row>
                        <img :src="hotel.main_photo"
                             alt="" style="width: 100%;height: 384px">
                    </el-row>
                    <hr>
                    <el-row>
                        <el-link type="primary" href="#summary" style="text-decoration: none">概括</el-link>
                        <el-link type="primary" href="#comment" style="margin-left: 50px; text-decoration: none">评论
                        </el-link>
                        <el-button type="primary" @click="newComment" size="small" style="float: right">
                            我要评论
                        </el-button>
                    </el-row>
                    <hr>

                    <el-row>
                        <el-col :span="24">
                            <span style="font-size: 20px;margin-right: 100px">基本信息</span>
                            <span>入住时间: 14:00 - 00:00 离店时间: 12:00之前</span>
                        </el-col>
                    </el-row>
                    <hr>
                    <el-row>
                        <el-col :span="24">
                            <span style="font-size: 20px;margin-right: 100px">交通</span>
                            <span>{{hotel.traffic}}</span>
                        </el-col>
                    </el-row>
                </el-col>
            </el-row>
            <hr>
            <el-row id="comment">
                <el-col :span="18" :offset="3">
                    <div class="rev-list">
                        <ul style="list-style: none">
                            <li class="rev-item comment-item clearfix" v-for="comment in comments" :key="comment.id">
                                <div class="user">
                                    <router-link class="avatar" :to="'/user/' + 1" target="_blank"><img
                                            :src="mainPhotoSrc(comment.user_info.avatar)"
                                            width="48" height="48">
                                    </router-link>
                                </div>
                                <router-link class="name" :to="'/user/' + 1" target="_blank">
                                    {{comment.user_info.username}}
                                </router-link>
                                <span class="s-star" :class="score2Stars(comment.score)"></span>
                                <p class="rev-txt">
                                    {{comment.content}}
                                </p>

                                <div class="info clearfix">
                                    <span class="time">{{comment.created_time}}</span>
                                </div>
                            </li>
                        </ul>
                    </div>
                </el-col>
            </el-row>
            <el-pagination
                    background
                    layout="prev, pager, next"
                    :page-size="pageSize"
                    :total="commentsCount"
                    @current-change="handleCurrentChange"
                    style="text-align: center; margin-top: 20px;margin-bottom: 40px">
            </el-pagination>
            <!--新增评论-->
            <el-dialog :title="'发布您的评论-' + hotel.name + '-景区'" :visible.sync="dialogFormVisible">
                <el-form :model="form">
                    <el-form-item label="评分" :label-width="formLabelWidth">
                        <el-rate
                                v-model="form.score"
                                :colors="colors">
                        </el-rate>
                    </el-form-item>
                    <el-form-item label="内容" :label-width="formLabelWidth">
                        <el-input type="textarea" v-model="form.content" placeholder="此处发表您的评论"></el-input>
                    </el-form-item>
                </el-form>
                <div slot="footer" class="dialog-footer">
                    <el-button @click="dialogFormVisible = false">取 消</el-button>
                    <el-button type="primary" @click="onSubmit">确 定</el-button>
                </div>
            </el-dialog>
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
        name: "Hotel",
        data() {
            return {
                uid: 0,
                id: 0,
                hotel: null,
                comments: [],
                pageSize: 10,
                commentsCount: 0,
                page: 1,
                dialogFormVisible: false,
                form: {
                    score: 0,
                    content: '',
                },
                formLabelWidth: '120px',
                colors: ['#99A9BF', '#F7BA2A', '#FF9900']
            }
        },
        computed: {
            mainPhotoSrc() {
                return mainPhoto => {
                    return `${this.$settings.HOST}${mainPhoto}`;
                }
            },
            score2Stars() {
                return score => {
                    let star = "s-star0";
                    switch (score) {
                        case 1:
                            star = "s-star1";
                            break;
                        case 2:
                            star = "s-star2";
                            break;
                        case 3:
                            star = "s-star3";
                            break;
                        case 4:
                            star = "s-star4";
                            break;
                        case 5:
                            star = "s-star5";
                            break;
                    }
                    return star
                }
            },
            number2Grade() {
                return grade => {
                    let star = "暂无评级";
                    switch (grade) {
                        case 2:
                            star = "一星级";
                            break;
                        case 3:
                            star = "二星级";
                            break;
                        case 4:
                            star = "三星级";
                            break;
                        case 5:
                            star = "四星级";
                            break;
                        case 6:
                            star = "五星级";
                            break;
                    }
                    return star
                }
            }
        },
        methods: {
            getUser(e) {
                this.uid = e;
            },
            getHotel(id) {
                this.$axios({
                    url: `${this.$settings.HOST}/hotel/${id}/`,
                    method: "GET",
                }).then(response => {
                    this.hotel = response.data;
                }).catch(error => {
                    alert(error.response.data);
                })
            },
            getHotelComments(id) {
                this.$axios({
                    url: `${this.$settings.HOST}/hotel_comments/${id}/`,
                    method: 'GET',
                    params: {
                        page: this.page,
                        page_size: this.pageSize
                    }
                }).then(response => {
                    this.comments = response.data.results;
                    this.commentsCount = response.data.count;
                }).catch(error => {
                    alert(error.response);
                })
            },
            handleCurrentChange(page) {
                this.page = page;
                location.href = '#comment';
                this.getHotelComments(this.id);
            },
            open() {
                this.$confirm('亲，发表评论需要登录哦, 前往登录?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    this.$router.push('/login')
                })
            },
            newComment() {
                if (!this.uid) {
                    this.open();
                } else {
                    this.dialogFormVisible = true;
                }
            },
            onSubmit() {
                this.dialogFormVisible = false;
                this.$axios({
                    url: `${this.$settings.HOST}/hotel_comment/`,
                    method: 'POST',
                    data: {
                        user: this.uid,
                        content: this.form.content,
                        score: this.form.score,
                        hotel: this.id
                    }
                }).catch(error=>{
                    alert("啊呀，出错啦！请重试!");
                });
                this.form.score = 0;
                this.form.content = "";
            }
        },
        created() {
            this.id = this.$route.params.id;
            this.getHotel(this.id);
            this.getHotelComments(this.id);
            this.getUser();
        },
        components: {
            Footer,
            Header
        }
    }
</script>

<style scoped>
    .rev-list {
        margin-left: -20px;
        border-bottom: 1px solid #eee
    }

    .rev-item {
        padding: 25px 0 20px 70px;
        border-bottom: 1px dashed #dedede
    }

    .rev-item .time {
        color: #999;
        margin-right: 20px
    }

    .rev-item:last-child {
        border-bottom: 0
    }

    .s-star {
        display: block;
        width: 67px;
        height: 13px;
        background: url("../../../static/image/shopping-icons3.png") no-repeat -60px -90px;
        overflow: hidden
    }

    .s-star5 {
        background-position: -61px -90px
    }

    .s-star4 {
        background-position: -74px -90px
    }

    .s-star3 {
        background-position: -87px -90px
    }

    .s-star2 {
        background-position: -101px -90px
    }

    .s-star1 {
        background-position: -114px -90px
    }

    .s-star0 {
        background-position: -128px -90px
    }

    .rev-item .s-star {
        display: inline-block;
        margin: 0 5px;
        vertical-align: -1px;
        *vertical-align: middle
    }

    .rev-item .user {
        float: left;
        margin-left: -70px;
        display: inline;
        text-align: center
    }

    .rev-item .avatar {
        display: block;
        margin-bottom: 5px;
        width: 48px;
        height: 48px;
        border-radius: 50%;
        overflow: hidden
    }

    .rev-item .name {
        font-size: 14px;
        color: #e38d13;
    }

    .rev-txt {
        margin: 8px 0 10px;
        font-size: 14px;
        line-height: 22px
    }
</style>