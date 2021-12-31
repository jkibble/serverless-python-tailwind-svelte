<script>
  export let title;
  export let article
</script>

<article>
  <h4>{ title }</h4>
  {#each article as paragraph}
  <p>
    { paragraph }
  </p>
  {/each}
</article>

<style>
  h4 {
    @apply font-extrabold;
  }

  p {
    @apply mt-2;
  }

  article {
    @apply bg-slate-400 p-5 rounded-lg;
  }
</style>