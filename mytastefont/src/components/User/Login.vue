<template>
    <el-container>
        <el-main
                style="width: 500px; height: 400px; background-color: #ffffff; border-radius: 5%; position: absolute; z-index: 9"
                class="center-in-center">
            <el-row style="margin-top: 35px">
                <el-col :span="7" :offset="6">
                    <span :class="{active:loginMethod === 0}" style="font-size: 20px; cursor: pointer" @click="switch2Psw">密码登录</span>
                </el-col>
                <el-col :span="7">
                    <span :class="{active: loginMethod === 1}" style="font-size: 20px; cursor: pointer" @click="switch2Sms">验证码登录</span>
                </el-col>
            </el-row>
            <div v-show="activeName === 'first'">
                <el-row style="margin-top: 30px;">
                    <el-col :span="18" :offset="3">
                        <el-input
                                placeholder="手机或邮箱"
                                prefix-icon="el-icon-user"
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
            </div>
            <div v-show="activeName === 'second'">
                <el-row style="margin-top: 30px;">
                    <el-col :span="18" :offset="3">
                        <el-input
                                placeholder="手机号码"
                                prefix-icon="el-icon-user"
                                v-model="username">
                        </el-input>
                    </el-col>
                </el-row>
                <el-row style="margin-top: 20px">
                    <el-col :span="12" :offset="3">
                        <el-input
                                placeholder="验证码"
                                v-model="sms_code">
                        </el-input>
                    </el-col>
                    <el-col :span="3" :offset="1">
                        <el-button type="primary">点击发送</el-button>
                    </el-col>
                </el-row>
            </div>
            <el-row style="margin-top: 30px">
                <el-col :span="18" :offset="3">
                    <div
                            style="color: #fff; border-radius: 5px; font-size: 20px; width: 100%; height: 45px; background-color: #ff9c38;text-align: center; line-height: 45px; cursor: pointer"
                            @click="loginHandler">
                        登录
                    </div>
                </el-col>
            </el-row>
            <el-row style="margin-top: 10px">
                <el-col :span="12" :offset="3">
                    <span>没有账号？</span>
                    <router-link to="/register">点击注册</router-link>
                </el-col>
                <el-col :span="3" :offset="3">
                    <a href="">忘记密码</a>
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
        name: "Login",
        data() {
            return {
                remember: true,
                activeName: 'first',
                username: "",
                password: "",
                sms_code: "",
                loginMethod: 0
            }
        },
        methods: {
            loginHandler() {
                this.$axios({
                    url: `${this.$settings.HOST}/login/`,
                    method: 'POST',
                    data: {
                        username: this.username,
                        password: this.password
                    }
                }).then(response => {
                    if (this.remember) {
                        // 记住登录
                        sessionStorage.clear();
                        localStorage.uavatar = response.data.avatar;
                        localStorage.utoken = response.data.token;
                        localStorage.uid = response.data.id;
                        localStorage.uname = response.data.username;
                    } else {
                        // 未记住登录
                        localStorage.clear();
                        sessionStorage.uavatar = response.data.avatar;
                        sessionStorage.utoken = response.data.token;
                        sessionStorage.uid = response.data.id;
                        sessionStorage.uname = response.data.username;
                    }
                    this.$router.back() || this.$router.push('/');
                }).catch(error => {
                    this.open_error();
                });
            },
            open_error() {
                this.$message.error("亲亲，用户名或密码错误哦！");
            },
            open_success() {
                this.$message.success("登陆成功！");
            },
            switch2Psw() {
                this.activeName = 'first';
                this.loginMethod = 0;
            },
            switch2Sms() {
                this.activeName = 'second';
                this.loginMethod = 1;
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