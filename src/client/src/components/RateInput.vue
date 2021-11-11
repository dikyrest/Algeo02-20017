<script setup>
import { ref } from '@vue/reactivity';
import { NSlider } from 'naive-ui'

const emit = defineEmits(['update:value'])
const props = defineProps({
  value: {
    type: Number,
    default: 0,
  },
})

const value = ref(props.value)
</script>

<template>
  <div class="rate-input">
    <div>Tingkat kompresi: {{ value }}%</div>
    <NSlider
      v-model:value="value"
      :format-tooltip="value => value + '%'"
      @update-value="emit('update:value', value)"
    />
  </div>
</template>

<style scoped>
.rate-input {
  width: 100%;
  max-width: 500px;
}
</style>
