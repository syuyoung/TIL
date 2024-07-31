<template>
  <child />
  <!-- <child :msg="msg" /> -->
</template>

<script>
import Child from '@/components/Child.vue'
export default {
  components: { Child }
  // props: {
  //   msg: {
  //     type: String,
  //     default: ''
  //   }
  // }
}
</script>

<style></style>
