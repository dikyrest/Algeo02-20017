<script setup>
import { toRef, ref } from '@vue/reactivity';
import { NSlider } from 'naive-ui'

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
    <div>Tingkat kompresi: {{ value }}%</div>
    <NSlider
      :value="value"
      :format-tooltip="value => value + '%'"
      @update:value="(v) => emit('update:value', v)"
    />
  </div>
</template>

<style scoped>
.rate-input {
  width: 100%;
  max-width: 500px;
}
</style>
