<template>
  <div class="signup-box">
    <div class="login-box">
      <div>
        <div style="margin-bottom: 10px;">
          <h1>JsCinephile</h1><br>
          <h3>회원가입</h3>
        </div>
        
        <div style="display: inline-block; text-align: center;">
          <div style="display: inline-block; text-align: center;">
            <form @submit.prevent="signUp">
              <div class="login">
                <input class="login_input underline" type="text" v-model="username" placeholder="아이디를 입력하세요">
              </div>
              <div class="login">
                <input class="login_input underline" type="password" v-model="password1" placeholder="비밀번호를 입력하세요">
              </div>
              <div class="login">
                <input class="login_input underline" type="password" v-model="password2" placeholder="위와 동일한 비밀번호를 입력하세요">
              </div>
              <div class="login">
                <input class="login_input underline" type="text" v-model="nickname" placeholder="닉네임을 입력하세요">
              </div>
              <button class="btn">계정 등록</button>
            </form>
          </div>
        </div>
      </div>
      <div class="tip">
        <p class="tip_text"> TIP. 포기</p>
      </div>
      <div>
      <button class="btn other" @click="openLogin">로그인</button>
      </div>
    </div>
    <!-- <div class="score-box">
      <div>
        <div class="genre-box"
          v-for="(score, genre) in genres"
          :key="genre.id"
        >
          <span class="genre-box_name">{{genre}}</span>
          <span>{{score}}</span>
        </div>
      </div>
    </div>
    <div class="dice-box">
      <div>
        <button @click="rollDice">주사위</button>
      </div>
    </div> -->
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      nickname: null,
      genres: {'액션': 0, '모험': 0, '애니메이션': 0, '코미디': 0, '범죄': 0, '다큐멘터리': 0, '드라마': 0, '가족': 0, '판타지': 0, '역사': 0, '공포': 0, '음악': 0, '미스터리': 0, '로맨스': 0, 'SF': 0, 'TV 영화': 0, '스릴러': 0, '전쟁': 0, '서부': 0}
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const nickname = this.nickname

      const payload = {
        username,
        password1,
        password2,
        nickname,
      }

      this.$store.dispatch('signUp', payload)

    },
    rollDice() {
      const stats = _.range(0, 20)
      let genres = this.genres
      Object.keys(genres).forEach(genre => {
        genres[genre] = _.sample(stats)
      })
      console.log(genres)
    },
    openLogin() {
      this.$store.commit('OPEN_LOGIN')
    },
  }
}
</script>
