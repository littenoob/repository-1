import Vue from 'vue'
import VueRouter from 'Vue-router'
// import main from '../views/main.vue'
Vue.use(VueRouter)

const routers = [
    {
        path: '/',
        name: 'main',
        component: () => import('../views/main.vue')
    }
]

const router = new VueRouter(
    {
        mode: 'history',
        routes: routers
    }
)

export default router