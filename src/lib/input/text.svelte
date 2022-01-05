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
  <div class="text-xs flex gap-2 align-bottom">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="h-5 w-5 text-red-700 dark:bg-slate-100 rounded-full"
      viewBox="0 0 20 20"
      fill="currentColor"
    >
      <path
        fill-rule="evenodd"
        d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
        clip-rule="evenodd"
      />
    </svg>
    <span>
      {error}
    </span>
  </div>
{/if}
