<template>
  <div class="article-item" @click="goDetail">
    <p class="article-item_title">{{ article.title }}</p>
    <p class="article-item_content">{{ article.content }}</p>
    <p class="article-item_time">{{ displayedAt }}</p>
    <p class="article-item_username">익명</p>
    <div class="article-item_icon">
      <span class="material-symbols-outlined thumb">thumb_up</span>
      <span class="thumb">{{like_cnt}}</span>
      <span class="material-symbols-outlined chat p-l">chat_bubble</span>
      <span class="chat">{{comment_cnt}}</span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
  data() {
    return {
      comment_cnt: null,
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    goDetail() {
      this.$router.push({ name: 'ArticleDetailView', params: { id: this.article.id } })
    },
    getArticleDetail() {
      // console.log(`Token ${this.$store.state.token}`)
      // console.log(`${API_URL}/api/v1/articles/${this.article.id}`)
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.article.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          // console.log(res)
          this.like_cnt = res.data.like_article_users.length
          this.comment_cnt = res.data.comment_count
          // console.log(this.comment_count)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  computed: {
    displayedAt() {
      let createAt = new Date(this.article.created_at)
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
  }
}
</script>

<style>

</style>
