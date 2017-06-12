<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style lang="less">
  html, body , #app{
    font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
    height: 100%;
    overflow: hidden;
    margin: 0;
  }
  /*浏览器滚动条*/
  ::-webkit-scrollbar {
    width: 6px;
    height: 6px; }

  ::-webkit-scrollbar-button:vertical {
    display: none; }

  ::-webkit-scrollbar-thumb:vertical {
    background-color: rgba(79, 101, 110,0.2);
    border-radius: 4px; }

  ::-webkit-scrollbar-thumb:vertical:hover {
    background-color: rgba(79, 101, 110,0.2); }

  ::-webkit-scrollbar-corner:vertical {
    background-color: rgba(79, 101, 110,0.2); }

  ::-webkit-scrollbar-resizer:vertical {
    background-color: rgba(79, 101, 110,0.2); }

  ::-webkit-scrollbar-thumb:horizontal {
    background-color: rgba(79, 101, 110,0.2);
    border-radius: 4px; }

  ::-webkit-scrollbar-thumb:horizontal:hover {
    background-color: rgba(79, 101, 110,0.2); }
</style>
