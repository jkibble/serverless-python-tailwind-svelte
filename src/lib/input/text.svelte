<script>
  const id = Math.random()
    .toString(36)
    .replace(/[^a-z]+/g, "");
  let element;

  export let label = "";
  export let inputType = "text";
  export let required = false;
</script>

<div class="relative">
  <label for={id} class:required>
    {label}
  </label>
  <input
    on:blur={() => element.reportValidity()}
    bind:this={element}
    {id}
    type={inputType}
    {required}
    {...$$restProps}
  />
</div>
