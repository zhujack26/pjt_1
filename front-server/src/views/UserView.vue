<template>
  <div class= "uvborder">
    <div class="uvsecond">
      <div class="uvthird">
        <div class="uvfourth">
          <!-- <div class="wall" :style="{backgroundImage: url(`${backgroundUrl}`)}"> -->
            <div class="wall" ref="bgstyle">
              <div>
                <button class="wallbutton" @click="openSetting"> </button>
              </div>
          </div>
          <div>
          <div style="margin: 0px 20px">
          <header class="userbox">
              <div class ="profileboarder">
                <div class ="profile" ></div>
              </div>
              <div class="usernamebox"> 
                <h1 class="username">{{this.$store.state.nickname}}</h1>
              </div>
          </header>
          </div>
          <div class="moive_first_user">
      <div class= "movie_subject_user">
        <p class= "movie_subject_name_user">회원님이 좋아요 한 영화</p>
      </div>
      <div class="movie_second_user">
        <div class="movie_third_user">
          <ul class="movie_list_user">
            <swiper :options="swiperOption">
              <swiper-slide
                v-for="(movie, index) in likeMovies" 
                :key="movie.id">
                <MovieList4
                  :movie="movie"
                  :index="index"
                />
              </swiper-slide>
            </swiper>
          </ul>
        </div>
      </div> 
    </div>
          </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import MovieList4 from '@/components/MovieList4'
