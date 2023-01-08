<template>
  <div>
    <div class="search-info">
      <span class="search-info_text">"{{searchText}}"의 검색결과</span>
      <span class="material-symbols-outlined search-info_icon" @click="closeSearch">close</span>
    </div>
    <div class="search-box">
      <div class="search-box_inner">
        <div class="search-header">
        <div class="search-header_outer">
          <div class="search-header_inner">
            <span>콘텐츠</span>
          </div>
        </div>
      </div>
      <div class="searchlistitem-box">
        <div class="searchlistitem-box_inner">
          <swiper
            class="swiper"
            :options="swiperOption"
          >
            <swiper-slide 
              v-for="movie in movies"
              :key="movie.id">
              <SearchListItem :movie="movie"/>
            </swiper-slide>
            <!-- <div
                class="swiper-pagination"
                slot="pagination"
                >
            </div> -->
          </swiper>
          <div class="sli-btn">
            <div class="swiper-button-prev sli-btn_l" slot="button-prev"></div>
            <div class="swiper-button-next sli-btn_r" slot="button-next"></div>
          </div>
        </div>
      </div>
      </div>
      
      <div class="hr-box"></div>
    </div>
  </div>
</template>

<script>
import SearchListItem from './SearchListItem.vue'
// import axios from 'axios'
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
  name: 'SearchList',
  components: {
    SearchListItem,
    Swiper,
    SwiperSlide,
  },
  data() {
    return {
      movies: null,
      newMovie: null,
      swiperOption: { 
        autoHeight: true,
        slidesPerView: 3,
        spaceBetween: 10, 
        slidesPerGroup: 3,
        loop: false, 
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
            slidesPerView: 4,
            slidesPerGroup: 4,
          },
          '@1.20': {
            slidesPerView: 5,
            slidesPerGroup: 5,
          }
        },
      },
      searchText: null,
    }
  },
  created() {
    this.getMovies()
    
  },
  methods: {
    getMovies() {
      // axios({
      //   method: 'get',
      //   url: './movie.json',
      // })
      //   .then((res) => {
      //     // console.log(res)
      //     this.movies = res.data
      //     this.searchText = this.$store.state.searchText
      //   })

      // tmdb 통신용
      this.searchText = this.$store.state.searchText
      this.movies = this.$store.state.searchMovies
      console.log(this.movies)
    },
    closeSearch() {
      this.$store.commit('CLOSE_SEARCH')
    },
    
  },
}
</script>

<style>

</style>