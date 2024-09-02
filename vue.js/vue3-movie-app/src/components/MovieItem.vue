<template>
  <RouterLink
    :to="`/movie/${movie.imdbID}`"
    :style="{ backgroundImage: `url(${movie.Poster})` }"
    class="movie"
  >
    <TheLoader v-if="imageLoading" :size="1.5" absolute />
    <div class="info">
      <div class="year">{{ movie.Year }}</div>
      <div class="title">{{ movie.Title }}</div>
    </div>
  </RouterLink>
</template>

<script setup>
import { onMounted, ref, getCurrentInstance } from 'vue'
import TheLoader from '@/components/TheLoader.vue'

const imageLoading = ref(true)

const props = defineProps({
  movie: {
    type: Object,
    default: () => ({})
  }
})

// function init() {
//   const img = document.createElement('img')
//   img.src = props.movie.Poster
//   img.addEventListener('load', () => {
//     imageLoading.value = false
//   })
// }

// methods: {
//   async init() {
//     await this.$loadImage(this.movie.poster)
//     this.imageLoading = false
//   }
// }

async function init() {
  // Vue 인스턴스의 글로벌 프로퍼티에 접근하기 위해 getCurrentInstance 사용
  const { $loadImage } = getCurrentInstance().appContext.config.globalProperties
  const poster = props.movie.Poster
  if (!poster || poster === 'N/A') {
    imageLoading.value = false
  } else {
    // 비동기로 이미지 로드
    await $loadImage(poster)
    // 이미지 로딩 상태 업데이트
    imageLoading.value = false
  }
}

onMounted(() => {
  init()
})
</script>

<style lang="scss" scoped>
.movie {
  $width: 168px;
  width: $width;
  height: calc($width * 3 / 2);
  margin: 10px;
  border-radius: 4px;
  background-color: $gray-400;
  background-size: cover;
  overflow: hidden;
  position: relative;

  &:hover::after {
    content: '';
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    border: 6px solid $primary;
  }

  .info {
    background: rgba($black, 0.3);
    width: 100%;
    padding: 14px;
    font-size: 14px;
    text-align: center;
    position: absolute;
    left: 0;
    bottom: 0;
    backdrop-filter: blur(10px);

    .year {
      color: $primary;
    }

    .title {
      color: $white;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
  }
}
</style>