import axios from 'axios'
import "swiper/css/swiper.css";
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UserView',
  components: {
    MovieList4, 
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      backgroundUrl : null,
      likeMovies: null,
      menu : [
      {
        name: "정보수정",
        link: "/usermodify"
      }
      ],
      swiperOption: {
          slidesPerView: 3,
          centeredSlides: false,
          spaceBetween: 1,
          pagination: {
            el: '.swiper-pagination',
            clickable: true
          },
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          },
          breakpoints: {
          '@0.75': {
            slidesPerView: 4
          },
          '@1.20': {
            slidesPerView: 5
          }
          },
          swiperSlides: [1, 2, 3, 4, 5]
          }
        }
      },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  created() {
    this.getbackground()
    this.getLikeList()
    },
  methods: {
    openSetting() {
      // this.$router.push({ name: 'UserModify'})
      this.$store.commit('ON_MODIFY')
    },
    fileChange: function(e) {
      console.log(e.target.files)
      this.file = e.target.files[0];
    },
    getUser() {
      if (this.isLogin === true) { 
        this.$store.dispatch('getUser')
      } else {
        alert('로그인이 필요한 서비스 입니다.')
        this.$router.push({ name: 'LogInView'})
      }
    },
    getbackground() {
      const backgroundNum = _.range(1, 9) 
      const selectedBack = _.sample(backgroundNum)
      const backgroundUrl = `@/assets/backgroundimage/background${selectedBack}.jpg`
      // this.$refs.bgstyle.style.backgroundImage = `url('${backgroundUrl}')`
      this.backgroundUrl = backgroundUrl

      // this.backgroundUrl = backgroundUrl
      // console.log('!!!!!!!!drl', this.backgroundUrl)
    },
    getLikeList() {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/${this.$store.state.userid}/list/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          // console.log('!!!!!!!likelist', res.data)
          this.likeMovies = res.data.like_movies
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
}
</script>

<style>
  .profile {
    position: relative;
    z-index: 1;
    background: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTyk5JAnYUj_KF4VKN9RJKje3ABzOc2JB1yftEo0ZLT-ur8V0dBbAqa0VeFUhphbApVX6E&usqp=CAU);
    background-size: cover;
    width: 100%;
    height: 100%;
  }
  .profileboarder {
    border: 1px solid rgba(0, 0, 0, 0.08);
    border-radius: 50%;
    display: flex;
    position: relative;
    -webkit-box-pack: center;
    justify-content: center;
    -webkit-box-align: center;
    align-items: center;
    width: 56px;
    height: 56px;
    overflow: hidden;
  }
  .uvborder {
    display: flex;
    flex-direction: column;
  }
  .uvsecond {
    flex: 1 1 0%;
    margin: 28px 0px 30px;
  }
  .uvthird {
    max-width: 1100px;
    margin: 0px auto;
  }
  .uvfourth {
    border: 1px solid;
    border-radius: 6px;
    border-color: rgb(227, 227, 227);
  }
  .wall {
    position: relative;
    background: url(https://d2rlq84xifqisi.cloudfront.net/images/mypagePatternResize.2e73487f09488acbeb2d.jpg);
    background-size: 180px 177px;
    padding-top: 30%;
    margin: 0 0 -20px;
  }
  .wallbutton {
    padding: 0px;
    border: none;
    margin: 0px;
    cursor: pointer;
    position: absolute;
    top: 10px;
    right: 10px;
    background: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGZpbGw9Im5vbmUiIGZpbGwtcnVsZT0iZXZlbm9kZCI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIvPgogICAgICAgIDxwYXRoIGZpbGw9IiNGRkYiIGZpbGwtcnVsZT0ibm9uemVybyIgZD0iTTE5LjQzIDEyLjk4Yy4wNC0uMzIuMDctLjY0LjA3LS45OCAwLS4zNC0uMDMtLjY2LS4wNy0uOThsMi4xMS0xLjY1Yy4xOS0uMTUuMjQtLjQyLjEyLS42NGwtMi0zLjQ2Yy0uMTItLjIyLS4zOS0uMy0uNjEtLjIybC0yLjQ5IDFjLS41Mi0uNC0xLjA4LS43My0xLjY5LS45OGwtLjM4LTIuNjVBLjQ4OC40ODggMCAwIDAgMTQgMmgtNGMtLjI1IDAtLjQ2LjE4LS40OS40MmwtLjM4IDIuNjVjLS42MS4yNS0xLjE3LjU5LTEuNjkuOThsLTIuNDktMWMtLjIzLS4wOS0uNDkgMC0uNjEuMjJsLTIgMy40NmMtLjEzLjIyLS4wNy40OS4xMi42NGwyLjExIDEuNjVjLS4wNC4zMi0uMDcuNjUtLjA3Ljk4IDAgLjMzLjAzLjY2LjA3Ljk4bC0yLjExIDEuNjVjLS4xOS4xNS0uMjQuNDItLjEyLjY0bDIgMy40NmMuMTIuMjIuMzkuMy42MS4yMmwyLjQ5LTFjLjUyLjQgMS4wOC43MyAxLjY5Ljk4bC4zOCAyLjY1Yy4wMy4yNC4yNC40Mi40OS40Mmg0Yy4yNSAwIC40Ni0uMTguNDktLjQybC4zOC0yLjY1Yy42MS0uMjUgMS4xNy0uNTkgMS42OS0uOThsMi40OSAxYy4yMy4wOS40OSAwIC42MS0uMjJsMi0zLjQ2Yy4xMi0uMjIuMDctLjQ5LS4xMi0uNjRsLTIuMTEtMS42NXpNMTIgMTUuNWMtMS45MyAwLTMuNS0xLjU3LTMuNS0zLjVzMS41Ny0zLjUgMy41LTMuNSAzLjUgMS41NyAzLjUgMy41LTEuNTcgMy41LTMuNSAzLjV6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=) center center / cover no-repeat;
    width: 40px;
    height: 40px;
  }
  .userbox {
    position: relative;
    padding-bottom: 26px;
  }
  .usernamebox {
    display: flex;
    -webkit-box-align: center;
    align-items: center;
    margin-top: 4px;
  }
  .username {
    color: rgb(0, 0, 0);
    font-size: 25px;
    font-weight: 700;
    letter-spacing: -0.9px;
    line-height: 30px;
    width: 100%;
  }
  .movie_first_user {
    margin-bottom: 20px;
    /* font-family:  */
  }
  .movie_second_user {
    max-width: 1320px;
  }
  .movie_third_user {
    position: relative;
    margin-right: 20px;
    margin-left: 15px;
  }
  .movie_list_user {
    list-style: none;
    padding: 0;
    white-space: nowrap;
    margin-right: -4px !important;
    margin-left: -4px !important;
    margin: 0;
  }
  .movie_subject_user {
    line-height: 29px;
    max-height: 58px;
    padding: 4px 20px 9px 0;
    white-space: nowrap;
    max-width: 1320px;
    margin-right: 15px;
    margin-left: 15px;
  }
  .movie_subject_name_user {
    font-weight: 700;
    letter-spacing: -0.4px;
    line-height: 30px;
    color: #292a32;
    display: -webkit-box;
    white-space: normal;
    overflow: hidden;
    text-overflow: ellipsis;
    max-height: 60px;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
  }
</style>