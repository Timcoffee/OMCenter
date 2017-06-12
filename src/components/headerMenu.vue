<template>
  <div class="header">
    <el-row>
      <el-col :span="4">
        <div class="logo"><img class="logo-img" src="../assets/logo.png"/></div>
      </el-col>
      <el-col :span="16">
        <div>
          <el-menu :default-active="activeIndex" class="el-menu-demo head-module" mode="horizontal"
                   @select="handleSelect" router>
            <el-menu-item class="head-module" index="1">CMDB</el-menu-item>
            <el-menu-item class="head-module" index="2">应用中心</el-menu-item>
            <el-menu-item class="head-module" index="3">任务中心</el-menu-item>
            <el-menu-item class="head-module" index="4">服务中心</el-menu-item>
            <el-menu-item class="head-module" index="5">管理中心</el-menu-item>
          </el-menu>
        </div>
      </el-col>
      <el-col :span="4">
        <div class="user-info">
          <el-dropdown class="user-info">
            <div class="user-info">
              <img class="user-logo" src="../assets/user.jpg">
              <span class="el-dropdown-link">{{username}}</span>
            </div>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>退出</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
      </el-col>
    </el-row>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        activeIndex: '1',
        username: localStorage.getItem('username')
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>
<style lang="less" scoped>
  .head-module{
    height: 100px !important;
    line-height: 100px !important;
  }
  .logo {
    height: 100px;
    background-color: #eef1f6;
    .logo-img {
      margin: 20px 0 0 20px;
      height: 60px;
    }
  }
  .user-info {
    height: 100px;
    width: 100%;
    background-color: #eef1f6;
  }
  .user-info .el-dropdown-link{
    right: 40px;
    position: absolute;
    top: 45px;
  }
  .user-info .user-logo{
    position: absolute;
    right: 90px;
    top:20px;
    width:60px;
    height:60px;
    border-radius: 50%;
  }

</style>
