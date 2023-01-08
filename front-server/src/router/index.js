import Vue from 'vue'
import VueRouter from 'vue-router'
// import MovieView from '@/views/MovieView'
import ArticleView from '@/views/ArticleView'
import CreateView from '@/views/CreateView'
import ArticleDetailView from '@/views/ArticleDetailView'
import SignUpView from '@/views/SignUpView'
// import LogInView from '@/views/LogInView'
import UserView from '@/views/UserView'
import TestHome from '@/views/TestHome'
import KakaoMap from '@/views/KakaoMap'
import UserModify from '@/views/UserModify'
import MovieDetailView from '@/views/MovieDetailView'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movies',
    component: TestHome
  },
  {
    path: '/home',
    name: 'TestHome',
    component: TestHome,
  },

  {
    path: '/community',
    name: 'ArticleView',
    component: ArticleView
  },
 
  {
    path: '/create',
    name: 'CreateView',
    component: CreateView,
    // 라우터 가드
    beforeEnter(to, from, next) {
      const isLogin = router.app.$store.getters.isLogin
      if (isLogin) {
        next()
      } else {
        // router.app.$store.commit('OPEN_LOGIN')
      }
    }
  },

  {
    path: '/map',
    name: 'KakaoMap',
    component: KakaoMap
  },

  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },

  // {
  //   path: '/login',
  //   name: 'LogInView',
  //   component: LogInView
  // },

  {
    path: '/user',
    name: 'UserView',
    component: UserView
  },

  {
    path: '/movie/:id',
    name: 'MovieDetailView',
    component: MovieDetailView
  },

  {
    path: '/article/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView,
    // 라우터 가드
    beforeEnter(to, from, next) {
      const isLogin = router.app.$store.getters.isLogin
      if (isLogin) {
        next()
      } else {
        router.app.$store.commit('OPEN_LOGIN')
      }
    }
  },
  
  {
    path: '/usermodify',
    name: 'UserModify',
    component: UserModify,
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() {
    // 매개변수 to, from, savedPosition
    return { x: 0, y: 0 }
  },
  
})

router.beforeEach((to, from, next) => {
  console.log(to)
  console.log(from)
  console.log(next)
  if (to.name !== 'TestHome') {
    router.app.$store.commit('CLOSE_SEARCH')
  }
  next()
})

export default router
