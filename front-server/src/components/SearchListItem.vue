<template>
  <div class="sli-box" @click="goMovieDetail">
    <img :src="posterUrl" alt="포스터">
    <p>{{movie.title}}</p>
    <div class="sli-box_data">
      <span>{{createdYear}}</span>
      <span class="sli-box_data_in">•</span>
      <span class="sli-box_data_in">평균 ★</span>
      <span>{{movie.vote_average}}</span>
    </div>
    <p>{{genres.join(' ')}}</p>

    
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  name: 'SearchListItem',
  props: {
    movie: Object,
  },
  data() {
    return {
      genres: null,
      genre: {28: "액션", 12: "모험", 16: "애니메이션", 35: "코미디", 80: "범죄", 99: "다큐멘터리", 18: "드라마", 10751: "가족", 14: "판타지", 36: "역사", 27: "공포", 10402: "음악", 9648: "미스터리", 10749: "로맨스", 878: "SF", 10770: "TV 영화", 53: "스릴러", 10752: "전쟁", 37: "서부"}
    }
  },
  created() {
    this.convertGenre()
  },
  computed: {
    posterUrl() {
      // 'https://image.tmdb.org/t/p/w185'+this.movie.fields.poster_path
      return 'https://image.tmdb.org/t/p/w185'+this.movie.poster_path
    },
    createdYear() {
      let release_date = this.movie.release_date
      release_date = release_date.substr(0, 4)
      return release_date
    },
  },
  methods: {
    convertGenre() {
      // const moviegenre_nums = this.movie.genre_check
      const moviegenre_nums = this.movie.genre_ids
      const genres = moviegenre_nums.reduce((acc, genre_num) => {
        acc.push(this.genre[genre_num])
          return acc
      }, [])
      // console.log(genres)
      this.genres = genres
    },
    goMovieDetail() {
      this.$router.push({ name: 'MovieDetailView', params: { id: this.movie.id } })
    },
    // convertGenre() {
    //   axios({
    //     method: 'get',
    //     url: './genre.json',
    //   })
    //     .then((res) => {
    //       // console.log(res.data)
    //       const genres_num = res.data
    //       const moviegenre_nums = this.movie.fields.genre_check
    //       const genre_lst = genres_num.filter(item => moviegenre_nums.indexOf(item.pk) !== -1)
    //       const genres_name = genre_lst.reduce((acc, el) => {
    //         // console.log(el.fields.name, acc)
    //         acc.push(el.fields.name)
    //         return acc
    //       }, [])
    //       this.genres = genres_name
    //       console.log(this.genres)
    //     })
    // },
  }

}
</script>

<style></style>
