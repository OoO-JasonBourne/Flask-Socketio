import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
// import VueSocketIO from 'vue-socket.io'
// import socketIO from 'socket.io-client'


Vue.config.productionTip = false

Vue.use(ElementUI);

// Vue.use(new VueSocketIO({
//   debug: true,
//   connection: socketIO('http://127.0.0.1:5002/dcenter', {
//     autoConnect: false
//   })
// }))



new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
