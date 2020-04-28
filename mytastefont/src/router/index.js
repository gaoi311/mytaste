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
        path: '/city/:id',
        name: 'city',
        component: __import__('Travel/City')
    },
    {
        path: '/destination',
        name: 'destination',
        component: __import__('Travel/Destination')
    },
    {
        path: '/hotel/:id',
        name: 'hotel',
        component: __import__('Hotel/Hotel')
    },
    {
        path: '/hotels/:id',
        name: 'hotels',
        component: __import__('Hotel/HotelList')
    },
    {
        path: '/scene/:id',
        name: 'scene',
        component: __import__('Travel/Scene')
    },
    {
        path: '/scenes/:id',
        name: 'scenes',
        component: __import__('Travel/SceneList')
    },
    {
        path: '/self',
        name: 'self',
        component: __import__('User/User')
    },
    {
        path: '/self/info',
        name: 'info',
        component: __import__('User/UserInfo')
    },

];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

export default router;
