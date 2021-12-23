<script>
  import Counter from '/src/lib/Counter.svelte'
  import Editor from '/src/lib/Editor.svelte'
  import Table from '/src/lib/Table.svelte'
  import Timer from '/src/lib/Timer.svelte'
	
  const options = [
		{ name: 'Counter',   component: Counter },
		{ name: 'Editor',   component: Editor },
		{ name: 'Table',   component: Table },
		{ name: 'Timer',   component: Timer },
	];

  let selected = options[0];
</script>

<h3 class="font-bold mb-5">
  Component selector
</h3>

<select bind:value={selected}>
  {#each options as option}
  <option value={option}>{option.name}</option>
  {/each}
</select>

<h3>{selected.name}</h3>

<svelte:component this={selected.component}/>

<style>
  h3 {
    @apply mt-5 font-bold;
  }
</style>