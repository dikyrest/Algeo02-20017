<script setup>
import { NSpin, NMessageProvider } from 'naive-ui'
import RateInput from './RateInput.vue'
import FileInput from './FileInput.vue'
import Comparator from './Comparator.vue'

import { ref, watch } from 'vue'
import { getCompressedImage } from '../services/api'
import { debounce } from '../helpers/debounce'

const rate = ref(50)
const onRateChange = debounce((value) => {
  if (file) {
    request()
  }
}, 1000)

let file = null
const fname = ref('')
const beforeImg = ref('')
const afterImg = ref('')

const onFileChange = (info) => {
  file = info.file.file
  fname.value = info.file.name
  beforeImg.value = URL.createObjectURL(file)
  request()
}

const isCompressing = ref(false)
const isLoading = ref(false)
const isError = ref(false)

const request = async () => {
  isLoading.value = true

  try {
    const compressed = await getCompressedImage(file)
    afterImg.value = URL.createObjectURL(compressed.file)
  } catch (e) {
    isError.value = true
  } finally {
    isLoading.value = false
    isCompressing.value = true
  }
}

const reset = () => {
  file = null
  URL.revokeObjectURL(beforeImg.value)
  URL.revokeObjectURL(afterImg.value)
  beforeImg.value = ''
  afterImg.value = ''
  fname.value = ''
  isCompressing.value = false
}
</script>

<template>
  <main>
    <NSpin :show="isLoading">
      <RateInput v-model:value="rate" @update:value="onRateChange" />
      <template v-if="!isCompressing">
        <NMessageProvider>
          <FileInput @change="onFileChange" />
        </NMessageProvider>
      </template>
      <template v-else>
        <Comparator
          :name="fname"
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
