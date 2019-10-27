import Vue from 'vue'
import Router from 'vue-router'
import index from '@/layouts/index'
import hotAnalyse from '@/layouts/hotAnalyse'
import onlineSpider from '@/layouts/onlineSpider'
import chartAnalyse from '@/layouts/chartAnalyse'
import paperDetail from '@/layouts/paperDetail'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/hotAnalyse',
      name: 'hotAnalyse',
      component: hotAnalyse
    },
    {
      path: '/onlineSpider',
      name: 'onlineSpider',
      component: onlineSpider
    },
    {
      path: '/chartAnalyse',
      name: 'chartAnalyse',
      component: chartAnalyse
    },
    {
      path: '/paperDetail',
      name: 'paperDetail',
      component: paperDetail
    }
  ]
})
