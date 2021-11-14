<script setup>
import { toRef } from '@vue/reactivity';
import { NSlider, NInputNumber } from 'naive-ui'

const emit = defineEmits(['update:value'])
const props = defineProps({
  value: {
    type: Number,
    default: 0,
  },
})

const value = toRef(props, 'value')
</script>

<template>
  <div class="rate-input">
    <div>Tingkat kompresi:</div>
    <NInputNumber
      :show-button="false"
      :value="value"
      @update:value="(v) => emit('update:value', v)"
    >
      <template #suffix>%</template>
    </NInputNumber>
  </div>
</template>

<style scoped>
.rate-input {
  width: 100%;
  max-width: 500px;
}
</style>
