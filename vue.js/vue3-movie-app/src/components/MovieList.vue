<template>
  <div class="container">
    <div class="inner">
      <MovieItem v-for="movie in movies" :key="movie.imdbID" :movie="movie" />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex'

import MovieItem from '@/components/MovieItem.vue'

const store = useStore()
const movies = computed(() => store.state.movie.movies)
</script>

<style lang="scss" scoped></style>
