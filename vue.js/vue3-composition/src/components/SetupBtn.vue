<template>
  <div v-bind="$attrs" class="btn" @click="hello"><slot></slot></div>
</template>

<script setup>
import { onMounted, defineProps, defineEmits, useAttrs } from 'vue'

const props = defineProps({
  color: {
    type: String,
    default: 'gray'
  }
})

const emit = defineEmits(['hello'])
const attrs = useAttrs()

function hello() {
  emit('hello')
}

onMounted(() => {
  console.log(props.color)
  console.log(attrs)
})
</script>

<style lang="scss" scoped></style>
