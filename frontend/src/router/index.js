// import Vue from 'vue'
// import Router from 'vue-router'
// import login from '@/components/login.vue'
// import main from '@/components/main.vue'
// import home from '@/components/home.vue'
//
// Vue.use(Router);
//
// export default new Router({
//   routes: [
//     {
//       path: '/',
//       redirect: '/login'
//     },
//     {
//       path: '/main',
//       component: main,
//       children: [{
//         path: '/',
//         component: home
//       }]
//     },
//     {
//       path: '/login',
//       component: login
//     }
//   ]
// })
import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/main',
      component: resolve => require(['@/components/main.vue'], resolve),
      children:[
        {
          path: '/',
          component: resolve => require(['@/components/home.vue'], resolve)
        },
        {
          path: '/test',
          component: resolve => require(['@/components/test.vue'], resolve)
        }
      ]
    },
    {
      path: '/login',
      component: resolve => require(['@/components/login.vue'], resolve)
    },
  ]
})
