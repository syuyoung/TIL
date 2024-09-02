<template>
  <div class="container">
    <div :class="{ 'no-result': !movies.length }" class="inner">
      <TheLoader v-if="loading" />
      <div v-if="message" class="message">{{ message }}</div>
      <div v-else class="movies">
        <MovieItem v-for="movie in movies" :key="movie.imdbID" :movie="movie" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useStore } from 'vuex'

import MovieItem from '@/components/MovieItem.vue'
import TheLoader from '@/components/TheLoader.vue'

const store = useStore()
const movies = computed(() => store.state.movie.movies)
const message = computed(() => store.state.movie.message)
const loading = computed(() => store.state.movie.loading)
</script>

<style lang="scss" scoped>
.container {
  margin-top: 30px;

  .inner {
    background-color: $gray-200;
    padding: 10px 0;
    border-radius: 4px;
    text-align: center;

    &.no-result {
      padding: 70px 0;
    }
  }

  .message {
    color: $gray-400;
    font-size: 20px;
  }

  .movies {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
}
</style>
