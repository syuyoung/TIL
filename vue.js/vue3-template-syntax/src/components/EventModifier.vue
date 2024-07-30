<template>
  <!-- 로직의 처리와 별개로 화면을 처리 -->
  <div class="parent" @wheel.passive="handler">
    <div class="child"></div>
  </div>

  <!-- 정확하게 클릭했을 때 -->
  <!-- <div class="parent" @click.self="handlerA">
    <div class="child"></div>
  </div> -->
  <!-- 버블링 방지 -->
  <!-- <div class="parent" @click.capture.stop="handlerA">
    <div class="child" @click="handlerB"></div>
  </div> -->
  <!-- 캡처링, 이벤트 버블링의 반대 -->
  <!-- <div class="parent" @click.capture="handlerA">
    <div class="child" @click="handlerB"></div>
  </div> -->
  <!-- 이벤트 버블링 방지 -->
  <!-- <div class="parent" @click="handlerA">
    <div class="child" @click.stop="handlerB"></div>
  </div> -->
  <!-- 이벤트 버블링 방지 -->
  <!-- <div class="parent" @click="handlerA">
    <div class="child" @click="handlerB"></div>
  </div> -->

  <!-- 체이닝 -->
  <!-- <a href="https://naver.com" target="_blank" @click.prevent.once="handler">NAVER</a> -->
  <!-- 한번만 실행 -->
  <!-- <a href="https://naver.com" target="_blank" @click.once="handler">NAVER</a> -->
  <!-- 기본 동작 방지 -->
  <!-- <a href="https://naver.com" target="_blank" @click.prevent="handler">NAVER</a> -->
  <!-- <a href="https://naver.com" target="_blank" @click="handler">NAVER</a> -->
</template>

<script>
export default {
  methods: {
    handler(event) {
      for (let i = 0; i < 10000; i += 1) {
        console.log(event)
      }
    }

    // handlerA() {
    //   console.log('A')
    // },
    // handlerB() {
    //   console.log('B')
    // }
    // handlerB(event) {
    //   // 이벤트 버블링 방지
    //   event.stopPropagation()
    //   console.log('B')
    // }
    // handler() {
    //   console.log('ABC!')
    // handler(event) {
    // 기본 동작 방지
    // event.preventDefault()
    // console.log('ABC!')
  }
}
</script>

<style lang="scss" scoped>
.parent {
  width: 200px;
  height: 100px;
  background: royalblue;
  margin: 10px;
  padding: 10px;
  overflow: auto;
  .child {
    width: 100px;
    height: 2000px;
    background: orange;
  }
}

/* .parent {
  width: 200px;
  height: 100px;
  background: royalblue;
  margin: 10px;
  padding: 10px;
  .child {
    width: 100px;
    height: 100px;
    background: orange;
  }
} */
</style>
