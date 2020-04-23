<template>
    <el-container style="background-color: #f6ffdf">
        <el-main>
            <el-row>
                <el-col :span="2" :offset="6">
                    <h4>迈味旅游</h4>
                </el-col>
                <el-col :span="2">
                    <a href="https://github.com/gaoi311/mytaste" target="_blank"><h4>Github</h4></a>
                </el-col>
                <el-col :span="2">
                    <a href="#" target="_blank"><h4>API文档</h4></a>
                </el-col>
                <el-col :span="2" :offset="2">
                    <a href="#" target="_blank"><h4>使用条款</h4></a>
                </el-col>
                <el-col :span="2">
                    <a href="https://github.com/gaoi311/mytaste" target="_blank"><h4>联系我们</h4></a>
                </el-col>



                <el-col :span="24">
                    <p style="font-size: 14px">Copyright©2019-2020, mytaste.com. All rights reserved. | ICP证：皖xx-xxxxxx</p>
                </el-col>
                <el-col :span="24">
                    <p style="font-size: 14px">皖公网备xxxxxxxxxxxxxxx号</p>
                </el-col>
                <el-col :span="24">
                    <p style="font-size: 12px">违法和不良信息举报电话021-22500846丨安徽省旅游网站落实诚信建设主体责任承诺书</p>
                </el-col>
            </el-row>
        </el-main>
    </el-container>
</template>

<script>
    export default {
        name: "Footer",
        data() {
            return {
            }
        },
        methods: {

        },
        created() {
        }
    }
</script>

<style scoped>
    .el-col{
        text-align: center;
    }

    a{
        text-decoration: none;
    }
    a:visited{
        color: #000;
    }
</style>