<script setup>
import { NSpin, NMessageProvider } from 'naive-ui'
import RateInput from './RateInput.vue'
import FileInput from './FileInput.vue'
import Comparator from './Comparator.vue'

import { ref, reactive, computed } from 'vue'
import { getCompressedImage } from '../services/api'
import { debounce } from '../helpers/debounce'
import { getFileSize } from '../helpers/file'

const rate = ref(50)
const onRateChange = debounce((value) => {
  if (data.file) {
    request()
  }
}, 500)

const data = reactive({
  file: null,
  compressedFile: null,
  fname: '',
  beforeUrl: '',
  afterUrl: '',
})

const onFileChange = ({ file }) => {
  data.file = file.file
  data.fname = file.name
  data.beforeUrl = URL.createObjectURL(data.file)
  data.beforeSize = getFileSize(data.file)
  request()
}

const state = reactive({
  isCompressing: false,
  isLoading: false,
  isError: false,
})

const request = async () => {
  if (!state.isLoading) {
    state.isLoading = true
    const requestRate = rate.value

    try {
      const compressed = await getCompressedImage(data.file, requestRate)
      data.compressedFile = compressed.file
      data.afterUrl = URL.createObjectURL(compressed.file)
      state.isError = false
    } catch (e) {
      console.error(e)
      state.isError = true
    } finally {
      rate.value = requestRate
      state.isLoading = false
      state.isCompressing = true
    }
  }
}

const reset = () => {
  data.file = null
  URL.revokeObjectURL(data.beforeUrl)
  URL.revokeObjectURL(data.afterUrl)
  state.isCompressing = false
}

const imgSize = computed(() => getFileSize(data.file))
const compSize = computed(() => getFileSize(data.compressedFile))
</script>

<template>
  <main>
    <NSpin :show="state.isLoading">
      <RateInput v-model:value="rate" @update:value="onRateChange" />
      <template v-if="!state.isCompressing">
        <NMessageProvider>
          <FileInput @change="onFileChange" />
        </NMessageProvider>
      </template>
      <template v-else>
        <Comparator
          :name="data.fname"
          :beforeImg="data.beforeUrl"
          :afterImg="data.afterUrl"
          :beforeComment="imgSize"
          :afterComment="compSize"
          :isError="state.isError"
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
