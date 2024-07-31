<template>
  <div class="btn">
    <slot name="icon"></slot>
    <slot name="text"></slot>
  </div>
  <!-- emit -->
  <!-- <input type="text" v-model="msg" /> -->
  <!-- 더블클릭 -->
  <!-- <h1 @dblclick="$emit('click', $event)">ABC</h1> -->
  <!-- <h1 @click="$emit('click')">ABC</h1> -->
  <!-- 하나만 작성 시 최상위 요소 -->
  <!-- <div class="btn"><slot></slot></div> -->
  <!-- 하나 이상일때 원하는 속성을 연결하고 싶을 때 -->
  <!-- <h1 v-bind="$attrs"></h1> -->
  <!-- <h1 :class="$attrs.class" :style="$attrs.style"></h1> -->
  <!-- 최상위 요소가 하나만 있을 시 상속됨 -->
  <!-- <div></div> -->
  <!-- <div :class="{ large }" :style="{ backgroundColor: color }" class="btn"><slot></slot></div> -->
</template>

<script>
export default {
  // emits: ['click', 'changeMsg'],
  // data() {
  //   return {
  //     msg: ''
  //   }
  // },
  // watch: {
  //   msg() {
  //     this.$emit('changeMsg', this.msg)
  //   }
  // }
  // 상속
  // 최상위 요소가 하나만 있을 때 상속하지 않는 옵션
  // inheritAttrs: false,
  // created() {
  //   console.log(this.$attrs)
  // }
  // 컴포넌트 기초
  // props: {
  //   color: {
  //     type: String,
  //     default: 'gray'
  //   },
  //   large: {
  //     type: Boolean,
  //     default: false
  //   }
  // }
}
</script>

<style lang="scss" scoped>
.btn {
  display: inline-block;
  margin: 4px;
  padding: 6px 12px;
  border-radius: 4px;
  background: gray;
  color: white;
  cursor: pointer;

  &.large {
    font-size: 20px;
    padding: 10px 20px;
  }
}
</style>
