<template>
  <div @click="increase">{{ count }} / {{ doubleCount }}</div>
  <div @click="changeMessage">{{ message }} / {{ reversedMessage }}</div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello world!',
      count: 0
    }
  },
  computed: {
    doubleCount() {
      return this.count * 2
    },
    reversedMessage() {
      return this.message.split('').reverse().join('')
    }
  },
  watch: {
    message(newValue) {
      console.log(newValue)
    }
  },
  created() {
    console.log(this.message)
  },
  mounted() {
    console.log(this.count)
  },
  methods: {
    increase() {
      this.count += 1
    },
    changeMessage() {
      this.message = 'Good!'
    }
  }
}
</script>

<style></style>
