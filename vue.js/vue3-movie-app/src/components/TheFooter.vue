<template>
  <footer>
    <TheLogo />
    <a href="https://github.com/syuyoung" target="_blank"
      >(c){{ new Date().getFullYear() }} YUYOUNG</a
    >
  </footer>
</template>

<script setup>
import TheLogo from '@/components/TheLogo.vue'
</script>

<style lang="scss" scoped>
footer {
  padding: 70px 0;
  text-align: center;
  opacity: 0.3;
  .logo {
    display: block;
    margin-bottom: 4px;
  }
}
</style>
