<template>
    <div>
        <el-carousel :height="height" indicator-position="outside" style="position: relative;">
            <el-carousel-item v-for="(carousel, index) in carousel_list" :key="index">
                <a :href="carousel.link">
                    <img class="carousel-img" :src="carousel.image_url" :alt="carousel.title">
                </a>
                <a :href="carousel.link">
                    <div style="position: absolute; top: 30px; left: 200px;">
                        <p style="color: white; font-size: 25px; font-weight: lighter">{{carousel.created_time}}</p>
                        <p style="color: white; font-size: 25px; font-weight: lighter">{{carousel.remark}}</p>
                    </div>
                </a>
            </el-carousel-item>
        </el-carousel>
        <div style="background-color: rgba(0,0,0,.6);border-radius: 10px;position: absolute; height: 100px; width: 450px; top: 380px; left: 455px;z-index: 9">
            <el-row style="font-size: 24px; margin-top: 10px">
                <el-col :span="18" :offset="3">
                    <el-radio-group v-model="radio" @change="optionChange">
                        <el-radio :label="1" style="color: #e38d13">酒店</el-radio>
                        <el-radio :label="2" style="color: #e38d13">景点</el-radio>
                        <el-radio :label="3" style="color: #e38d13">目的地</el-radio>
                    </el-radio-group>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="16" :offset="1">
                    <el-autocomplete
                            class="inline-input"
                            v-model="state"
                            :fetch-suggestions="querySearch"
                            :placeholder="tips"
                            :trigger-on-focus="false"
                            @select="handleSelect"
                            style="width: 300px"
                    ></el-autocomplete>
                </el-col>
                <el-col :span="1" :offset="1">
                    <el-button type="primary" icon="el-icon-search" @click="search">搜索</el-button>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Carousel",
        data() {
            return {
                height: "",
                carousel_list: [],
                radio: 1,
                state: '',
                tips: '请输入酒店/周边景点',
                search_id: '',
            }
        },
        methods: {
            // 获取首页轮播图数据
            getCarouselList() {
                this.$axios.get(`${this.$settings.HOST}/carousel/`, {}).then(response => {
                    this.carousel_list = response.data;
                }).catch(error => {
                    console.log(error.response);
                })
            },
            getWindowHeight() {
                this.height = window.screen.height * 0.58 + "px";
            },
            querySearch(queryString, cb) {
                let url = "";
                switch (this.radio) {
                    case 1:
                        url = `${this.$settings.HOST}/fuzzy_hotels/`;
                        break;
                    case 2:
                        url = `${this.$settings.HOST}/fuzzy_scenes/`;
                        break;
                    case 3:
                        url = `${this.$settings.HOST}/fuzzy_destinations/`;
                        break;
                }
                this.$axios({
                    url: url,
                    method: "get",
                    params: {
                        search: queryString
                    }
                }).then(response => {
                    let suggestion = [];
                    for (var i = 0; i < response.data.length; i++) {
                        // suggestion[i].value = response.data[i].name;
                        suggestion.push({
                            "value": response.data[i].name + '\xa0\xa0\xa0' + response.data[i].around,
                            "name": response.data[i].name,
                            "id": response.data[i].id
                        })
                    }
                    cb(suggestion);
                }).catch(error => {
                    console.log(error.response)
                });
            },
            handleSelect(item) {
                this.state = item.name;
                this.search_id = item.id;
            },
            optionChange(label) {
                switch (label) {
                    case 1:
                        this.tips = "请输入酒店/周边景点";
                        break;
                    case 2:
                        this.tips = "请输入景点";
                        break;
                    case 3:
                        this.tips = "请输入目的地";
                        break;
                }
            },
            search(){
                let url = '';
                switch (this.radio) {
                    case 1:
                        url = `/hotel/${this.search_id}/`;
                        break;
                    case 2:
                        url = `/scene/${this.search_id}/`;
                        break;
                    case 3:
                        url = `/city/${this.search_id}/`;
                        break;
                }
                this.$router.push(url);
            }
        },
        created() {
            this.getCarouselList();
        },
        beforeMount() {
            this.getWindowHeight();
        }
    }
</script>

<style scoped>
    .el-carousel-item h3 {
        color: #475669;
        font-size: 18px;
        opacity: 0.75;
        line-height: 300px;
        margin: 0;
    }

    .carousel-img {
        width: 100%;
        height: 100%;
    }
</style>