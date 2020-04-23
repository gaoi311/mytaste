<template>
    <div class="login">
        <div class="vertical-center pdt" style="margin-top: 9%;">
            <div class="container login-container">
                <div class="row">
                    <div class="col-sm-5 col-xs-12">
                        <div class="login-form">
                            <a href="http://www.mytaste.com">
                                <img class="logo" src="https://a.hecdn.net/img/sso/1/logo.png">
                                <img class="logo logo-white" src="https://a.hecdn.net/img/sso/1/logo-white.png">
                            </a>
                            <form class="form-horizontal">
                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-sm-4">
                                            <h1>登录</h1>
                                        </div>
                                        <div class="col-xs-8 input hidden-xs tip-container" style="display: none">
                                            <div class="tip text-center">
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <div class="form-group">
                                    <div class="line">
                                        <div class="row">
                                            <label class="col-xs-3 control-label text-left"
                                                   for="username">手机号码</label>
                                            <div class="col-xs-9 input">
                                                <input id="username" v-model="username" type="text" class="form-control"
                                                       value=""
                                                       maxlength="60" autofocus>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <div class="line">
                                        <div class="row">
                                            <label class="col-xs-3 control-label text-left"
                                                   for="password">输入密码</label>
                                            <div class="col-xs-9 input">
                                                <input id="password" v-model="password" type="password"
                                                       class="form-control" value=""
                                                       maxlength="30">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!--<div class="drag">-->
                                    <!--<div class="bg"></div>-->
                                    <!--<div class="text" onselectstart="return false;">请拖动滑块解锁</div>-->
                                    <!--<div class="btn">&gt;&gt;</div>-->
                                <!--</div>-->

                                <!--<div id="your-dom-id" class="nc-container"></div>-->
                                <!--<div class="form-group tip-container hidden-sm hidden-md hidden-lg"-->
                                     <!--style="display: none;">-->
                                    <!--<div class="col-sm-12">-->
                                        <!--<div class="tip text-center">-->
                                        <!--</div>-->
                                    <!--</div>-->
                                <!--</div>-->
                                <div class="form-group">
                                    <button id="submitForm" @click="loginHandler" type="button" class="btn btn-block">登&nbsp;录</button>
                                </div>
                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-xs-7 text-left">
                                            <div class="account">
                                                <span>没有账号?</span>
                                                <router-link to="/register">点击免费注册</router-link>
                                            </div>
                                        </div>
                                        <div class="col-xs-5">
                                            <a href="https://www.mytaste.com/forget"
                                               class="company">忘记密码</a>
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                    <div class="col-sm-7 hidden-xs" style="cursor: pointer" @click="clickToIndex">
                        <div class="decoration">
                            <div class="row">
                                <div class="col-sm-8 text-right">
                                    <img class="phone" src="https://a.hecdn.net/img/sso/1/phone.png">
                                </div>
                                <div class="col-sm-4">
                                    <div class="qr-code-container">
                                        <img class="qr-code" src="https://a.hecdn.net/img/sso/1/qr-code.png">
                                        <p>扫码下载</p>
                                        <h3>下载和风天气<br>官方APP</h3>
                                        <p>全球可视化天气APP</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div style="padding-bottom: 20px;">
            <div class="footer-company text-center visible-xs">
                <a href="http://www.mytaste.com/">迈味旅游服务条款</a>
            </div>
            <div class="footer-copyright text-center">
                © 2020 迈味旅游版权所有 京ICP备14028982号-1
            </div>
        </div>
        <el-button :plain="true" @click="open_error" style="display: none">错误</el-button>
        <el-button :plain="true" @click="open_success" style="display: none">成功</el-button>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                remember: false,
                username: "",
                password: "",
            }
        },
        methods: {
            loginHandler() {
                this.$axios({
                    url: `${this.$settings.HOST}/login/`,
                    methods: 'POST',
                    data: {
                        username: this.username,
                        password: this.password
                    }
                }).then(response=>{
                    if (this.remember) {
                        // 记住登录
                        sessionStorage.clear();
                        localStorage.avator = response.data.avator;
                        localStorage.token = response.data.token;
                        localStorage.id = response.data.id;
                        localStorage.username = response.data.username;
                    } else {
                        // 未记住登录
                        localStorage.clear();
                        sessionStorage.avator = response.data.avator;
                        sessionStorage.token = response.data.token;
                        sessionStorage.id = response.data.id;
                        sessionStorage.username = response.data.username;
                    }
                    this.$router.go(-1);
                }).catch(error=>{
                    this.open_error();
                });
            },
            open_error() {
                this.$message.error("亲亲，用户名或密码错误哦！");
            },
            open_success() {
                this.$message.success("登陆成功！");
            },
            clickToIndex() {
                this.$router.push('/');
            }
        }
    }
</script>

<style scoped>
    .login {
        background-size: cover;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url("http://attach.bbs.miui.com/forum/201112/14/223055hvzi1h6frov6o9fc.jpg") no-repeat center center;
    }
</style>