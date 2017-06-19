<template>
  <div id="login">
    <div class="login-box">
      <div class="content">
        <div class="logo"><img class="logo-img" src="../assets/logo.png"/></div>

        <el-form :model="loginForm" :rules="rules" ref="ruleForm" class="login-row" label-width="0px">
          <el-form-item label="用户名" prop="username">
            <el-input v-model="loginForm.username" class="login-input" placeholder="用户名"></el-input>
          </el-form-item>

          <el-form-item label="密码" prop="password">
            <el-input v-model="loginForm.password" class="login-input" type="password" placeholder="密码"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button class="login-btn" type="primary" @click="login()">登  录</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'login',
    data () {
      return {
          loginForm :{
            username: '',
            password: ''
          },

        rules: {
          username: [
            { required: true, message: '请输入用户名', trigger: 'blur' },
          ],
          password: [
            { required: true, message: '请输入密码', trigger: 'blur' }
          ],
        },
        showLogin: false,
      }
    },
    components: {
    },
    methods: {
      goMain () {
        this.$router.push('main')
      },
      login() {
        localStorage.username = this.loginForm.username;
        this.goMain();
      }
    }
  }
</script>
<style lang="less">
  #login {
    width: 100%;
    height: 100%;
    color: #47525D;
    background: rgba(238, 243, 252, .96) url(../assets/login_bg.png) center bottom no-repeat fixed;
    background-size: contain;
  }
  .login-input {
    input:last-child {
      border-radius: 0 !important;
    }
  }
  .login-row {
    margin: 20px;
    label {
      display: none;
    }
  }

  .login-btn {
    width: 100%;
    border-radius: 0 !important;
  }

  .logo {
    background-color: #fff;
    text-align: center;
    .logo-img {
      margin: 10px 0 10px 0;
      height: 60px;
    }
  }

  .login-box {
    width: 100%;
    margin: 0 auto;
    position: relative;
    top: 30%;
    text-align: center;
    min-height: 340px;
    .content {
      display: inline-block;
      width: 378px;
      padding: 32px 64px;
      text-align: left;
      background: #fff;
      box-shadow: 0 0 6px 0 rgba(0, 0, 0, .12), 0 26px 24px 0 rgba(118, 153, 223, .1);
    }
  }

</style>
