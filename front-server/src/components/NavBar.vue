<template>
  <nav class="nav">
    <div class="nav__left">
      <div class="nav__left__logo" @click="goHome">
        <img v-if="isDarkMode" src="@/assets/cinephile_day.png" alt="">
        <img v-else src="@/assets/cinephile_night.png" alt="">
      </div>
      <div class="nav__left__menu">
        <router-link class="nav__left__menu__link" v-for="item in menu" :key="item.name" :to="item.link">
          <div class="nav__left__menu__item">
            <div class="nav__left__menu__item__name">{{ item.name }}</div>
          </div>
        </router-link>
      </div>
    </div>
    <div class="nav__right">
      <!-- <!— search input -> -->
      <div class="nav__right__search">
        <input type="text" placeholder="영화를 검색해보세요. " v-model="searchText" @keyup.enter="searchMovie"/>
      </div>
      <div v-if="!isLogin" class="nav__right__login" @click="openLogin">로그인</div>
      <div v-else class="nav__right__login" @click="logOut">로그아웃</div>
      <div v-if="!isLogin" class="nav__right__signup" @click="openSignup">회원가입</div>
      <div v-else class="nav__right__signup" @click="profile">프로필</div>
    </div>
  </nav>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'NavBar',
  data() {
    return {
      menu: [
        // {
        //   name: "홈",
        //   link: "/home",
        // },
        {
          name: "커뮤니티",
          link: "/community",
        },
        {
          name: "영화관 찾기",
          link: "/map",
        },
        // {
        //   name: "메뉴",
        //   link: "/",
        // },
      ],
      searchText: null,
    }
  },
  methods: {
    openLogin() {
      this.$store.commit('OPEN_LOGIN')
    },
    openSignup() {
      this.$store.commit('OPEN_SIGNUP')
    },
    logOut() {
      this.$store.commit('DELETE_TOKEN')
    },
    profile() {
      this.$router.push({ name: 'UserView' })
    },
    searchMovie() {
      this.$router.push({ name: 'TestHome' })
      this.$store.commit('CLOSE_SEARCH')
      this.$store.dispatch('searchMovie', this.searchText)
    },
    goHome() {
      this.$router.push({ name: 'TestHome' })
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    ...mapState([
      'isModalLogin',
      'isDarkMode',
    ])
  },

}
</script>

<style>
  
</style>