<template>
  <h1>{{ msg }}</h1>
  <!-- 공백 제거 -->
  <input type="text" v-model.trim="msg" />
  <!-- 데이터 타입이 숫자로 유지해야 할 때 -->
  <!-- <input type="text" v-model.number="msg" /> -->
  <!-- 값이 바뀔 때 갱신 -->
  <!-- <input type="text" v-model.lazy="msg" /> -->
  <!-- <input type="text" :value="msg" @change="msg = $event.target.value" /> -->
</template>

<script>
export default {
  data() {
    return {
      // msg: 123
      msg: 'Hello world!'
    }
  },
  watch: {
    msg() {
      console.log(this.msg)
      // 공백 제거
      // console.log(this.msg.trim())
      // console.log(typeof this.msg)
    }
  }
}
</script>

<style></style>
