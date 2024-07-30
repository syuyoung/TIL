<template>
  <button @click="handlerA(), handlerB()">Click me!</button>
  <!-- <button @click="handler('hi', $event)">Click 1</button>
  <button @click="handler('what', $event)">Click 2</button> -->
  <!-- <button @click="handler">Click me!</button> -->
</template>

<script>
export default {
  methods: {
    handlerA() {
      console.log('A')
    },
    handlerB() {
      console.log('B')
    }
    // handler(msg, event) {
    //   console.log(msg)
    //   console.log(event)
    // }
    // handler(e) {
    //   console.log(e)
    //   console.log(e.target.textContent)
    // }
  }
}
</script>

<style></style>
