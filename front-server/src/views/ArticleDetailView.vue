<template>
  <div class="article-box">
    <div class="header-box">
      <h2 class="header-box_text">영화게시판</h2>
    </div>
    <hr class="hr">
    <div class="detail-box">
      <div class="detail-box_pro">
        <img src="@/assets/profile.png" alt="">
        <div class="detail-box_smbox">
          <p class="detail-box_name">익명</p>
          <p class="detail-box_time">{{displayedAt(article.created_at)}}</p>
        </div>
      </div>
      <h2 class="detail-box_text">{{ article?.title }}</h2>
      <p class="detail-box_content">{{ article?.content }}</p>

      <div class="detail-box_text">
        <span class="material-symbols-outlined thumb">thumb_up</span>
        <span class="thumb">{{like_cnt}}</span>
        <span class="material-symbols-outlined chat p-l">chat_bubble</span>
        <span class="chat">{{comment_cnt}}</span>
      </div>
      <div class="pp">
        <div @click="likeArticle" :class="{'q-box': likeMine, 'g-box': !likeMine}">
          <div class="g-box_inner">
            <span class="material-symbols-outlined g-box_inner_thumb">thumb_up</span>
            <span class="g-box_inner_text">공감</span>
          </div>
        </div>
        <div @click="badwordFilter" :class="{'n-box': badwordFilterOn, 'f-box':!badwordFilterOn}">
          <div class="f-box_inner">
            <span class="material-symbols-outlined">mood_bad</span>
            <span class="f-box_inner_text">비속어 필터</span>
          </div>
        </div>

      </div>
    </div>
    <CommentList :article="article" @create-comment="createComment" @delete-comment="deleteComment" ref="commentRef"/>
    <div class="box-btn">
      <div class="btn-d_box" @click="goArticleView">
        <span class="material-symbols-outlined btn-d_icon">list</span>
        <button class="btn-d">목록</button>
      </div>
      <div class="btn-d_box" @click="deleteArticle">
        <span class="material-symbols-outlined btn-d_icon">delete</span>
        <button class="btn-d">삭제</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentList from '../components/CommentList.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetailView',
  components: {
    CommentList,
  },
  data() {
    return {
      article: null,
      comment_cnt: null,
      like_cnt: null,
    }
  },
  created() {
    this.getArticleDetail()
  },
  computed: {
    badwordFilterOn() {
      return this.$store.state.badwordFilter
    },
    likeMine() {
      let mylike = false
      const likeUsers = this.article.like_article_users
      // console.log(likeUsers)
      const currentUser = this.$store.state.userid
      console.log('11111',currentUser)
      if (likeUsers.includes(this.$store.state.userid)) {
        mylike = true
      }
      console.log(mylike)
      return mylike
    },
  },
  methods: {
    getArticleDetail() {
      // console.log(`Token ${this.$store.state.token}`)
      // console.log(`${API_URL}/api/v1/articles/${this.$route.params.id}`)
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          // console.log('!!!!', res.data)
          this.article = res.data
          this.like_cnt = this.article.like_article_users.length
          this.comment_cnt = this.article.comment_count
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteArticle() {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/articles/${this.article.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.$router.push({ name: 'ArticleView' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    likeArticle() {
      console.log(`${API_URL}/api/v1/${this.article.id}/like/`)
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/${this.article.id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.getArticleDetail()
        })
    },
    displayedAt(at) {
      let createAt = new Date(at)
      const milliSeconds = new Date() - createAt
      const seconds = milliSeconds / 1000
      if (seconds < 60) return `방금 전`
      const minutes = seconds / 60
      if (minutes < 60) return `${Math.floor(minutes)}분 전`
      const hours = minutes / 60
      if (hours < 24) return `${Math.floor(hours)}시간 전`
      const days = hours / 24
      if (days < 7) return `${Math.floor(days)}일 전`
      const weeks = days / 7
      if (weeks < 5) return `${Math.floor(weeks)}주 전`
      const months = days / 30
      if (months < 12) return `${Math.floor(months)}개월 전`
      const years = days / 365
      return `${Math.floor(years)}년 전`
    },
    goArticleView() {
      this.$router.push({ name: 'ArticleView' })
    },
    commentScroll() {
      this.$nextTick(() => {
        const commentRef = this.$refs.commentRef
        // console.log(commentRef.$el.scrollHeight)
        window.scrollTo({ top: commentRef.$el.scrollHeight, behavior: 'smooth' })
      })
    },
    async createComment() {
      await this.getArticleDetail()
      await this.commentScroll()
    },
    deleteComment() {
      this.getArticleDetail()
    },
    badwordFilter() {
      this.$store.commit('BADWORD_FILTER')
    },
    
  },
}
</script>
