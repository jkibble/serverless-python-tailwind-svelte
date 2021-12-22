<script>
  const id = Math.random().toString(36).replace(/[^a-z]+/g, '');
  export let label = ''
  export let inputType = 'text'
</script>

<div class="relative">
  <label for={id} class="absolute -top-3 left-5 bg-red-100 pl-2 pr-2 rounded pb-0 text-sm">
    {label}
  </label>
  <input {id} type={inputType} {...$$restProps}>
</div>
