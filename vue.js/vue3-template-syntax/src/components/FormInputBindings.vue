<template>
  <h1>{{ msg }}</h1>
  <input type="text" v-model="msg" />
  <h1>{{ checked }}</h1>
  <input type="checkbox" v-model="checked" />
  <!-- 한글일 경우 -->
  <!-- <input type="text" :value="msg" @input="msg = $event.target.value" /> -->
  <!-- <input type="text" :value="msg" @input="handler" /> -->
</template>

<script>
export default {
  data() {
    return {
      msg: 'Hello world!',
      checked: false
    }
  }
  // methods: {
  //   handler(event) {
  //     console.log(event.target.value)
  //     this.msg = event.target.value
  //   }
  // }
}
</script>

<style></style>
