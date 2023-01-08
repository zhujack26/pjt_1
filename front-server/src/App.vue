<template>
  <div id="app">
    <div style="height: 56px;">
    <NavBar/>
    </div>
    <router-view/>
    <ModalComp 
    v-if="isModalLogin"
    />
    <div class="theme-btn">
      <div v-if="!isDarkMode" class="darkmode" @click="toggleTheme"> </div>
      <div v-else class="lightmode" @click="toggleTheme"> </div>
    </div>
  </div>
</template>

<script>
import "./assets/css/index.scss"

import ModalComp from "./components/ModalComp.vue"
import NavBar from "./components/NavBar.vue"

export default {
  name: 'app',
  components: {
    ModalComp,
    NavBar,

  },
  data() {
    return {
    }
  },
  created() {
    document.documentElement.setAttribute("data-theme", "light");
  },
  computed: {
    isModalLogin() {
      return this.$store.state.isModalLogin
    },
    isDarkMode() {
      return this.$store.state.isDarkMode
    }
  },
  methods: {
    toggleTheme() {
      this.$store.dispatch('toggleTheme')
      // document.documentElement.classList.toggle("dark")
    },

  }
}
</script>
<style>
  
</style>
