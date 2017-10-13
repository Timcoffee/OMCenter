<template>
  <div id="login">
    <div class="login-box">
      <div class="content">
        <div class="logo"><img class="logo-img" src="../assets/logo.png"/></div>

        <el-form :model="loginForm" :rules="rules" ref="ruleForm" class="login-row" label-width="0px">
          <el-form-item label="用户名" prop="username">
            <i class="iconfont icon-my"></i>
            <el-input v-model="loginForm.username" class="login-input" placeholder="用户名"></el-input>
          </el-form-item>

          <el-form-item label="密码" prop="password">
            <i class="iconfont icon-lock"></i>
            <el-input v-model="loginForm.password" class="login-input" type="password" placeholder="密码"></el-input>
          </el-form-item>
        </el-form>
        <el-button class="login-btn" type="primary" @click="login()">登  录</el-button>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'main',
    data() {
      return {
        loginForm: {}
      }
    }
  }
</script>
<style lang="less" scoped>

</style>
