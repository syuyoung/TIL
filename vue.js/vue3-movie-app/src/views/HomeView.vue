<template>
  <HeadLine />
  <SearchInput />
  <MovieList />
</template>

<script setup>
import { onMounted } from 'vue'
import { useStore } from 'vuex'

const store = useStore()

import HeadLine from '@/components/HeadLine.vue'
import SearchInput from '@/components/SearchInput.vue'
import MovieList from '@/components/MovieList.vue'

onMounted(() => {
  store.commit('movie/resetMovies')
})
</script>

<style lang="scss" scoped></style>
