<script setup>
import { NSpin, NMessageProvider } from 'naive-ui'
import RateInput from './RateInput.vue'
import FileInput from './FileInput.vue'
import Comparator from './Comparator.vue'

import { ref } from '@vue/reactivity'
import { getCompressedImage } from '../services/api'

const rate = ref(50)
const fname = ref('')
const beforeImg = ref('')
const afterImg = ref('')

const isCompressing = ref(false)
const isLoading = ref(false)

const onFileChange = async ({ file }) => {
  isLoading.value = true

  fname.value = file.name
  beforeImg.value = URL.createObjectURL(file.file)

  try {
    const compressed = await getCompressedImage(file.file)
    afterImg.value = URL.createObjectURL(compressed.file)
  } catch (e) {
    // TODO: handle error
  } finally {
    isLoading.value = false
    isCompressing.value = true
  }
}

const reset = () => {
  URL.revokeObjectURL(beforeImg.value)
  URL.revokeObjectURL(afterImg.value)
  beforeImg.value = ''
  afterImg.value = ''
  isCompressing.value = false
}
</script>

<template>
  <main>
    <NSpin :show="isLoading">
      <RateInput v-model:value="rate" :disabled="isLoading" />
      <template v-if="!isCompressing">
        <NMessageProvider>
          <FileInput @change="onFileChange" />
        </NMessageProvider>
      </template>
      <template v-else>
        <Comparator :name="fname" :beforeImg="beforeImg" :afterImg="afterImg" @reset="reset" />
      </template>
    </NSpin>
  </main>
</template>

<style>
main {
  height: 100%;
}

.n-spin-content {
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 25px;
}
</style>
