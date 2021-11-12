<script setup>
import { NCard, NButton, NIcon, NAlert } from 'naive-ui'
import { ImageArrowCounterclockwise24Regular as ImageIcon } from '@vicons/fluent'
import { ArrowDownload16Regular as DownloadIcon } from '@vicons/fluent'
import { ArrowClockwise16Regular as RefreshIcon } from '@vicons/fluent'
import { toRefs } from '@vue/reactivity'

const props = defineProps({
  beforeImg: String,
  afterImg: String,
  name: String,
  isError: Boolean,
})

const { beforeImg, afterImg, name, isError } = toRefs(props)

const emit = defineEmits(['reset', 'retry'])

</script>

<template>
  <div class="comparator">
    <NCard
      title="sebelum"
      header-style="padding: 10px 20px;"
      content-style="padding: 0;"
      :footer-style="{
        padding: '10px',
        display: 'flex',
        justifyContent: 'flex-end',
      }"
      segmented
      class="comparator-col"
    >
      <div class="comparator-img">
        <img :src="beforeImg" />
      </div>
      <template #footer>
        <NButton type="error" @click="() => emit('reset')">
          <template #icon>
            <NIcon>
              <ImageIcon />
            </NIcon>
          </template>
          Ganti Gambar
        </NButton>
      </template>
    </NCard>
    <NCard
      title="sesudah"
      header-style="padding: 10px 20px;"
      content-style="padding: 0;"
      :footer-style="{
        padding: '10px',
        display: 'flex',
        justifyContent: 'flex-end',
      }"
      segmented
      class="comparator-col"
    >
      <template v-if="!isError" #header-extra>kompresi: 5 detik</template>
      <div class="comparator-img">
        <img :src="isError ? beforeImg : afterImg" :class="isError ? 'error' : ''" />
        <div v-if="isError" class="error-msg">
          <NAlert title="Kompresi Gagal" type="error" class="alert">Silakan mencoba kembali.</NAlert>
        </div>
      </div>
      <template #footer>
        <template v-if="isError">
          <NButton type="info" @click="() => emit('retry')">
            <template #icon>
              <NIcon>
                <RefreshIcon />
              </NIcon>
            </template>
            Coba lagi
          </NButton>
        </template>
        <template v-else>
          <a :href="afterImg" :download="name" target="__blank">
            <NButton type="primary">
              <template #icon>
                <NIcon>
                  <DownloadIcon />
                </NIcon>
              </template>
              Unduh
            </NButton>
          </a>
        </template>
      </template>
    </NCard>
  </div>
</template>

<style scoped lang="scss">
.comparator {
  width: 100%;
  height: 100%;
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.comparator-col {
  flex-basis: 350px;
  flex-grow: 1;
}

.comparator-img {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: url("/assets/images/tile.png");
  background-size: auto 30px;
}

img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

a {
  color: unset;
  text-decoration: none;
}

.error-msg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);

  .alert {
    margin: 0 15px;
  }
}
</style>