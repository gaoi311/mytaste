<template>
    <el-container>
        <el-header>
            <Header></Header>
        </el-header>
        <el-main id="top">
            <div>
                <el-row>
                    <el-col :span="3" :offset="6">
                        <el-cascader
                                placeholder="地区"
                                :options="options"
                                v-model="address"
                                :props="{expandTrigger: 'hover'}"
                                clearable
                                @change="getHotels"
                        ></el-cascader>
                    </el-col>
                    <el-col :span="3">
                        <el-input
                                placeholder="周边"
                                v-model="aroundValue"
                                @change="getHotels"
                                style="margin-left: 20px;width: 140px"
                                clearable>
                        </el-input>
                    </el-col>
                    <el-col :span="3">
                        <el-select
                                @change="getHotels"
                                v-model="gradeValue"
                                style="margin-left: 20px;"
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
                                @change="getHotels"
                                v-model="orderValue"
                                style="margin-left: 20px;"
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
                     v-for="hotel in hotels" :key="hotel.id">
                    <div class="hotel-pic">
                        <router-link :to="'/hotel/' + hotel.id" target="_blank">
                            <img :src="mainPhotoSrc(hotel.main_photo)"
                                 style="width: 280px;">
                        </router-link>
                    </div>
                    <div class="hotel-title">
                        <div class="title">
                            <h3>
                                <router-link :to="'/hotel/' + hotel.id" target="_blank"
                                             style="font-size: 26px; font-weight: bold">{{hotel.name}}
                                </router-link>
                            </h3>
                            <p>{{hotel.ename}}</p>
                            <br>
                        </div>
                    </div>
                    <div class="hotel-info airbnb-info" style="margin-left: -10px; margin-top: -30px">
                        <ul class="nums clearfix" style="list-style: none; margin-left: -30px">
                            <li>
                                <span>{{grade2Stars(hotel.grade)}}</span>
                            </li>
                            <li class="divide"></li>
                            <li>
                                <span style="font-size: 26px; color: #8166ff">{{hotel.score}}</span>
                            </li>
                            <li>
                                <span style="margin-left: 10px; margin-top: 10px">{{hotel.score_comment}}</span>
                            </li>
                        </ul>
                        <p style="margin-left: 10px">价格 ￥<span
                                style="font-size: 24px;color: #c0a16b">{{hotel.price}}</span></p>
                        <div class="location" style="margin-left: 8px;margin-top: 15px">
                            <i class="el-icon-location"></i><span>{{hotel.around}}</span>
                        </div>
                    </div>
                    <div class="hotel-btns">
                        <div class="btn-tel">

                            <el-link class="btn-detail" type="primary" target="_blank"
                                     :href="'/hotel/' + hotel.id + '#comment'">
                                <span>查看评论</span>
                            </el-link>
                        </div>
                    </div>
                    <div class="hotel-btns" style="margin-top: 15px">
                        <div class="btn-tel">
                            <a :href="'/hotel/' + hotel.id" target="_blank">
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
                    :total="hotelsCount"
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
        name: "HotelList",
        data() {
            return {
                id: 0,
                pageSize: 10,
                hotelsCount: 0,
                page: 1,
                hotels: [],
                value: 4.6,

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

                gradeOption: [
                    {value: '2', label: '一星级'},
                    {value: '3', label: '二星级'},
                    {value: '4', label: '三星级'},
                    {value: '5', label: '四星级'},
                    {value: '6', label: '五星级'},
                ],

                orderOption: [
                    {value: 'price', label: '价格最低'},
                    {value: '-score', label: '评分最高'},
                    {value: '-comment_num', label: '评论数最多'},
                ],

                gradeValue: '',
                aroundValue: '',
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
            getHotels() {
                this.$axios({
                    url: `${this.$settings.HOST}/hotelslist/${this.id}/`,
                    method: "GET",
                    params: {
                        page: this.page,
                        page_size: this.pageSize,
                        search_city: this.address[1],
                        hotel_around: this.aroundValue,
                        hotel_grade: this.gradeValue,
                        hotel_order: this.orderValue
                    }
                }).then(response => {
                    this.hotels = response.data.results;
                    this.hotelsCount = response.data.count;
                }).catch(error => {
                    alert(error.response.data);
                })
            },
            handleCurrentChange(page) {
                this.page = page;
                location.href = '#top';
                this.getHotels(this.id);
            },
        },
        created() {
            this.id = this.$route.params.id;
            this.getHotels();
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