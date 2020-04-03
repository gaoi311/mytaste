import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '@/components/Index'

Vue.use(VueRouter);

const __import__ = file => () => import(`@/components/${file}.vue`);

const routes = [
    {
        path: '/',
        name: 'index',
        component: Index
    },
    {
        path: '/user',
        name:'user',
        component: __import__('User')
    },
    {
        path: '/login',
        name: 'login',
        component: __import__('Login')
    },
    {
        path: '/register',
        name: 'register',
        component: __import__('Register')
    }
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

export default router;
