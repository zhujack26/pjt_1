<template>
  <div>
    <div class="SearchBox">
      <SearchList
        v-if="isSearch"
      />
    </div>
    <MovieView/>
  </div>
</template>

<script>
import SearchList from '../components/SearchList.vue'
import MovieView from '../views/MovieView.vue'
import _ from 'lodash'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'TestHome',
  components: {
    SearchList,
    MovieView,
  },
  created() {
    this.recommendGenre()
  },
  data() {
    return {
      genres: {28: "액션", 12: "모험", 16: "애니메이션", 35: "코미디", 80: "범죄", 99: "다큐멘터리", 18: "드라마", 10751: "가족", 14: "판타지", 36: "역사", 27: "공포", 10402: "음악", 9648: "미스터리", 10749: "로맨스", 878: "SF", 10770: "TV 영화", 53: "스릴러", 10752: "전쟁", 37: "서부"},
      genre_movie: null,
    }
  },
  computed: {
    isSearch() {
      return this.$store.state.isSearch
    }
  },
  methods: {
    recommendGenre() {
      const genres = this.genres
      const genre_num = _.sampleSize(Object.keys(genres), 1)
      // console.log('!!!!',genre_num)

      const URL = API_URL+`/movies/${genre_num}/sort/`
      console.log('!!!!!',URL)
      axios({
        mothod: 'get',
        url: URL,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.genre_movie = res.data
          console.log(this.genre_movie)
          this.$store.commit('GET_GENRE_MOVIE', res.data)
        })
    },
    
  },
  
}
</script>

<style>

</style>