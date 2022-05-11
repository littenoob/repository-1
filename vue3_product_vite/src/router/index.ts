import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'StartSearch',
    component: () => import('@/components/content/StartSearch.vue')
  },
  {
    path:'/resultProduct',
    name:'ResultProduct',
    component: () => import('@/components/common/search/ResultProduct.vue')
  },
  {
    path:'/productDateShow',
    name:'ProductDateShow',
    component:() => import('@/components/content/productDateShow.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
