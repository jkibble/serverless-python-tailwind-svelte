<script>
  import Editor from '/src/lib/Editor.svelte'
  import Counter from '/src/lib/Counter.svelte'
  import { _ } from '/src/lib/i18n.js'

  console.log(window.user)
</script>

<h3 class="font-bold mb-5">
  { $_('title') }
</h3>

<div class="mb-5">
  {@html $_('subtitle') }
</div>

<Counter />

<Editor />

<style>
  h3 {
    @apply mt-5 font-bold;
  }
</style>