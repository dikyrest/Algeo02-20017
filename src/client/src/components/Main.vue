<script setup>
import { NSpin, NMessageProvider } from 'naive-ui'
import RateInput from './RateInput.vue'
import FileInput from './FileInput.vue'
import Comparator from './Comparator.vue'

import { ref } from '@vue/reactivity'
import { getCompressedImage } from '../services/api'

const rate = ref(50)
const file = ref('')
const beforeImg = ref('')
const afterImg = ref('')

const isCompressing = ref(false)
const isLoading = ref(false)
const isError = ref(false)

const onFileChange = (info) => {
  file.value = info.file
  beforeImg.value = URL.createObjectURL(file.value.file)
  request()
}

const request = async () => {
  isLoading.value = true

  try {
    const compressed = await getCompressedImage(file.value.file)
    afterImg.value = URL.createObjectURL(compressed.file)
  } catch (e) {
    isError.value = true
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
        <Comparator
          :name="file.name"
          :beforeImg="beforeImg"
          :afterImg="afterImg"
          :isError="isError"
          @reset="reset"
          @retry="request"
        />
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
