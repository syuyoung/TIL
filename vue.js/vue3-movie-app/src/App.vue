<script setup>
import { RouterView } from 'vue-router'
import TheHeading from '@/components/TheHeading.vue'
import TheFooter from '@/components/TheFooter.vue'
</script>

<template>
  <TheHeading />
  <RouterView />
  <TheFooter />
</template>

<style lang="scss">
@import '@/scss/main.scss';
</style>
