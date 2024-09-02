import { createApp } from 'vue'
import App from './App.vue'
import router from './router' ///index.js 생략 가능
import store from './store'
import loadImage from '@/plugins/loadImage'

const app = createApp(App)

app.use(router)
app.use(store)
app.use(loadImage)
app.mount('#app')
