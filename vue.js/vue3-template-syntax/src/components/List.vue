<template>
  <button @click="handler">click me!</button>
  <ul>
    <li v-for="{ id, name } in newFruits" :key="id">{{ name }}-{{ id }}</li>
  </ul>
  <!-- <ul>
    <li v-for="fruit in newFruits" :key="fruit.id">{{ fruit.name }}-{{ fruit.id }}</li>
  </ul> -->
  <!-- <ul>
    <li v-for="(fruit, index) in fruits" :key="fruit">{{ fruit }}-{{ index + 1 }}</li>
  </ul> -->
</template>

<script>
import shortid from 'shortid'

export default {
  data() {
    return {
      fruits: ['Apple', 'Banana', 'Cherry']
      // newFruits: [
      //   { id: 0, name: 'Cpple' },
      //   { id: 1, name: 'Banana' },
      //   { id: 2, name: 'Cherry' }
      // ]
    }
  },
  computed: {
    newFruits() {
      return this.fruits.map((fruit) => ({
        id: shortid.generate(),
        name: fruit
      }))
    }
    // newFruits() {
    //   return this.fruits.map((fruit, index) => {
    //     return {
    //       id: index,
    //       name: fruit
    //     }
    //   })
  },
  methods: {
    handler() {
      this.fruits.push('Orange')
    }
  }
}
</script>

<style></style>
