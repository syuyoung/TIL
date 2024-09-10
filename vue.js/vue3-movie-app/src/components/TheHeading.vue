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
    <div class="user" @click="toAbout">
      <!-- <img :src="image" :alt="name" /> -->
    </div>
  </header>
</template>

<script setup>
import TheLogo from '@/components/TheLogo.vue'
// import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
// import { useStore } from 'vuex'

// const store = useStore()
const route = useRoute()
const router = useRouter()

const navigations = [
  { name: 'Search', href: '/' },
  {
    name: 'Movie',
    href: '/movie/tt4520988',
    path: /^\/movie/ // '/movie'
  },
  { name: 'About', href: '/about' }
]

function toAbout() {
  router.push('/about')
}

function isMatch(path) {
  if (!path) return false
  return path.test(route.fullPath)
}

// const name = computed(() => store.state.about.name)
</script>

<style lang="scss" scoped>
header {
  height: 70px;
  padding: 0 40px;
  display: flex;
  align-items: center;
  position: relative;
  .logo {
    margin-right: 40px;
  }
  .user {
    width: 40px;
    height: 40px;
    padding: 6px;
    border-radius: 50%;
    box-sizing: border-box;
    background-color: $gray-200;
    cursor: pointer;
    position: absolute;
    top: 0;
    bottom: 0;
    right: 40px;
    margin: auto;
    transition: 0.4s;
    &:hover {
      background-color: darken($gray-200, 10%);
    }
    img {
      width: 100%;
    }
  }
  @include media-breakpoint-down(sm) {
    .nav {
      display: none;
    }
  }
}
</style>
