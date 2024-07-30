<template>
  <h1 :class="{ active: isActive }" @click="activate">Hello?!({{ isActive }})</h1>
  <h1 :style="[fontStyle, backgroundStyle]" @click="changeStyle">Hello?!</h1>
</template>

<script>
export default {
  data() {
    return {
      isActive: false,
      fontStyle: {
        color: 'orange',
        fontSize: '30px'
      },
      backgroundStyle: {
        backgroundColor: 'black'
      }
    }
  },
  methods: {
    activate() {
      this.isActive = true
    },
    changeStyle() {
      this.fontStyle.color = 'red'
      this.fontStyle.fontSize = '50px'
    }
  }
}
</script>

<style scoped>
.active {
  color: red;
  font-weight: bold;
}
</style>
