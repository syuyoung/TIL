<template>
  <div>Child: {{ msg }}</div>
</template>

<script>
export default {
  inject: ['msg']
  // props: {
  //   msg: {
  //     type: String,
  //     default: ''
  //   }
  // }
}
</script>

<style></style>
