import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '@/components/Index/Index'

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
        component: __import__('User/User')
    },
    {
        path: '/login',
        name: 'login',
        component: __import__('User/Login')
    },
    {
        path: '/register',
        name: 'register',
        component: __import__('User/Register')
    },
    {
        path: '/scene/:id',
        name: 'scene',
        component: __import__('Travel/Scene')
    },
    {
        path: '/destination',
        name: 'destination',
        component: __import__('Travel/Destination')
    },
    {
        path: '/city/:id',
        name: 'city',
        component: __import__('Travel/City')
    }
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

export default router;
