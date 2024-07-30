<template>
  <h1>{{ count }}</h1>
</template>

<script>
export default {
  data() {
    return {
      count: 2
    }
  },
  beforeCreate() {
    console.log('Before Create!', this.count)
  },
  created() {
    console.log('created!', this.count)
    console.log(document.querySelector('h1'))
  },
  beforeMount() {
    console.log('Before Mount!')
    console.log(document.querySelector('h1'))
  },
  mounted() {
    console.log('mounted!')
    console.log(document.querySelector('h1'))
  }
}
</script>

<style></style>
