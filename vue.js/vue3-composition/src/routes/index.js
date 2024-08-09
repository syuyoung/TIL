import { createRouter, createWebHashHistory } from 'vue-router'
import Option from '@/components/Option.vue'

export default createRouter({
  // Hash
  // https://google.com/#/search
  history: createWebHashHistory(),
  // pages
  routes: [
    {
      // 각각의 경로
      path: '/',
      component: Option
    }
  ]
})
