<template>
  <div class="content">
    <el-row>
      <el-col :span="24">
        <header-menu></header-menu>
      </el-col>
    </el-row>
    <div class="row">
      <div class="box">
        <left-menu></left-menu>
      </div>
      <div class="content-view">
        <transition name="move" mode="out-in">
          <div class="content-box">
            <router-view></router-view>
          </div>
        </transition>
      </div>
    </div>
  </div>
</template>

<script>
  import headerMenu from './headerMenu'
  import leftMenu from './leftMenu'
  export default {
    name: 'main',
    data () {
      return {

      }
    },
    components: {
      headerMenu,
      leftMenu
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="less" scoped>
  .content {
    height: 100%;
  }

  .row {
    height: ~ "calc(100% - 100px)";
    .box {
      float: left;
      display: inline;
      height: 100%;
      width: 250px;
    }
    .content-view {
      float: left;
      display: inline;
      height: 100%;
      background: none repeat scroll 0 0 #dedede;
      position: absolute;
      left: 250px;
      right: 0;
      top: 100px;
      bottom: 0;
      width: auto;
      padding: 40px;
      box-sizing: border-box;
      overflow-y: scroll;
      .content-box {
        box-shadow: 0 0 6px 0 rgba(0, 0, 0, .12), 0 26px 24px 0 rgba(118, 153, 223, .1);
        background-color: #fff;
        padding: 20px;
      }
    }
  }
</style>
