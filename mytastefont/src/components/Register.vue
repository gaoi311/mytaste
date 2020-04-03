<template>
    <div class="register1">
        <div class="vertical-center pdt" style="margin-top: 7%;">
            <div class="container login-container register">
                <div class="row">
                    <div class="col-sm-12">
                        <div class="login-form">
                            <router-link to="/">
                                <img class="logo" src="https://a.hecdn.net/img/sso/1/logo.png">
                                <img class="logo logo-white" src="https://a.hecdn.net/img/sso/1/logo-white.png">
                            </router-link>
                            <form class="form-horizontal">
                                <div class="form-group">
                                    <div class="row">
                                        <div class="col-sm-4">
                                            <h1>注册</h1>
                                        </div>
                                        <div class="col-sm-8 hidden-xs">
                                            <div class="account text-right" style="padding: 10px 0">
                                                <span>已有账号?</span>
                                                <router-link to="/login">点击登录</router-link>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <div class="line">
                                        <div class="row">
                                            <label class="col-xs-3 control-label text-left" for="phone">手机号码</label>
                                            <div class="col-xs-9 input">
                                                <input id="phone" v-model="phone" type="text" class="form-control" maxlength="60"
                                                       value="" autofocus>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <div class="line">
                                        <div class="row">
                                            <label class="col-xs-3 control-label text-left" for="password">设置密码</label>
                                            <div class="col-xs-9 input">
                                                <input id="password" v-model="password" type="password" maxlength="20" class="form-control"
                                                       value="">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <div class="line">
                                        <div class="row">
                                            <label class="col-xs-3 control-label text-left" for="password">重复密码</label>
                                            <div class="col-xs-9 input">
                                                <input id="repassword" v-model="repassword" type="password" maxlength="20"
                                                       class="form-control" value="">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <div class="row">
                                        <div class=" col-sm-12">
                                            <div id="slider" class="dragdealer">
                                                <div class="handle"
                                                     style="perspective: 1000px; backface-visibility: hidden; transform: translateX(0px); border-color: rgb(236, 236, 236);">
                                                    <div class="doing">
                                                        <span class="glyphicon glyphicon-menu-right"></span>
                                                        <span class="glyphicon glyphicon-menu-right"></span>
                                                    </div>
                                                    <div class="done hidden">
                                                        <span class="glyphicon glyphicon-ok"></span>
                                                    </div>
                                                </div>
                                                <div class="mask" style="width: 0%;"></div>
                                                <span class="handler-information">向右滑动验证</span>
                                                <span class="handler-information handle-success hidden">验证通过</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="form-group tip-container" style="display: none;">
                                    <div class="col-sm-12">
                                        <div class="tip text-center">
                                        </div>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <button id="submitForm" @click="registerHandler" type="button" class="btn btn-block">同意服务条款并提交注册</button>
                                </div>
                                <div class="form-group">
                                    <div class="row">
                                        <!--<div class="col-sm-12 visible-xs">-->
                                            <!--<div class="account text-center">-->
                                                <!--<span>已有账号?</span>-->
                                                <!--<a href="https://id.heweather.com/login?redirect=https://console.heweather.com">点击登录</a>-->
                                            <!--</div>-->
                                        <!--</div>-->
                                        <div class="col-sm-12 input hidden-xs">
                                            <!--<a href="https://www.heweather.com/terms/tos" class="company">迈味旅游服务条款</a>-->
                                            <router-link to="/" class="company">迈味旅游服务条款</router-link>
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div style="padding-bottom: 20px;">
            <div class="footer-company text-center visible-xs">
                <a href="https://www.heweather.com/">迈味旅游服务条款</a>
            </div>
            <div class="footer-copyright text-center">
                © 2020 迈味旅游版权所有 皖ICP备14028982号-1
            </div>
        </div>
        <el-button :plain="true" @click="open_error" style="display: none">错误</el-button>
        <el-button :plain="true" @click="open_success" style="display: none">成功</el-button>
    </div>
</template>

<script>
    export default {
        name: "Register",
        data(){
            return {
                phone: "",
                password: "",
                repassword: ""
            }
        },
        methods:{
            registerHandler(){
                console.log(this.phone + this.password);
                if (this.password === this.repassword){
                    this.$axios({
                        url: `${this.$settings.HOST}/register/`,
                        method: "POST",
                        data: {
                            phone: this.phone,
                            password: this.password
                        }
                    }).then(response=>{
                        if (response.data.ok) {
                            this.open_success();
                            this.$router.push('/');
                        }else {
                            this.open_error("亲亲，该手机号已经有人注册了哦！");
                        }
                    }).catch(error=>{
                        console.log(error.response);
                    })
                } else {
                    this.open_error("亲亲，两次密码不一样哦！")
                }
            },
            open_error(message) {
                this.$message.error(message);
            },
            open_success() {
                this.$message.success("注册成功！");
            },
        }
    }
</script>

<style scoped>
    .register1 {
        background-size: cover;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url("http://attach.bbs.miui.com/forum/201112/14/223055hvzi1h6frov6o9fc.jpg") no-repeat center center;
    }
</style>