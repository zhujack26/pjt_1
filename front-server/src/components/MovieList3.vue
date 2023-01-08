<template>
  <li class="movie_card">
    <span>
      <div class ="movie_border"> 
        <div class="movie_img">
          <span v-if="!isLike"  @click="likeMovie" class ="moviegood"> ♥</span>
          <span v-else @click="likeMovie" class ="moviegood2"> ♥</span>
          <span class ="number_cnt"> {{index+1}}</span>
          <img @click="goMovieDetail" :src="getTrend" :alt="movie3.title" class= "movie">  
        </div>
      </div>
      <div class="context">
        <div class = "movie_title">{{ movie3.title }}</div>
        <div class= "context_detail">{{createdYear}} 평균 ★{{movie3.vote_average.toFixed(1) }}</div>
      </div>
    </span>
  </li>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'MovieList3',
  props: {
    movie3: Object,
    index: Number,
  },
  data() {
    return {
      isLike: false,
      genres: null,
      genre: {28: "액션", 12: "모험", 16: "애니메이션", 35: "코미디", 80: "범죄", 99: "다큐멘터리", 18: "드라마", 10751: "가족", 14: "판타지", 36: "역사", 27: "공포", 10402: "음악", 9648: "미스터리", 10749: "로맨스", 878: "SF", 10770: "TV 영화", 53: "스릴러", 10752: "전쟁", 37: "서부"}
    }
  },
  created() {
    this.convertGenre()
    this.isLikeMovie()
  },
  computed: {
    getTrend() {
      return `https://image.tmdb.org/t/p/original/${this.movie3.poster_path}`
    },
    createdYear() {
      let release_date = this.movie3.release_date
      release_date = release_date.substr(0, 4)
      return release_date
    },
  },
  methods: {
    convertGenre() {
      const moviegenre_nums = this.movie3.genre_ids
      const genres = moviegenre_nums.reduce((acc, genre_num) => {
        acc.push(this.genre[genre_num])
          return acc
      }, [])
      this.genres = genres
    },
    goMovieDetail() {
        this.$router.push({ name: 'MovieDetailView', params: { id: this.movie3.id } })
    },
    likeMovie() {
      this.$store.dispatch('likeMovie', this.movie3.id)
      this.isLikeMovie()
    },
    isLikeMovie() {
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.movie3.id}/exist/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          // console.log('!!!!!!!', res.data)
          if (res.data === 1) {
            this.isLike = true
          } else {
            this.isLike = false
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
  }
}

</script>

<style>
  .movie {
    border-radius: 5px;
    vertical-align: top;
    width: 100%;
    height: 100%;
    opacity: 1;
    object-fit: cover;
    
  }
  .number_cnt {
    position: absolute;
    top: 3px;
    left: 3px;
    background-color: rgba(0, 0, 0, 0.77);
    color: rgb(255, 255, 255);
    font-weight: 700;
    letter-spacing: normal;
    font-size: 14px;
    line-height: 22px;
    text-align: center;
    width: 24px;
    height: 24px;
    border-radius: 4px;
    opacity: 1;
  }
  .movie_img {
    position: absolute;
    top: 0;
    left: 0;
    box-sizing: border-box;
    height: 100%;
  }
  .movie_img:hover {
    cursor: pointer;
  }
  .movie_border {
    position: relative;
    width: 100%;
    height: 0;
    padding-bottom: 143%;
  }
  .movie_title {
    display: -webkit-box;
    font-size: 15px;
    font-weight: 400;
    letter-spacing: -0.2px;
    /* line-height: 18px; */
    white-space: normal;
    max-height: 36px;
    margin-bottom: 4px;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    color: #292a32;
  }
  .context_detail {
    color: #555765;
    display: flex;
    font-size: 14px;
    letter-spacing: 0;
    line-height: 14px;
    height: 20px;
  }
  .context {
    margin: 6px 5px 0 0;
    text-align: left;
    width: calc(100% - 10px);
  }
  a {
    display: inline-block;
    text-decoration: none;
    width: 100%;
  }
  .moviegood {
    position: absolute;
    bottom: 3px;
    left: 3px;
    background-color: rgba(0, 0, 0, 0.77);
    color: rgb(255, 255, 255);
    font-weight: 700;
    letter-spacing: normal;
    font-size: 14px;
    line-height: 22px;
    text-align: center;
    width: 24px;
    height: 24px;
    border-radius: 4px;
    opacity: 1;
  }
  .moviegood2 {
    position: absolute;
    bottom: 3px;
    left: 3px;
    background-color: rgba(0, 0, 0, 0.77);
    color: rgb(255, 50, 50);
    font-weight: 700;
    letter-spacing: normal;
    font-size: 14px;
    line-height: 22px;
    text-align: center;
    width: 24px;
    height: 24px;
    border-radius: 4px;
    opacity: 1;
  }
  .movie_card {
    /* width: 33.333333333333336%; */
    margin-bottom: 0px;
    padding: 0 5px !important;
    /* display: inline-block; */
    /* vertical-align: top; */
    box-sizing: border-box;
    margin: 0 0 24px;
  }
</style>