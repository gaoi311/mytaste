<template>
    <div class="container" style="background-color: #fbffc0; margin-bottom: 10px">
        <div class="row">
            <div class="col-md-9 col-lg-offset-3">
                <h3>省内游 | 畅享娱乐</h3>
            </div>
        </div>
        <div class="row">
            <div class="col-md-3">
                <ul>
                    <li>1</li>
                    <li>2</li>
                    <li>3</li>
                    <li>4</li>
                    <li>5</li>
                    <li>6</li>
                </ul>
            </div>
            <div class="col-md-3" v-for="scene in provinceSceneList" :key="scene.id"
                 :style="{width: '220px', marginRight: '-10px'}">
                <router-link :to="'/scene/' + scene.id" target="_blank">
                    <div class="thumbnail">
                        <img :src="mainPhotoSrc(scene.main_photo)"
                             style="height: 100%; width: 100%; display: block;">
                        <div class="caption">
                            <p style="font-size: 12px">{{scene.name}}</p>
                            <p>热度：{{scene.hot}}</p>
                            <p>{{scene.city.name}}</p>
                        </div>
                    </div>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ProvinceTravelModule",
        data() {
            return {
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
                    methods: "GET",
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
            // getImageSrc(filePath){
            //     return
            // }
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

</style>