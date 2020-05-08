<template>
    <el-container>
        <el-main
                style="width: 500px; height: 450px; background-color: #ffffff; border-radius: 5%; position: absolute; z-index: 9"
                class="center-in-center">
            <el-row style="margin-top: 15px">
                <el-col :span="9" :offset="7" style="text-align: center; font-size: 20px" class="active">
                    一键注册迈味旅行
                </el-col>
            </el-row>
            <el-row style="margin-top: 20px;">
                <el-col :span="18" :offset="3">
                    <el-input
                            placeholder="手机"
                            prefix-icon="el-icon-user"
                            @blur="checkPhoneFormat"
                            v-model="username">
                    </el-input>
                </el-col>
            </el-row>
            <el-row style="margin-top: 20px">
                <el-col :span="18" :offset="3">
                    <el-input
                            placeholder="密码"
                            prefix-icon="el-icon-view"
                            v-model="password"
                            show-password>
                    </el-input>
                </el-col>
            </el-row>
            <el-row style="margin-top: 20px">
                <el-col :span="18" :offset="3">
                    <el-input
                            placeholder="确认密码"
                            prefix-icon="el-icon-view"
                            v-model="repassword"
                            show-password>
                    </el-input>
                </el-col>
            </el-row>
            <!--<el-row style="margin-top: 20px">-->
                <!--<el-col :span="12" :offset="3">-->
                    <!--<el-input-->
                            <!--placeholder="验证码"-->
                            <!--v-model="sms_code">-->
                    <!--</el-input>-->
                <!--</el-col>-->
                <!--<el-col :span="3" :offset="1">-->
                    <!--<el-button type="primary" :disabled="disabledClick" @click="getSmsCode">{{sms_text}}</el-button>-->
                <!--</el-col>-->
            <!--</el-row>-->

            <el-row style="margin-top: 30px">
                <el-col :span="18" :offset="3">
                    <div
                            style="color: #fff; border-radius: 5px; font-size: 20px; width: 100%; height: 45px; background-color: #ff9c38;text-align: center; line-height: 45px; cursor: pointer"
                            @click="registerHandler">
                        注册
                    </div>
                </el-col>
            </el-row>
            <el-row style="margin-top: 10px">
                <el-col :span="18" :offset="3">
                    <span>已有账号？</span>
                    <router-link to="/login">点击登录</router-link>
                </el-col>
            </el-row>
        </el-main>
        <div class="fullscreen-bg"
             style="background-image: url('https://images.mafengwo.net/images/signup/wallpaper/46.jpg')">
        </div>
    </el-container>
</template>

<script>
    export default {
        name: "Register",
        data() {
            return {
                username: "",
                password: "",
                repassword: "",
                sms_code: "",

                disabledClick: false,
                sms_text: "点击发送"
            }
        },
        methods: {
            registerHandler() {
                if (this.checkAttrs()) {
                    this.$axios({
                        url: `${this.$settings.HOST}/register/`,
                        method: 'POST',
                        data: {
                            phone: this.username,
                            password: this.password,
                            sms_code: this.sms_code
                        }
                    }).then(response => {
                        localStorage.uid = response.data.id;
                        localStorage.uname = response.data.username;
                        localStorage.utoken = response.data.token;
                        localStorage.uavatar = response.data.avatar;
                        this.openSuccessMessage("注册成功！");
                        this.$router.push("/");
                    }).catch(error => {
                        let message = error.response.data.phone[0];
                        this.openErrorMessage(message);
                    })
                }

            },
            openErrorMessage(message_) {
                this.$message({
                    message: message_,
                    type: 'error',
                    center: true
                });
            },
            openSuccessMessage(message_) {
                this.$message({
                    message: message_,
                    type: 'success',
                    center: true
                });
            },
            getSmsCode() {
                if (!/^1[3456789]\d{9}$/.test(this.username)) {
                    this.openErrorMessage("请输入正确的手机号码！");
                    return false;
                } else {
                    this.$axios({
                        url: `${this.$settings.HOST}/sms/${this.username}/`,
                        method: 'GET',
                    }).then(response => {
                        if (response.data.status === 1) {
                            this.openSuccessMessage(response.data.message);
                            let time = 120;
                            let timer = setInterval(() => {
                                if (time <= 1) {
                                    // 停止倒计时，允许用户点击发送短信
                                    clearInterval(timer);
                                    this.disabledClick = false; // 设置短信发送段的间隔状态为false,允许点击发送短信
                                    this.sms_text = "点击发送";
                                } else {
                                    time--;
                                    this.disabledClick = true;
                                    this.sms_text = `还需要等待${time}秒哦`;
                                }
                            }, 1000);
                        }
                        if (response.data.status === -1) {
                            this.openErrorMessage(response.data.message);
                        }
                        if (response.data.status === -2) {
                            this.openErrorMessage(response.data.message);
                        }
                        if (response.data.status === 101) {
                            this.openErrorMessage(response.data.message);
                        }
                    }).catch(error => {
                        console.log(error.response);
                    })
                }
            },
            checkAttrs() {
                let flag = true;
                if (this.password !== this.repassword) {
                    this.openErrorMessage("两次密码不一样哦！");
                    flag = false;
                }
                return flag;
            },
            checkPhoneFormat() {
                var reg = /^1[3456789]\d{9}$/;
                if (!reg.test(this.username)) {
                    this.openErrorMessage('请输入正确的手机号码！');
                }
            }
        }
    }
</script>

<style scoped>
    .center-in-center {
        position: absolute;
        top: 45%;
        left: 50%;
        -webkit-transform: translate(-50%, -50%);
        -moz-transform: translate(-50%, -50%);
        -ms-transform: translate(-50%, -50%);
        -o-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
    }

    .fullscreen-bg {
        background-position: 50% 50%;
        background-size: cover;
        bottom: 0;
        right: 0;
        position: fixed;
        position: absolute \9;
        width: 100% \9;
        height: 100% \9;
        overflow: hidden;
        left: 0;
        top: 0;
    }

    .active {
        padding-bottom: 5px;
        border-bottom: 5px solid #ff9c38;
        border-radius: 2px;
    }
</style>