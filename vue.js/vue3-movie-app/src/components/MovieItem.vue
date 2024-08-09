<template>
  <div>{{ movie.imdbID }}</div>
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  movie: {
    type: Object,
    default: () => ({})
  }
})
</script>

<style lang="scss" scoped></style>
