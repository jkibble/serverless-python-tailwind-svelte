<script>
  import Text from "/src/lib/input/text.svelte";
  export let options = [];
  let id;
</script>

<Text
  inputType="text"
  autocomplete="false"
  bind:id
  list={id + "_datalist"}
  {...$$restProps}
/>
<datalist id={id + "_datalist"}>
  {#each options as item}
    <option value={item.value} />
  {/each}
</datalist>
