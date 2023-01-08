<template>
  <div>
    <div>
      <CommentListItem
      v-for="comment in article.comment_set"
      :key="comment.id"
      :comment="comment"
      @delete-comment="deleteComment"
      />
    </div>
    <div class="comment-input-box">
      <input @keyup.enter="createComment" type="text" v-model.trim="currnetComment" placeholder="댓글을 입력하세요.">
      <div class="create-btn" @click="createComment">
        <span class="material-symbols-outlined" style="margin-top 7px;">edit</span>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommentListItem from './CommentListItem.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentList',
  components: {
    CommentListItem,
  },
  props: {
    article: Object,
  },
  data() {
    return {
      currnetComment: null,
    }
  },
  methods: {
    createComment() {
      const content = this.currnetComment
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/comments/`,
        data: {
          content: content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.currnetComment = null
          // this.$router.replace({ name: 'DetailView', params: { id: this.$route.params.id } })
          // location.reload()
        })
        .catch((err) => {
          console.log(err)
        })
      this.$emit('create-comment')
    },
    deleteComment() {
      this.$emit('delete-comment')
    }
  },
}
</script>

<style>

</style>