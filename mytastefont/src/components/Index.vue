<template>
    <div>
        <Header></Header>
        <el-carousel :height="height" indicator-position="outside">
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

        <div>
            <Footer></Footer>
        </div>
    </div>
</template>

<script>
    import Header from './Header'
    import Footer from './Footer'

    export default {
        name: "Index",
        components: {Header},
        data() {
            return {
                height: "",
                carousel_list: []
            }
        },
        methods: {
            // 获取首页轮播图数据
            getCarouselList() {
                this.$axios.get(`${this.$settings.HOST}/carousel`, {}).then(response => {
                    console.log(response.data);
                    this.carousel_list = response.data;
                }).catch(error => {
                    console.log(error.response);
                })
            },
            getWindowHeight() {
                this.height = window.screen.height * 0.58 + "px";
            }
        },
        created() {
            this.getCarouselList();
        },
        beforeMount() {
            this.getWindowHeight();
        },
        comments: {
            Header,
            Footer
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