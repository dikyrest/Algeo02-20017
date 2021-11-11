<script setup>
import { NCard, NButton, NIcon } from 'naive-ui'
import { ImageArrowCounterclockwise24Regular as ImageIcon } from '@vicons/fluent'
import { ArrowDownload16Regular as DownloadIcon } from '@vicons/fluent'

const props = defineProps({
  beforeImg: String,
  afterImg: String,
  name: String,
})

const emit = defineEmits(['reset', 'download'])

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
      <img :src="props.beforeImg" />
      <template #footer>
        <NButton type="error" @click="(e) => emit('reset', e)">
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
      <template #header-extra>kompresi: 5 detik</template>
      <img :src="props.afterImg" />
      <template #footer>
        <a :href="props.afterImg" :download="props.name" target="__blank">
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
    </NCard>
  </div>
</template>

<style scoped>
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

img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

a {
  color: unset;
  text-decoration: none;
}
</style>