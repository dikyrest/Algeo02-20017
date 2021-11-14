<script setup>
import { NUpload, NUploadDragger, NIcon, NH2, NP, useMessage } from 'naive-ui'
import { ImageAdd24Regular as Icon } from '@vicons/fluent'
import { ref } from '@vue/reactivity'

const emit = defineEmits(['change'])

const types = [
  'image/png',
  'image/jpeg',
  'image/gif',
  'image/bmp',
]

const draggerClass = ref('')
const message = useMessage()

const beforeUpload = async ({ file }) => {
  if (!types.includes(file.file.type)) {
    message.error(`Format file ${file.file.type} tidak didukung!`)
    draggerClass.value = 'dragger-error'

    setTimeout(() => {
      draggerClass.value = ''
    }, 850)

    return false
  }

  return true
}
</script>

<template>
  <NUpload :show-file-list="false" @before-upload="beforeUpload" @change="emit('change', $event)">
    <NUploadDragger :class="draggerClass">
      <NIcon size="48">
        <Icon />
      </NIcon>
      <NH2 style="margin: 10px 0 0 0;">Unggah gambar&nbsp;Anda di sini</NH2>
      <NP depth="3" style="margin: 10px 0 0 0;">
        Tekan&nbsp;di&nbsp;sini
        atau&nbsp;geser&nbsp;file&nbsp;gambar&nbsp;Anda
        ke&nbsp;area&nbsp;ini
      </NP>
      <NP style="margin: 5px 0 0 0;">Format yang didukung: JPEG,&nbsp;PNG, GIF,&nbsp;dan&nbsp;BMP</NP>
    </NUploadDragger>
  </NUpload>
</template>

<style lang="scss">
.n-spin-container,
.n-spin-content,
.n-upload {
  width: 100%;
}

.n-upload {
  display: flex;
  justify-content: center;
}

.n-upload-trigger {
  flex-basis: 500px;
}

.n-upload-dragger {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>

<style scoped lang="scss">
.dragger-error {
  animation: shake 0.82s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
  transform: translate3d(0, 0, 0);
  backface-visibility: hidden;
  perspective: 1000px;

  &,
  &:hover {
    /* TODO: colors */
    border-color: red;
    background-color: coral;
  }
}

@keyframes shake {
  10%,
  90% {
    transform: translate3d(-1px, 0, 0);
  }

  20%,
  80% {
    transform: translate3d(2px, 0, 0);
  }

  30%,
  50%,
  70% {
    transform: translate3d(-4px, 0, 0);
  }

  40%,
  60% {
    transform: translate3d(4px, 0, 0);
  }
}
</style>
