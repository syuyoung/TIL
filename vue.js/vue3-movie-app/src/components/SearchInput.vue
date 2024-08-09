<template>
  <div class="container">
    <input
      v-model="title"
      class="form-control"
      type="text"
      placeholder="Search for Movies, Series & more"
      @keyup.enter="apply"
    />
    <div class="selects">
      <select
        v-for="filter in filters"
        v-model="filter.value"
        :key="filter.name"
        class="form-select"
      >
        <option v-if="filter.name === 'year'" value="">All Years</option>
        <option v-for="item in filter.items" :key="item">{{ item }}</option>
      </select>
    </div>
    <button class="btn btn-primary" @click="apply">Apply</button>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useStore } from 'vuex'

const store = useStore()
const title = ref('')
const type = ref('movie')
const number = ref(10)
const year = ref('')

const filters = reactive([
  { name: 'type', value: type, items: ['movie', 'series', 'episode'] },
  { name: 'number', value: number, items: ['10', '20', '30'] },
  {
    name: 'year',
    value: year,
    items: (() => {
      const years = []
      const thisYear = new Date().getFullYear()
      for (let i = thisYear; i >= 1985; i -= 1) {
        years.push(i)
      }
      return years
    })()
  }
])

const apply = () => {
  store.dispatch('movie/searchMovies', {
    title: title.value,
    type: type.value,
    number: number.value,
    year: year.value
  })
}
</script>

<style lang="scss" scoped>
.container {
  display: flex;

  > * {
    margin-right: 10px;
    font-size: 15px;

    &:last-child {
      margin-right: 0;
    }
  }

  .selects {
    display: flex;

    select {
      width: 120px;
      margin-right: 10px;

      &:last-child {
        margin-right: 0;
      }
    }
  }

  .btn {
    width: 120px;
    height: 50px;
    font-weight: 700;
    flex-shrink: 0;
  }
}
</style>
