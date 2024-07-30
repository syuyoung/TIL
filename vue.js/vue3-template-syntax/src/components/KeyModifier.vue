<template>
  <!-- 체이닝 -->
  <input type="text" @keydown.ctrl.shift.a="handler" />
  <!-- 케밥케이스 작성 -->
  <!-- <input type="text" @keydown.a="handler" /> -->
  <!-- <input type="text" @keydown="handler" /> -->
</template>

<script>
export default {
  methods: {
    handler() {
      console.log('Enter!!')
    }
    // handler(event) {
    //   if (event.key === 'Enter') {
    //     console.log('Enter!!')
    //   }
    // }
  }
}
</script>

<style></style>
