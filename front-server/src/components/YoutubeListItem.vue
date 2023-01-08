<template>
  <li class="youtube-list-item">
    <v-dialog
      v-model="dialog"
      hide-overlay
      width="1000px"
    >
    <template v-slot:activator="{ on, attrs }">
      <img
        :src="imgSrc" alt="thumbnail"
        v-bind="attrs"
        v-on="on">
    </template>
      <div class="youtube-dialog-card">
        <div class="youtube-container">
          <iframe :src="videoURL" frameborder="0"></iframe>
        </div>
      </div>
    </v-dialog>
  </li>
</template>

<script>
export default {
  name: 'YoutubeListItem',
  data() {
    return {
      dialog: false
    }
  },
  props: {
    video: {
      type: Object,
      required: true
    }
  },
  computed: {
    imgSrc() {
      return this.video.snippet.thumbnails.high.url
    },
    videoURL: function () {
      const { videoId } = this.video.id
      return `https://www.youtube.com/embed/${videoId}`
    },
  }
}
</script>

<style>
  /* .youtube-list .youtube-list-item:focus,
  .youtube-list .youtube-list-item:hover {
  transform: scale(1.4);
  z-index: 1;
} */

  /* .youtube-list .youtube-list-item {
    transform: scale(1.4)
  } */
  .youtube-list:focus-within ~ .youtube-list-item,
  .youtube-list:hover ~ .youtube-list-item {
  transform: translateX(-15%);
}

  .youtube-list-item:focus  .youtube-list-item,
  .youtube-list-item:hover  .youtube-list-item {
  transform: translateX(15%);
}

  .youtube-list-item {
  display: flex;
  margin-bottom: 1rem;
  cursor: pointer;
  transition: transform 500ms;
}

  .youtube-list-item:hover {
  background: #eee;
}

  .youtube-list-item > img {
  height: fit-content;
  width: 200px;
  border: 1px solid #eee;
}

/* youtube dialog */
  .youtube-dialog-card {
  display: flex;
  flex-flow: column wrap;
  background-color: #000000;
}

  .youtube-dialog-toolbar {
  height: 56px;
}

  .youtube-container > iframe {
  /* position: absolute; */
  /* top: 25%;
  left: 25%;
  width: 50%;
  height: 50%; */
}

iframe {
  overflow-x: hidden;
  overflow: auto;
  width: 460px;
  height: 280px;
}
@media screen and (max-width: 1200px) {
    iframe {
  overflow-x: hidden;
  overflow: auto;
  width: 100%;
  height: 100%;
}
  }
</style>
