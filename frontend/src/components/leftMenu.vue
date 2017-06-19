<template>
  <div class="sidebar">
    <el-menu id="leftMenu" default-active="1" class="el-menu-vertical-demo" @open="handleOpen" @close="handleClose"
             @select="handleSelect">
      <el-submenu v-bind:index="group.id" v-for="group in leftList" :key="group.id">
        <template slot="title"><i class="el-icon-message"></i>{{ group.name }}</template>
        <el-menu-item v-if="item.children.length == 0" v-bind:index="item.id" v-for="item in group.children"
                      :key="item.id">{{ item.name }}
        </el-menu-item>
        <el-submenu v-if="item.children.length > 0" v-bind:index="item.id" v-for="item in group.children"
                    :key="item.id">
          <template slot="title">{{ item.name }}</template>
        </el-submenu>
      </el-submenu>
    </el-menu>
  </div>
</template>
<script>
  import {store} from '../store'
  import router from '../router'
  export default {
    data: function () {
      return {
        leftList: [
          {id: '1', name: '仪表盘', children: [{id: '1-1', name: '监控', children: []}]},
          {id: '2', name: '控制台', children: [{id: '2-1', name: '个人中心', children: []}]}
        ]
      }
    },
    mounted () {
      console.log(this.leftList)
      var set = this
      store.$on('test', function (msg) {
        var data =[
          {id: '3', name: 'test1', children: [{id: '3-1', name: 'test11', children: []}]},
          {id: '4', name: 'test2', children: [{id: '4-1', name: 'test22', children: []}]}
        ]
        console.log(set.leftList)
        set.leftList.splice(0,set.leftList.length)
        for (let i = 0; i<data.length; i ++) {
          set.leftList.splice(i,0,data[i])
        }
        console.log(set.leftList)
      })
    },
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
      handleSelect(key, keyPath) {
        router.push('test')
        console.log(key, keyPath);
      }
    }
  }

</script>
<style>
  .sidebar {
    height: 100%;
  }

  .sidebar > ul {
    height: 100%;
  }
</style>
