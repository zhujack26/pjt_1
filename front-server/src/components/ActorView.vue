<template>

  <a class="actor-box" :href="`https://www.themoviedb.org/person/${this.actor?.id}?language=ko`">
    <div>
      <img :src="actorImgUrl" alt="">
      <p>{{actor?.name}}</p>
    </div>
  </a>
</template>

<script>
export default {
  name: "ActorView",
  props: {
    actor: Object,
  },
  computed: {
    actorImgUrl() {
      return 'https://image.tmdb.org/t/p/w300'+this.actor.profile_path
    }
  },
  mothods: {

  },
}
</script>

<style>

</style>