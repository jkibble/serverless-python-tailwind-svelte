<script>
  import Counter from '/src/lib/Counter.svelte'
  import Table from '/src/lib/Table.svelte'
</script>

<h3>Button with counter example</h3>
<Counter />

<h3>https://picsum image load</h3>
<img src="https://picsum.photos/600/200" alt="" width="600" height="200">

<h3>Table component example</h3>
<Table />

<style>
  h3 {
    @apply mt-5 font-bold;
  }
</style>