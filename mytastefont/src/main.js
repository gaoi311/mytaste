import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';
import settings from '@/settings';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';


// 使用element-ui
Vue.use(ElementUI);
// 使用axios
Vue.prototype.$axios = axios;
Vue.prototype.$settings = settings;
Vue.config.productionTip = false;
// 不允许ajax携带cookie
axios.defaults.withCredentials = false;

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
