<template>
    <el-container>
        <el-header>
            <Header></Header>
        </el-header>
        <el-main>
            <el-row>
                <el-col :span="18" :offset="3">
                    <el-row>
                        <el-col :span="22">
                            <h1>{{scene.name}}</h1>
                        </el-col>
                        <el-row>
                            <el-col :span="22">
                                <p>{{scene.ename}}</p>
                            </el-col>
                            <el-col :span="2">
                                <a href="#">加入收藏</a>
                            </el-col>
                        </el-row>
                    </el-row>
                    <hr>
                    <el-row>
                        <a href="#summary">概括</a><a href="#comment" style="margin-left: 50px">评论</a>
                        <el-button type="primary" size="small" style="float: right;">我要评论</el-button>
                    </el-row>
                    <hr>
                    <el-row>
                        <img src="http://api.mytaste.com:8000//media/scene/%E6%BB%81%E5%B7%9E_%E6%98%8E%E4%B8%AD%E9%83%BD%E7%9A%87%E5%9F%8E%E9%81%97%E5%9D%80.jpg"
                             alt="">
                        <p style="margin-top: 50px">{{scene.summary}}</p>
                    </el-row>
                    <hr>

                    <el-row>
                        <el-col :span="8">
                            <p>电话</p>
                            <p>{{scene.phone}}</p>
                        </el-col>
                        <el-col :span="8">
                            <p>网址</p>
                            <el-link type="primary" :href="scene.website">{{scene.website}}</el-link>
                        </el-col>
                        <el-col :span="8">
                            <p>用时参考</p>
                            <p>{{scene.advice_time}}</p>
                        </el-col>
                    </el-row>
                    <el-row style="margin-top: 20px">
                        <p>{{scene.address}}</p>
                    </el-row>
                    <el-row style="margin-top: 20px">
                        <p>交通</p>
                        <p>{{scene.traffic}}</p>
                    </el-row>
                    <el-row style="margin-top: 20px">
                        <p>开放时间</p>
                        <p>{{scene.open_time}}</p>
                    </el-row>
                    <el-row style="margin-top: 20px">
                        <p>小提示</p>
                        <p>{{scene.tips}}</p>
                    </el-row>
                    <el-row style="margin-top: 20px;font-size: 10px">
                        <p>最后修改时间{{scene.updated_time}}</p>
                    </el-row>
                </el-col>
            </el-row>
        </el-main>
    </el-container>
</template>

<script>
    import Header from '@/components/Common/Header'

    export default {
        name: "Scene",
        data() {
            return {
                scene: null,
                id: 0,
            }
        },
        methods: {
            getScene(id) {
                this.$axios({
                    url: `${this.$settings.HOST}/scene/${id}/`,
                    methods: "GET",
                }).then(response => {
                    this.scene = response.data;
                }).catch(error => {
                    alert(error.response.data);
                })
            }
        },
        created() {
            this.id = this.$route.params.id;
            this.getScene(this.id);
        },
        components: {
            Header
        }
    }
</script>

<style scoped>

</style>