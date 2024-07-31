<template>
  <hello ref="hello" />
  <!-- <h1 ref="hello">Hello World!</h1> -->
  <!-- provide inject -->
  <!-- <button @click="message = 'Good?'">Click!</button>
  <h1>App: {{ message }}</h1>
  <parent /> -->
  <!-- <Parent :msg="message" /> -->
  <!-- slot -->
  <!-- <MyBtn>
    <template #icon>
      <span>(B)</span>
    </template>
    <template v-slot:text>
      <span>Banana</span>
    </template>
  </MyBtn> -->
  <!-- emit -->
  <!-- @click 이름 바꿔도 상관 없으나 정의를 해야됨 -->
  <!-- <MyBtn @click="log" @change-msg="logMsg">Banana</MyBtn> -->
  <!-- 상속 -->
  <!-- <MyBtn class="asd" style="color: red" title="Hello world!">Banana</MyBtn> -->
  <!-- 컴포넌트 기초 -->
  <!-- <MyBtn :color="color"><span style="color: red">Banana</span></MyBtn>
  <MyBtn large color="royalblue">Apple</MyBtn>
  <MyBtn>Cherry</MyBtn>
  <button>Banana</button> -->
</template>

<script>
import MyBtn from '@/components/MyBtn.vue'
import Parent from '@/components/Parent.vue'
import { computed } from 'vue'
import Hello from '@/components/Hello.vue'

export default {
  components: {
    MyBtn,
    Parent,
    Hello
  },

  mounted() {
    console.log(this.$refs.hello.$refs.good)
  }

  // data() {
  //   return {
  //     message: 'Hello World!'
  //   }
  // },
  // provide() {
  //   return {
  //     msg: computed(() => this.message)
  //   }
  // }

  // methods: {
  //   log(event) {
  //     console.log('Click!!'), console.log(event)
  //   },
  //   logMsg(msg) {
  //     console.log(msg)
  //   }
  // }

  // data() {
  //   return {
  //     color: '#000'
  //   }
  // }
}
</script>

<style></style>
