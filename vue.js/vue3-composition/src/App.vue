<template>
  <!-- <Option />
  <composition /> -->
  <OptionBtn class="asd" style="color: red" color="#ff0000" @hello="log">Apple</OptionBtn>
  <CompositionBtn class="asd" style="color: red" color="#ff0000" @hello="log">Apple</CompositionBtn>
</template>

<script>
import Option from '@/components/Option.vue'
import Composition from '@/components/Composition.vue'
import OptionBtn from '@/components/OptionBtn.vue'
import CompositionBtn from '@/components/CompositionBtn.vue'

export default {
  components: {
    Option,
    Composition,
    OptionBtn,
    CompositionBtn
  },
  methods: {
    log() {
      console.log('Hello world!')
    }
  }
}
</script>

<style></style>
