<template>
    <el-container>
        <el-header>
            <Header></Header>
        </el-header>
        <el-main>
            <el-row>
                <el-col class="title" :span="24">
                    <h2>热门目的地</h2>
                </el-col>
            </el-row>
            <el-row style="font-size: 18px">
                <el-col :span="6" :offset="9">
                    <el-tabs v-model="activeName" @tab-click="handleClick">
                        <el-tab-pane label="国内" name="first"></el-tab-pane>
                        <el-tab-pane label="港澳台" name="second"></el-tab-pane>
                        <el-tab-pane label="东南亚" name="third"></el-tab-pane>
                        <el-tab-pane label="欧洲" name="fourth"></el-tab-pane>
                        <el-tab-pane label="美洲" name="fifth"></el-tab-pane>
                    </el-tabs>
                </el-col>
            </el-row>

            <div style="margin-left: 12%; margin-top: -20px">
                <div class="row row-hot">
                    <div v-if="activeName === 'first'" class="hot-list clearfix">
                        <div class="col">
                            <dl>
                                <dt>直辖市</dt>
                                <dd>
                                    <a href="/city/1/" target="_blank">北京</a>
                                    <a href="/city/3/" target="_blank">上海</a>

                                    <a href="/city/4/" target="_blank">重庆</a>
                                    <a href="/city/2/" target="_blank">天津</a>
                                </dd>
                            </dl>
                            <dl>
                                <dt><a href="/city/1" target="_blank">云南</a></dt>
                                <dd>
                                    <a href="/city/301/" target="_blank">丽江</a>
                                    <a href="/city/298/" target="_blank">玉溪</a>
                                    <a href="/city/296/" target="_blank">昆明</a>
                                    <a href="/city/1" target="_blank">香格里拉</a>
                                    <a href="/city/1" target="_blank">泸沽湖</a>
                                    <a href="/city/1" target="_blank">双廊</a>
                                    <a href="/city/1" target="_blank">西双版纳</a>
                                    <a href="/city/1" target="_blank">束河</a>
                                    <a href="/city/1" target="_blank">腾冲</a>
                                    <a href="/city/1" target="_blank">雨崩</a>
                                </dd>
                            </dl>
                            <dl>
                                <dt><a href="/city/1" target="_blank">四川</a></dt>
                                <dd>
                                    <a href="/city/248/" target="_blank">成都</a>
                                    <a href="/city/252/" target="_blank">绵阳</a>
                                    <a href="/city/257/" target="_blank">乐山</a>
                                    <a href="/city/266/" target="_blank">阿坝藏族羌族自治州</a>
                                    <a href="/city/267/" target="_blank">甘孜藏族自治州</a>
                                    <!--<a href="/city/1" target="_blank">都江堰</a>-->
                                    <!--<a href="/city/1" target="_blank">亚丁</a>-->
                                    <!--<a href="/city/1" target="_blank">阿坝</a>-->
                                    <!--<a href="/city/1" target="_blank">峨眉山</a>-->
                                    <!--<a href="/city/1" target="_blank">牛背山</a>-->
                                </dd>
                            </dl>
                            <dl>
                                <dt><a href="/city/1" target="_blank">浙江</a></dt>
                                <dd>
                                    <a href="/city/99/" target="_blank">杭州</a>
                                    <a href="/city/102/" target="_blank">嘉兴</a>
                                    <a href="/city/107/" target="_blank">舟山</a>
                                    <a href="/city/108/" target="_blank">台州</a>
                                    <!--<a href="/city/1" target="_blank">普陀山</a>-->
                                    <!--<a href="/city/1" target="_blank">东极岛</a>-->
                                    <!--<a href="/city/1" target="_blank">南浔</a>-->
                                </dd>
                            </dl>
                            <dl>
                                <dt>
                                    <a href="/city/1" target="_blank">海南</a>
                                    <a href="/city/1" target="_blank">福建</a></dt>
                                <dd>
                                    <a href="/city/279/" target="_blank">三亚</a>
                                    <a href="/city/1278/" target="_blank">海口</a>
                                    <a href="/city/283/" target="_blank">文昌</a>
                                    <a href="/city/128/" target="_blank">厦门</a>
                                    <a href="/city/127/" target="_blank">福州</a>
                                    <!--<a href="/city/1" target="_blank">武夷山</a>-->
                                    <a href="/city/131/" target="_blank">泉州</a>
                                </dd>
                            </dl>
                            <dl>
                                <dt>
                                    <a href="/city/1" target="_blank">江苏</a>
                                </dt>
                                <dd>
                                    <a href="/city/86/" target="_blank">南京</a>
                                    <a href="/city/90/" target="_blank">苏州</a>
                                    <a href="/city/87/" target="_blank">无锡</a>
                                    <a href="/city/95/" target="_blank">扬州</a>
                                    <a href="/city/89" target="_blank">常州</a>
                                    <a href="/city/92/" target="_blank">连云港</a>
                                    <a href="/city/88/" target="_blank">徐州</a>
                                </dd>
                            </dl>
                            <dl>
                                <dt>
                                    <a href="/city/1" target="_blank">广东</a>
                                    <a href="/city/1" target="_blank">广西</a>
                                </dt>
                                <dd>
                                    <a href="/city/213/" target="_blank">广州</a>
                                    <a href="/city/214/" target="_blank">深圳</a>
                                    <a href="/city/215/" target="_blank">珠海</a>
                                    <a href="/city/216/" target="_blank">汕头</a>
                                    <a href="/city/218/" target="_blank">佛山</a>
                                    <a href="/city/331/" target="_blank">桂林</a>
                                    <a href="/city/338/" target="_blank">玉林</a>
                                    <a href="/city/339/" target="_blank">百色</a>
                                    <!--<a href="/city/1" target="_blank">黄姚古镇</a>-->
                                    <!--<a href="/city/1" target="_blank">涠洲岛</a>-->
                                    <!--<a href="/city/1" target="_blank">龙脊梯田</a>-->
                                </dd>
                            </dl>
                        </div>
                        <div class="col">
                            <dl>
                                <dt>
                                    <a href="/city/1" target="_blank">西藏</a>
                                    <a href="/city/1" target="_blank">贵州</a>
                                </dt>
                                <dd>
                                    <a href="/city/344/" target="_blank">拉萨</a>
                                    <a href="/city/350" target="_blank">林芝</a>
                                    <a href="/city/349/" target="_blank">阿里</a>
                                    <a href="/city/276/" target="_blank">黔东南</a>
                                    <a href="/city/277/" target="_blank">黔南</a>
                                    <a href="/city/271/" target="_blank">遵义</a>
                                    <a href="/city/269/" target="_blank">贵阳</a>
                                    <!--<a href="/city/1" target="_blank">黄果树</a>-->
                                </dd>
                            </dl>
                            <dl>
                                <dt>
                                    <a href="/city/1" target="_blank">西北</a>
                                </dt>
                                <dd>
                                    <a href="/city/320/" target="_blank">西安</a>
                                    <a href="/city/323/" target="_blank">咸阳</a>
                                    <a href="/city/312/" target="_blank">西宁</a>
                                    <!--<a href="/city/1" target="_blank">祁连</a>-->
                                    <!--<a href="/city/1" target="_blank">敦煌</a>-->
                                    <a href="/city/234/" target="_blank">兰州</a>
                                    <a href="/city/240/" target="_blank">张掖</a>
                                    <a href="/city/238/" target="_blank">嘉峪关</a>
                                    <a href="/city/242/" target="_blank">酒泉</a>
                                    <a href="/city/356/" target="_blank">乌鲁木齐</a>
                                    <a href="/city/362/" target="_blank">吐鲁番</a>
                                </dd>
                            </dl>
                            <dl>
                                <dt>
                                    <a href="/city/1" target="_blank">山东</a>
                                    <a href="/city/1" target="_blank">山西</a>
                                </dt>
                                <dd>
                                    <a href="/city/148/" target="_blank">青岛</a>
                                    <a href="/city/147/" target="_blank">济南</a>
                                    <a href="/city/157/" target="_blank">日照</a>
                                    <a href="/city/156/" target="_blank">威海</a>
                                    <a href="/city/152/" target="_blank">烟台</a>
                                    <!--<a href="/city/1" target="_blank">长岛</a>-->
                                    <a href="/city/16/" target="_blank">太原</a>
                                    <a href="/city/22/" target="_blank">晋中</a>
                                    <!--<a href="/city/1" target="_blank">大同</a>-->
                                    <!--<a href="/city/1" target="_blank">五台山</a>-->
                                    <!--<a href="/city/1" target="_blank">壶口瀑布</a>-->
                                </dd>
                            </dl>
                            <dl>
                                <dt>
                                    <a href="/city/1" target="_blank">湖南</a>
                                    <a href="/city/1" target="_blank">湖北</a>
                                </dt>
                                <dd>
                                    <a href="/city/206/" target="_blank">张家界</a>
                                    <a href="/city/212/" target="_blank">湘西土家族苗族自治州</a>
                                    <a href="/city/182/" target="_blank">武汉</a>
                                    <a href="/city/198/" target="_blank">恩施</a>
                                    <a href="/city/197/" target="_blank">神农架</a>
                                    <a href="/city/186/" target="_blank">宜昌</a>
                                </dd>
                            </dl>
                            <dl>
                                <dt>
                                    <a href="/city/1" target="_blank">安徽</a>
                                    <a href="/city/1" target="_blank">江西</a>
                                </dt>
                                <dd>
                                    <a href="/city/118/" target="_blank">黄山</a>
                                    <a href="/city/117/" target="_blank">安庆</a>
                                    <a href="/city/136/" target="_blank">南昌</a>
                                    <a href="/city/137/" target="_blank">景德镇</a>
                                    <a href="/city/142/" target="_blank">赣州</a>
                                    <a href="/city/143/" target="_blank">吉安</a>
                                    <!--<a href="/city/1" target="_blank">南昌</a>-->
                                </dd>
                            </dl>
                            <dl>
                                <dt>
                                    <a href="/city/1" target="_blank">河北</a>
                                    <a href="/city/1" target="_blank">河南</a>
                                </dt>
                                <dd>
                                    <a href="/city/5/" target="_blank">石家庄</a>
                                    <a href="/city/7/" target="_blank">秦皇岛</a>
                                    <a href="/city/12/" target="_blank">承德</a>
                                    <a href="/city/164/" target="_blank">郑州</a>
                                    <a href="/city/166/" target="_blank">洛阳</a>
                                    <a href="/city/165/" target="_blank">开封</a>
                                    <a href="/city/175/" target="_blank">三门峡</a>
                                </dd>
                            </dl>
                            <dl>
                                <dt>
                                    <a href="/city/1" target="_blank">内蒙古</a>
                                    <a href="/city/1" target="_blank">东北</a>
                                </dt>
                                <dd>
                                    <a href="/city/384/" target="_blank">呼伦贝尔</a>
                                    <a href="/city/383/" target="_blank">鄂尔多斯</a>
                                    <a href="/city/386/" target="_blank">乌兰察布</a>
                                    <a href="/city/389/" target="_blank">阿拉善</a>
                                    <a href="/city/73/" target="_blank">哈尔滨</a>
                                    <a href="/city/83/" target="_blank">黑河</a>
                                    <a href="/city/64/" target="_blank">长春</a>
                                    <a href="/city/51/" target="_blank">大连</a>
                                    <a href="/city/55/" target="_blank">丹东</a>
                                    <a href="/city/60/" target="_blank">盘锦</a>
                                </dd>
                            </dl>
                        </div>
                    </div>
                    <div v-if="activeName === 'second'" class="hot-list clearfix">
                        <div class="col">
                            <dl>
                                <dt><a href="/city/1" target="_blank">台湾</a></dt>
                                <dd>
                                    <a href="/city/27/" target="_blank">台北</a>
                                    <a href="/city/31/" target="_blank">台南</a>
                                    <a href="/city/49/" target="_blank">花莲</a>
                                    <a href="/city/28/" target="_blank">高雄</a>
                                    <a href="/city/30/" target="_blank">台中</a>
                                    <a href="/city/34/" target="_blank">新北</a>
                                    <a href="/city/41/" target="_blank">南投</a>
                                </dd>
                            </dl>
                        </div>
                        <div class="col">
                            <dl>
                                <dt>
                                    <a href="/city/391/" target="_blank">香港</a>
                                    <a href="/city/390/" target="_blank">澳门</a>
                                </dt>
                            </dl>
                        </div>
                    </div>
                </div>
            </div>
        </el-main>
        <el-main>
            <el-row>
                <el-col class="title" :span="24">
                    <h2>主题精选</h2>
                </el-col>
            </el-row>
            <el-row style="font-size: 18px">
                <el-col class="title" :span="1" :offset="8">
                    <a href="">人文</a>
                </el-col>
                <el-col class="title" :span="0.5">
                    <p class="divide">|</p>
                </el-col>
                <el-col class="title" :span="1">
                    <a href="">自然</a>
                </el-col>
                <el-col class="title" :span="0.5">
                    <p class="divide">|</p>
                </el-col>
                <el-col class="title" :span="1">
                    <a href="">历史</a>
                </el-col>
                <el-col class="title" :span="0.5">
                    <p class="divide">|</p>
                </el-col>
                <el-col class="title" :span="1">
                    <a href="">建筑</a>
                </el-col>
                <el-col class="title" :span="0.5">
                    <p class="divide">|</p>
                </el-col>
                <el-col class="title" :span="1">
                    <a href="">网红</a>
                </el-col>
                <el-col class="title" :span="0.5">
                    <p class="divide">|</p>
                </el-col>
                <el-col class="title" :span="1">
                    <a href="">购物</a>
                </el-col>
                <el-col class="title" :span="0.5">
                    <p class="divide">|</p>
                </el-col>
                <el-col class="title" :span="1">
                    <a href="">小吃</a>
                </el-col>
            </el-row>
        </el-main>
    </el-container>
