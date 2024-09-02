<template>
  <header>
    <TheLogo />
    <div class="nav nav-pills">
      <div v-for="nav in navigations" :key="nav.name" class="nav-item">
        <RouterLink
          :to="nav.href"
          active-class="active"
          :class="{ active: isMatch(nav.path) }"
          class="nav-link"
          >{{ nav.name }}</RouterLink
        >
      </div>
    </div>
  </header>
</template>

<script setup>
import TheLogo from '@/components/TheLogo.vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const navigations = [
  { name: 'Search', href: '/' },
  {
    name: 'Movie',
    href: '/movie/tt4520988',
    path: /^\/movie/ // '/movie'
  },
  { name: 'About', href: '/about' }
]

function isMatch(path) {
  if (!path) return false
  return path.test(route.fullPath)
}
</script>

<style lang="scss" scoped>
header {
  height: 70px;
  padding: 0 40px;
  display: flex;
  align-items: center;
  .logo {
    margin-right: 40px;
  }
}
</style>
