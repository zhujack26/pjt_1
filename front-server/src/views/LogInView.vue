<template>
  <div class="login-box">
    <div>
      <div style="margin-bottom: 10px;">
        <h1>JsCinephile</h1><br>
        <h3>로그인</h3>
      </div>
      
      <div style="display: inline-block; text-align: center;">
        <div style="display: inline-block; text-align: center;">
          <form @submit.prevent="logIn">
            <div class="login">
              <input class="login_input underline" type="text" id="username" v-model="username" placeholder="아이디를 입력하세요">
            </div>
            <div class="login">
              <input class="login_input underline" type="password" id="password" v-model="password" placeholder="비밀번호를 입력하세요">
            </div>
            <button class="btn">로그인</button>
          </form>
        </div>
        <div class="wrap">
          <hr class="bar">
          <span class="txt">OR</span>
          <hr class="bar">
        </div>
      </div>
    </div>
    <div>
      <button class="btn kakao" @click="kakaoLoginBtn">카카오톡으로 로그인</button>
    </div>
    <div>
      <button class="btn other" @click="openSignup">계정 생성</button>
    </div>
    <div class="tip">
      <p class="tip_text"> TIP. 아직 계정이 없으신가요? 저희는 소셜로그인이 가능해요. 아마도</p>
    </div>
  </div>
</template>

<script src="https://developers.kakao.com/sdk/js/kakao.js"></script>
<script>

export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    },
    openSignup() {
      this.$store.commit('OPEN_SIGNUP')
    },
    
    // 카카오 로그인
    kakaoLoginBtn() {

      window.Kakao.init(process.env.VUE_APP_KAKAOMAP_API_KEY) // Kakao Developers에서 요약 정보 -> JavaScript 키
      // 로그인 세션 제거
      if (window.Kakao.Auth.getAccessToken()) {
        window.Kakao.API.request({
          url: '/v1/user/unlink',
          success: function (response) {
            console.log(response)
          },
          fail: function (error) {
            console.log(error)
          },
        })
        window.Kakao.Auth.setAccessToken(undefined)
      }

      // 로그인 시도
      window.Kakao.Auth.login({
        success: function () {
          window.Kakao.API.request({
            url: '/v2/user/me',
            data: {
              property_keys: ["kakao_account.email"]
            },
            success: async function (response) {
              console.log(response);
            },
            fail: function (error) {
              console.log(error)
            },
          })
        },
        fail: function (error) {
          console.log(error)
        },
      })
    }
  }
}
</script>
