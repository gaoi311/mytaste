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
                                                   for="phone">手机号码</label>
                                            <div class="col-xs-9 input">
                                                <input id="phone" v-model="phone" type="text" class="form-control"
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

    // var $ = function (selector) {
    //         return document.querySelector(selector);
    //     },
    //     box = $(".drag"),//容器
    //     bg = $(".bg"),//背景
    //     text = $(".text"),//文字
    //     btn = $(".btn"),//滑块
    //     success = false,//是否通过验证的标志
    //     distance = box.offsetWidth - btn.offsetWidth;//滑动成功的宽度（距离）
    //
    // //二、给滑块注册鼠标按下事件
    // btn.onmousedown = function (e) {
    //
    //     //1.鼠标按下之前必须清除掉后面设置的过渡属性
    //     btn.style.transition = "";
    //     bg.style.transition = "";
    //
    //     //说明：clientX 事件属性会返回当事件被触发时，鼠标指针向对于浏览器页面(或客户区)的水平坐标。
    //
    //     //2.当滑块位于初始位置时，得到鼠标按下时的水平位置
    //     var e = e || window.event;
    //     var downX = e.clientX;
    //
    //     //三、给文档注册鼠标移动事件
    //     document.onmousemove = function (e) {
    //
    //         var e = e || window.event;
    //         //1.获取鼠标移动后的水平位置
    //         var moveX = e.clientX;
    //
    //         //2.得到鼠标水平位置的偏移量（鼠标移动时的位置 - 鼠标按下时的位置）
    //         var offsetX = moveX - downX;
    //
    //         //3.在这里判断一下：鼠标水平移动的距离 与 滑动成功的距离 之间的关系
    //         if (offsetX > distance) {
    //             offsetX = distance;//如果滑过了终点，就将它停留在终点位置
    //         } else if (offsetX < 0) {
    //             offsetX = 0;//如果滑到了起点的左侧，就将它重置为起点位置
    //         }
    //
    //         //4.根据鼠标移动的距离来动态设置滑块的偏移量和背景颜色的宽度
    //         btn.style.left = offsetX + "px";
    //         bg.style.width = offsetX + "px";
    //
    //         //如果鼠标的水平移动距离 = 滑动成功的宽度
    //         if (offsetX == distance) {
    //
    //             //1.设置滑动成功后的样式
    //             text.innerHTML = "验证通过";
    //             text.style.color = "#fff";
    //             btn.innerHTML = "&radic;";
    //             btn.style.color = "green";
    //             bg.style.backgroundColor = "lightgreen";
    //
    //             //2.设置滑动成功后的状态
    //             success = true;
    //             //成功后，清除掉鼠标按下事件和移动事件（因为移动时并不会涉及到鼠标松开事件）
    //             btn.onmousedown = null;
    //             document.onmousemove = null;
    //
    //             //3.成功解锁后的回调函数
    //             setTimeout(function () {
    //                 alert('解锁成功！');
    //             }, 100);
    //         }
    //     }
    //
    //     //四、给文档注册鼠标松开事件
    //     document.onmouseup = function (e) {
    //
    //         //如果鼠标松开时，滑到了终点，则验证通过
    //         if (success) {
    //             return;
    //         } else {
    //             //反之，则将滑块复位（设置了1s的属性过渡效果）
    //             btn.style.left = 0;
    //             bg.style.width = 0;
    //             btn.style.transition = "left 1s ease";
    //             bg.style.transition = "width 1s ease";
    //         }
    //         //只要鼠标松开了，说明此时不需要拖动滑块了，那么就清除鼠标移动和松开事件。
    //         document.onmousemove = null;
    //         document.onmouseup = null;
    //     }
    //
    //
    // }

    export default {
        name: "Login",
        data() {
            return {
                phone: "",
                password: "",
            }
        },
        methods: {
            loginHandler() {
                this.$axios({
                    url: `${this.$settings.HOST}/login/`,
                    method: 'POST',
                    data: {
                        phone: this.phone,
                        password: this.password
                    }
                }).then(response => {
                    this.open_success();
                    this.$router.push("/");
                }).catch(error => {
                    this.open_error();
                    console.log(error.response);
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