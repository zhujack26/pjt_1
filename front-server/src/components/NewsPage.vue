<template>
  <div>
    <div 
      class="article-item"
      v-for="news in crawledNews"
      :key="news.id"
    >
      <a class="news-a" :href="`${news.url}`">{{news.title}}</a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import cheerio from 'cheerio'

export default {
  name: 'NewsPage',
  data() {
    return {
      crawledNews: null,
    }
  },
  created() {
    this.getNews()
  },
  methods: {
    getNews() {

      axios({
        method: 'get',
        url: '/topics/cyx5k2q66qvt'
      })
      .then((res) => {
        let crawledNews = []

        console.log(res)
        const $ = cheerio.load(res.data)

        $('.bbc-v8cf3q a').map((i, element) => {
          // console.log(element)
          crawledNews[i] = {
            'url': element.attribs.href,
            'title': element.children[0].data
          }
        })

        console.log(crawledNews)
        this.crawledNews = crawledNews
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>