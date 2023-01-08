<template>
  <li class="movie_card">
    <span>
      <div class ="movie_border"> 
        <div class="movie_img">
          <span v-if="!isLike"  @click="likeMovie" class ="moviegood"> ♥</span>
          <span v-else @click="likeMovie" class ="moviegood2"> ♥</span>
          <span class ="number_cnt"> {{index+1}}</span>
          <img @click="goMovieDetail" :src="getTrend" :alt="movie.title" class= "movie">  
        </div>
      </div>
      <div class="context">
        <div class = "movie_title">{{ movie.title }}</div>
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
    movie: Object,
    index: Number,
  },
  data() {
    return {
      isLike: false,
      }
  },
  created() {
    this.isLikeMovie()
  },
  computed: {
    getTrend() {
      return `https://image.tmdb.org/t/p/original/${this.movie.poster_path}`
    },
  },
  methods: {
    goMovieDetail() {
      this.$router.push({ name: 'MovieDetailView', params: { id: this.movie.id } })
    },
    likeMovie() {
      this.$store.dispatch('likeMovie', this.movie.id)
      this.isLikeMovie()
    },
    isLikeMovie() {
      // console.log('!!!!!fsadfesf', this.movie)
      axios({
        method: 'get',
        url: `${API_URL}/movies/${this.movie.id}/exist/`,
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