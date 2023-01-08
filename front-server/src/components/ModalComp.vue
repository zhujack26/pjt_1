<template>
  <div class="modal">
    <div class="overlay" @click="closeModal"></div>
    <div class="modal-card">
      <LoginView v-if="notSign && !onModify"/>
      <SignUpView v-if="!notSign && !onModify"/>
      <UserModify v-if="onModify"/>
    </div>
  </div>
</template>

<script>
import LoginView from "@/views/LogInView"
import SignUpView from "@/views/SignUpView"
import UserModify from "@/views/UserModify"

export default {
  name: 'ModalComp',
  components: {
    LoginView,
    SignUpView,
    UserModify,
  },
  methods: {
    closeModal() {
      this.$store.commit('CLOSE_MODAL')
    }
  },
  computed: {
    notSign() {
      return this.$store.state.notSign
    },
    onModify() {
      return this.$store.state.onModify
    },
  }
}
</script>

<style>

</style>
