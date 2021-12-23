<script>
  import Editor from '/src/lib/Editor.svelte'
</script>

<h3 class="font-bold mb-5">
  Quill WYSISYG Editor Test
</h3>

<div class="mb-5">
  loaded from CDN using <code class="font-bold">&lt;svelte:head&gt;</code>
</div>

<Editor />

<style>
  h3 {
    @apply mt-5 font-bold;
  }
</style>