</template>

<script>
    import Header from "@/components/Common/Header";

    export default {
        name: "Destination",
        data() {
            return {
                activeName: 'first',
            }
        },
        methods: {
            headerValue(val) {
                this.activeIndex = val;
            }
        },
        components: {
            Header
        }
    }
</script>

<style scoped>
    .title {
        text-align: center;
    }

    .divide {
        display: inline-block;
        margin-top: 3px;
        width: 1px;
        height: 15px;
        background-color: #eee;
        overflow: hidden;
        line-height: 100px;
        vertical-align: top;
    }

    .hot-list {
        line-height: 24px;
        font-size: 14px;
    }

    .hot-list .col {
        float: left;
        width: 470px;
    }

    .hot-list .col + .col {
        margin-left: 60px;
    }

    .hot-list dl {
        border-bottom: 1px dashed #eee;
        padding: 20px 0 20px 100px;
    }

    .hot-list dl:last-child {
        border-bottom: 0 none;
        padding-bottom: 0;
    }

    .hot-list dt {
        float: left;
        font-size: 16px;
        color: #333;
        margin-left: -100px;
    }

    .hot-list dt a {
        color: #333;
        text-decoration: underline
    }

    .hot-list dd a {
        margin-right: 10px;
        color: #666;
    }

    .hot-list a:hover {
        color: #ff8a00
    }

    .row {
        padding: 40px 0;
    }

    .row-hot {
        margin: 0 0 50px;
    }
</style>