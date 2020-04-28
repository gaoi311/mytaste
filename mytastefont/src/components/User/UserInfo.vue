<template>
    <el-container>
        <el-header>
            <Header></Header>
        </el-header>
        <el-main style="margin-left: 25%; width: 50%;margin-top: 50px">
            <el-form :model="form" :rules="rules" ref="form" label-width="100px" class="demo-ruleForm">
                <el-form-item label="用户名" prop="name">
                    <el-input v-model="form.username"></el-input>
                </el-form-item>

                <el-form-item label="性别" prop="resource">
                    <el-radio-group v-model="form.gender">
                        <el-radio :label="item.value" :key="item.value" v-for="item in genderOption">{{item.label}}</el-radio>
                    </el-radio-group>
                </el-form-item>

                <el-form-item label="生日">
                    <el-date-picker type="date" placeholder="选择日期"></el-date-picker>
                </el-form-item>

                <el-form-item label=""></el-form-item>
                    <el-cascader></el-cascader>
                <el-form-item>
                    <el-button type="primary">立即创建</el-button>
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
                user: null,
                form: {
                    username: '',
                    gender: '',
                    birth: '',
                    avatar: '',
                    province: '',
                    city: '',
                    address: '',
                    phone: '',
                    email: '',
                },
                rules: {
                    username: [
                        {required: true, message: '请输入活动名称', trigger: 'blur'},
                    ],
                },
                genderOption: [
                    {label: "男", value: 1},
                    {label: "女", value: 2},
                    {label: "保密", value: 3}
                ]
            }
        },
        methods: {
            getUserInfo(id) {

                this.$axios({
                    url: `${this.$settings.HOST}/user/info/${id}/`,
                    method: 'GET',
                }).then(response => {
                    this.user = response.data;
                    console.log(this.user.username);
                    this.form.username = this.user.username;
                    this.form.gender = this.user.gender;
                    this.form.birth = this.user.birth;
                    this.form.avatar = this.user.avatar;
                    this.form.province = this.user.province;
                    this.form.city = this.user.city;
                    this.form.address = this.user.address;
                    this.form.phone = this.user.phone;
                    this.form.email = this.user.email;
                }).catch(error => {
                    alert(error.response);
                })
            }
            ,
        }
        ,
        created() {
            this.uid = sessionStorage.uid || localStorage.uid;
            this.getUserInfo(this.uid);
        }
        ,
        components: {
            Header
        }
    }
</script>

<style scoped>

</style>