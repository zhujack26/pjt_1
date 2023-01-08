<template>
  <div>
    <div class="backdrop" :style="{backgroundImage: `url(${backdropUrl})`}">
      <div class="backover">
        <div class="backover_poster">
          <img :src="posterUrl" :alt="posterUrl">
        </div>
        <div class="backover_text">
          <div class="backover_text_title">
            <h1>{{detailMovie?.title}}</h1>
            <span>({{createdYear}})</span>
          </div>
          <div>
            <p>{{detailMovie?.release_date.replaceAll('-', '/') }} • {{genres.join(' ')}} • {{runtime}}</p>
          </div>
          <div>
            <p>평점 ★ {{voteAvg}} • 현재 {{detailMovie.status}}</p>
          </div>
          <div class="backover_overview">
            <p class="backover_overview_t1">개요</p>
            <p class="backover_overview_t2">{{detailMovie.overview}}</p>
          </div>
          <p>출연자</p>
          <div class="actors-box">
            <ActorView
              v-for="actor in actors"
              :key="actor.id"
              :actor="actor"
            />
          </div>
        </div>
      </div>
      
    </div>
    <!-- <p>{{detailMovie}}</p> -->
    <div>
      <div class="movie-youtube-area">
        <p class="youtuve">관련 영상</p>
        <div>
        <YoutubeList :title="movieTitle"/>
        </div>
        <hr class="detail-hr">
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ActorView from '../components/ActorView.vue'
import YoutubeList from '@/components/YoutubeList'

export default {
  name: 'MovieDetailView',
  components: {
    ActorView,
    YoutubeList,
  },
  data() {
    return {
      detailMovie: null,
      actors: null,
      movieTitle: null,
    }
  },
  created() {
    this.getDetailMovie()
    this.getActors()
  },
  computed: {
    backdropUrl() {
      return 'https://image.tmdb.org/t/p/original'+this.detailMovie?.backdrop_path
    },
    posterUrl() {
      return 'https://image.tmdb.org/t/p/w300'+this.detailMovie?.poster_path
    },
    createdYear() {
      // console.log(this.detailMovie?.release_date)
      let release_date = this.detailMovie?.release_date
      release_date = release_date.substr(0, 4)
      return release_date
    },
    genres() {
      let movieGenre = this.detailMovie.genres
      const genre = movieGenre.reduce((acc, el) => {
        acc.push(el.name)
        return acc
      }, []);
      return genre
    },
    runtime() {
      const runtime = this.detailMovie.runtime
      const hour = parseInt(runtime/60)
      const min = runtime%60
      return `${hour}h ${min}m`
    },
    voteAvg() {
      return String(this.detailMovie?.vote_average).substr(0, 3)
    }
  },
  methods: {
    // http://localhost:8080/movie/436270
    getDetailMovie() {
      const API_KEY = process.env.VUE_APP_TMDB_API_KEY
      const URL = `https://api.themoviedb.org/3/movie/${this.$route.params.id}`

      axios({
        method: "get",
        url: URL,
        params: {
          api_key: API_KEY,
          language: 'ko-KR',
        }
      })
      .then((res) => {
        // console.log(res.data)
        const detailMovie = res.data
        this.detailMovie = detailMovie
        this.movieTitle = detailMovie.title
      })
    },
    getActors() {
      const API_KEY = process.env.VUE_APP_TMDB_API_KEY
      const URL = `https://api.themoviedb.org/3/movie/${this.$route.params.id}/credits`

      axios({
        method: "get",
        url: URL,
        params: {
          api_key: API_KEY,
          language: 'ko-KR',
        }
      })
      .then((res) => {
        // console.log(res.data)
        let actor = res.data.cast
        actor = actor.slice(0, 5)
        this.actors = actor
        console.log(actor)
      })
    },
  }
}
</script>

<style>
  .movie-youtube-area {
  font-size: 32px;
}
</style>