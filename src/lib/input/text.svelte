<script>
  export const id = Math.random()
    .toString(36)
    .replace(/[^a-z]+/g, "");
  let element;
  let isValid = true;

  export let error = "invalid input";
  export let label = "";
  export let inputType = "text";
  export let required = false;
</script>

<label for={id} class:required>
  {label}
</label>
<input
  on:blur={() => (isValid = element.checkValidity())}
  bind:this={element}
  {id}
  type={inputType}
  {required}
  {...$$restProps}
/>
{#if !isValid}
  <span class="text-xs text-red-700">{error}</span>
{/if}
