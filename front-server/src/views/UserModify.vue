<template>
  <div class="settingbox">
    <header class="settingname">
      
      <div class="settingname_1"></div>
      <div class="settingname_2"></div>
      <div class="settingname_3">설정</div>
      <h1>회원정보 변경</h1>
    </header>
    <div class="settingcontext">
      <div class="settingcontext_1">
        <div class="settingcontext_2">
          <section class = "settingcontext_3">
            <div class="login">
              <input class="login_input underline" type="text" v-model="username" placeholder="새로운 아이디를 입력하세요">
            </div>
            <div class="login">
              <input class="login_input underline" type="password" v-model="password1" placeholder="새로운 비밀번호를 입력하세요">
            </div>
            <div class="login">
              <input class="login_input underline" type="password" v-model="password2" placeholder="위와 동일한 비밀번호를 입력하세요">
            </div>
            <div class="login">
              <input class="login_input underline" type="text" v-model="nickname" placeholder="새로운 닉네임을 입력하세요">
            </div>
          </section>
          <button class="btn">정보 변경</button>
        <!-- 탈퇴하기  -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserModify',
  data() {
    return {
      password1: null,
      password2: null,
      nickname: null,
    }
  },
  methods: {
    modifyUser() {
      const password1 = this.password1
      const password2 = this.password2
      const nickname = this.nickname

      const payload = {
        password1,
        password2,
        nickname,
      }

      this.$store.dispatch('modifyUser', payload)
    }
  }
}
</script>

<style>
  .settingbox {
    display: inline-block;
    position: relative;
    vertical-align: middle;
    text-align: left;
    /* width: 375px; */
    height: auto;
    min-height: 540px;
    border-radius: 6px;
    overflow: auto;
  }
  .settingname {
    left: 0px;
    z-index: 50;
    background: rgb(255, 255, 255);
    box-sizing: border-box;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: -0.5px;
    line-height: 22px;
    width: 100%;
    padding: 0px 16px;
    /* border-bottom: 1px solid rgb(227, 227, 227); */
    position: absolute;
    top: 0px;
    text-align: left;
    height: auto;
  }
  h1 {
    text-align: center;
    }
  .settingcontext {
    height: auto;
    overflow: auto;
    box-sizing: border-box;
    padding: 96px 0px 0px;
  }
  .settingname_1 {
    display: flex;
    -webkit-box-pack: justify;
    justify-content: space-between;
  }
  .settingname_2 {
    display: flex;
    transform: translate3d(0px, 0px, 0px);
    -webkit-box-pack: center;
    justify-content: center;
    -webkit-box-align: center;
    align-items: center;
    height: 30px;
    margin: 0px 4px 10px;
    opacity: 1;
  }
  .settingname_3 {
    position: absolute;
    top: 0px;
    right: 0px;
    left: 0px;
    white-space: nowrap;
    text-align: center;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: -0.5px;
    line-height: 22px;
    margin: 11px 100px;
    overflow: hidden;
    text-overflow: ellipsis;
    opacity: 0;
  }
  .settingcontext_1 {
    text-align: left;
  }
  .settingcontext_2 {
    margin: 0px 20px;
  }
  .settingcontext_3 {
    margin: 32px 0px;
  }
</style>