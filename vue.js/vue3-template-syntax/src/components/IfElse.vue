<template>
  <button @click="handler">Click me!</button>
  <h1 v-show="isShow">Hello?!</h1>
  <!-- <template v-if="isShow">
    <h1>Title</h1>
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
  </template> -->
  <!-- <h1 v-if="isShow">Hello?!</h1>
  <h1 v-else-if="count > 3">count > 3</h1>
  <h1 v-else>Good~</h1> -->
</template>

<script>
export default {
  data() {
    return {
      isShow: false,
      count: 0
    }
  },
  methods: {
    handler() {
      this.isShow = !this.isShow
      this.count += 1
    }
  }
}
</script>

<style></style>
