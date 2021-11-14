<script setup>
import { NCard, NButton, NIcon, NAlert } from 'naive-ui'
import { ImageArrowCounterclockwise24Regular as ImageIcon } from '@vicons/fluent'
import { ArrowDownload16Regular as DownloadIcon } from '@vicons/fluent'
import { ArrowClockwise16Regular as RefreshIcon } from '@vicons/fluent'
import { Clock20Regular as ClockIcon } from '@vicons/fluent'
import { toRefs } from '@vue/reactivity'

const props = defineProps({
  beforeImg: String,
  afterImg: String,
  beforeComment: String,
  afterComment: String,
  name: String,
  time: Number,
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
      <template #header-extra>{{ beforeComment }}</template>
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
        alignItems: 'center',
      }"
      segmented
      class="comparator-col"
    >
      <template v-if="!isError" #header-extra>{{ afterComment }}</template>
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
          <div v-if="time" class="comparator-duration">
            <NIcon size="24">
              <ClockIcon />
            </NIcon>
            <span>{{ time.toFixed(3) }} detik</span>
          </div>
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
  background: url("/assets/images/tile.png") white;
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

.comparator-duration {
  flex-grow: 1;
  display: flex;
  align-items: center;

  span {
    margin-left: 5px;
  }
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