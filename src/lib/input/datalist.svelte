<script>
  export let options = [];
  const id = Math.random()
    .toString(36)
    .replace(/[^a-z]+/g, "");

  export let required = false;
  export let label = "";
</script>

<label for={id} class:required>
  {label}
</label>
<input type="text" autocomplete="false" list={id} {required} {...$$restProps} />
<datalist {id}>
  {#each options as item}
    <option value={item.value} />
  {/each}
</datalist>
