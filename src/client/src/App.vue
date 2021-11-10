<script setup>
import { NConfigProvider, NGlobalStyle } from 'naive-ui'
import Main from './components/Main.vue'
</script>

<template>
  <NConfigProvider abstract>
    <NGlobalStyle />
    <div class="view">
      <header>
        <h1>Kompres Air&nbsp;Hangat</h1>
        <p>Kompresor&nbsp;gambar yang&nbsp;sangat&nbsp;baik.</p>
      </header>
      <Main />
      <footer>
        <div class="footer-content">&copy; Hak Cipta 2021</div>
      </footer>
    </div>
  </NConfigProvider>
</template>

<style lang="scss">
@use "normalize.css/normalize.css";

@import url("https://fonts.googleapis.com/css2?family=Sofia&display=swap");

$footer-height: 36px;

body {
  min-height: 100vh;
  position: relative;
}

#app {
  width: 100%;
  height: 100%;
  min-height: 100vh;
  display: flex;
  justify-content: center;

  .view {
    flex-basis: 1080px;
    padding-bottom: $footer-height;
    display: flex;
    flex-direction: column;

    &,
    & .footer-content {
      margin: 0 25px;
    }
  }
}

header {
  text-align: center;
  margin-top: 10vmin;
  margin-bottom: 30px;

  h1 {
    margin: 0;
    line-height: 1;
    font-size: 58px;
    font-family: "Sofia", cursive;
  }

  p {
    margin: 10px 0 0 0;
    font-size: 16px;
  }
}

footer {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 36px;
  overflow: hidden;
  display: flex;
  align-items: center;

  .footer-content {
    white-space: nowrap;
  }
}
</style>
