<!-- views/CreateView.vue -->
<template>
  <div>
    <div class="article-box">
      <div class="header-box">
        <h2 class="header-box_text">게시글 작성</h2>
      </div>
      
      <form @submit.prevent="createArticle">
        <div class="create-input-box">
          <input type="text" id="title" placeholder="제목을 입력해주세요" v-model.trim="title"><br>
        </div>
        <div class="create-input-box">
          <textarea id="text" placeholder="내용을 입력해주세요" v-model="content"></textarea>
        </div>
        <div class="create-input-box">
          <input type="submit" id="submit" value="작성" class="create-input-box_btn">
        </div>
      </form>
      <div class="box-btn">
      <div class="btn-d_box" @click="goArticleView">
        <span class="material-symbols-outlined btn-d_icon">list</span>
        <button class="btn-d">목록</button>
      </div>
      <div class="btn-d_box" @click="deleteContent" style="width: 75px;">
        <span class="material-symbols-outlined btn-d_icon">delete</span>
        <button class="btn-d">지우기</button>
      </div>
    </div>
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'


export default {
  name: 'CreateView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: {
          title: title,
          content: content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.$router.push({ name: 'ArticleView' })
        })
        .catch((err) => {
          console.log(err)
        })
    },
    goArticleView() {
      this.$router.push({ name: 'ArticleView' })
    },
    deleteContent() {
      this.title = null
      this.content = null
    }
  }
}
</script>

<style>

</style>
