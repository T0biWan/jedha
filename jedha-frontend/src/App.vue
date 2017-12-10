<template>
<div id="app">
  <hero title="Jedha" subtitle="We fight the lack of labeled datasets for deep learning through distributed user input"></hero>
  <div class="container">
    <div class="box">
      <div class="field has-addons has-addons-centered">
        <div class="control is-expanded">
          <input class="input" type="text" placeholder="Label">
        </div>
        <div class="control">
          <a class="button is-info">Send</a>
        </div>
      </div>
    </div>

  </div>
</div>
</div>
</template>

<script>
import hero from "./components/hero.vue"

export default {
  name: 'app',
  components: {
    'hero': hero,
  },
}
</script>

<style lang="scss"></style>
