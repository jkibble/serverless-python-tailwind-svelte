<script>
  export let options = [];
  const id = Math.random()
    .toString(36)
    .replace(/[^a-z]+/g, "");
</script>

<input type="text" autocomplete="false" list={id} />
<datalist {id}>
  {#each options as item}
    <option value={item.value}>{item.value}</option>
  {/each}
</datalist>
