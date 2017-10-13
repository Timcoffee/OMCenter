<template>
  <div id="app">
    <router-view v-loading.fullscreen.lock="loading"></router-view>
  </div>
</template>

<script>
  import {store} from './store'
  export default {
    name: 'app',
    data () {
      return {
          loading: false
      }
    },
    mounted() {
      let self = this
      store.$on('showLoading', function (type) {
        self.loading = type;
      })
    }
  }

</script>

<style lang="less">
  html, body, #app {
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
    height: 100%;
    overflow: hidden;
    margin: 0;
  }

  /*浏览器滚动条*/
  ::-webkit-scrollbar {
    width: 6px;
    height: 6px;
  }

  ::-webkit-scrollbar-button:vertical {
    display: none;
  }

  ::-webkit-scrollbar-thumb:vertical {
    background-color: rgba(79, 101, 110, 0.2);
    border-radius: 4px;
  }

  ::-webkit-scrollbar-thumb:vertical:hover {
    background-color: rgba(79, 101, 110, 0.2);
  }

  ::-webkit-scrollbar-corner:vertical {
    background-color: rgba(79, 101, 110, 0.2);
  }

  ::-webkit-scrollbar-resizer:vertical {
    background-color: rgba(79, 101, 110, 0.2);
  }

  ::-webkit-scrollbar-thumb:horizontal {
    background-color: rgba(79, 101, 110, 0.2);
    border-radius: 4px;
  }

  ::-webkit-scrollbar-thumb:horizontal:hover {
    background-color: rgba(79, 101, 110, 0.2);
  }

  .user-info {
    .el-dialog--tiny {
      width: 300px !important;
    }
  }

  #login {
    width: 100%;
    height: 100%;
    color: #47525D;
    background: rgba(238, 243, 252, .96) url(./assets/login_bg.png) center bottom no-repeat fixed;
    background-size: contain;
    .iconfont {
      position: absolute;
      left: 10px;
      z-index: 5;
      font-size: 15px;
      color: deepskyblue;
    }

    .register-btn {
      margin-left: 20px !important;
      width: 338px;
      text-align: center;
    }

    .login-input {
      input:last-child {
        padding-left: 30px;
        border-radius: 0 !important;
      }
    }

    .captcha-box {
      margin-top: -13px;
      .iconfont {
        top: 13px;
      }
    }

    .captcha-input {
      width: 180px;
    }

    .captcha {
      height: 36px;
      top: 13px;
      position: relative;
      left: 10px;

    }

    .login-row {
      margin: 20px;
      label {
        display: none;
      }
    }

    .login-remember {
      margin-left: 20px;
    }

    .login-btn {
      margin: 0 0 20px 20px;
      width: 338px;
      border-radius: 0 !important;
    }

    .logo {
      background-color: #fff;
      text-align: center;
      .logo-img {
        margin: 10px 0 10px 0;
        height: 40px;
        width: 320px;
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
  }
</style>
