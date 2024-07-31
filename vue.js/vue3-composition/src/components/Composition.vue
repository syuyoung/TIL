<template>
  <div @click="increase">{{ count }} / {{ doubleCount }}</div>
  <div @click="changeMessage">{{ message }} / {{ reverseMessage }}</div>
</template>

<script>
import { computed, ref, watch, onMounted } from 'vue'
export default {
  setup() {
    const count = ref(0)
    function increase() {
      // value를 통해 해당하는 내용 접근
      count.value += 1
    }
    const doubleCount = computed(() => {
      return count.value * 2
    })

    const message = ref('Hello world!')
    const reverseMessage = computed(() => {
      return message.value.split('').reverse().join('')
    })
    watch(message, (newValue) => {
      console.log(newValue)
    })
    function changeMessage() {
      message.value = 'Good!'
    }
    console.log(message.value)

    onMounted(() => {
      console.log(count.value)
    })

    return {
      // 속성과 이름이 같으면 생략
      // count: count
      count,
      increase,
      doubleCount,
      message,
      changeMessage,
      reverseMessage
    }
  }
}
</script>

<style></style>
