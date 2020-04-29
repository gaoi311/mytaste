<template>
    <el-container>
        <el-header>
            <Header></Header>
        </el-header>
        <el-main style="margin-left: 35%; width: 30%;margin-top: 50px">
            <el-form :model="form" :rules="rules" ref="form" label-width="100px" class="demo-ruleForm">
                <el-form-item label="用户名" prop="username">
                    <el-input v-model="form.username"></el-input>
                </el-form-item>

                <el-form-item label="性别" prop="resource">
                    <el-radio-group v-model="form.gender">
                        <el-radio :label="item.value" :key="item.value" v-for="item in genderOption">{{item.label}}
                        </el-radio>
                    </el-radio-group>
                </el-form-item>

                <el-form-item label="生日">
                    <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="form.birth"
                                    placeholder="选择日期"></el-date-picker>
                </el-form-item>


                <el-form-item label="详细地址">
                    <el-input v-model="form.address"></el-input>
                </el-form-item>

                <el-form-item label="邮箱">
                    <el-input v-model="form.email"></el-input>
                </el-form-item>

                <el-form-item>
                    <el-button @click="updateInfo" style="width: 100%" type="primary">修改</el-button>
                </el-form-item>
            </el-form>
        </el-main>
    </el-container>
</template>

<script>
    import Header from "@/components/Common/Header";

    export default {
        name: "UserInfo",
        data() {
            return {
                uid: 0,
                user: undefined,
                form: {
                    username: '',
                    gender: '',
                    birth: '',
                    address: '',
                    email: '',
                },
                rules: {
                    username: [
                        {required: true, message: '用户名不能为空', trigger: 'blur'},
                    ],
                },
                genderOption: [
                    {label: "男", value: 1},
                    {label: "女", value: 2},
                    {label: "保密", value: 3}
                ],
            }
        },
        methods: {
            getUserInfo(id) {
                this.$axios({
                    url: `${this.$settings.HOST}/user/info/${id}/`,
                    method: 'GET',
                }).then(response => {
                    this.user = response.data;
                    this.form.username = this.user.username;
                    this.form.gender = this.user.gender;
                    this.form.birth = this.user.birth;
                    this.form.address = this.user.address;
                    this.form.email = this.user.email;
                }).catch(error => {
                    alert(error.response);
                })
            },
            updateInfo() {
                this.$axios({
                    url: `${this.$settings.HOST}/user/info/${this.uid}/`,
                    method: 'PUT',
                    data: {
                        username: this.form.username,
                        gender: this.form.gender,
                        birth: this.form.birth,
                        address: this.form.address,
                        email: this.form.email
                    }
                }).then(response => {
                    this.$message.success('修改成功！');
                    this.$router.push('/self');
                }).catch(error => {
                    let message = "";
                    for (let key in error.response.data) {
                        message = error.response.data[key][0];
                    }
                    this.$message.error(message);
                })
            }
        },
        created() {
            this.uid = localStorage.uid;
            this.getUserInfo(this.uid);
        },
        components: {
            Header,
        },

    }
</script>

<style scoped>
    .avatar-uploader .el-upload {
        border: 1px dashed #d9d9d9;
        border-radius: 6px;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }

    .avatar-uploader .el-upload:hover {
        border-color: #409EFF;
    }

    .avatar-uploader-icon {
        font-size: 28px;
        color: #8c939d;
        width: 178px;
        height: 178px;
        line-height: 178px;
        text-align: center;
    }

    .avatar {
        width: 178px;
        height: 178px;
        display: block;
    }
</style>