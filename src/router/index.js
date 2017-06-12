import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login.vue'
import main from '@/components/main.vue'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/main',
      name: 'main',
      component: main
    },
    {
      path: '/login',
      name: 'login',
      component: login
    }
  ]
})
