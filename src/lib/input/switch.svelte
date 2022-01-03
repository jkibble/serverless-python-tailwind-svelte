<script>
  export let label = "";
  export let toggle = false;
</script>

<label class="flex justify-between items-center p-2 relative">
  {label}
  <input
    type="checkbox"
    class="peer invisible absolute left-0 top-0 w-full h-full rounded-md"
    bind:checked={toggle}
  />
  <span
    class="w-12 h-7 flex items-center flex-shrink-0 ml-4 p-1 bg-gray-300 rounded-full after:w-5
    after:h-5 
    after:bg-white 
    after:rounded-full 
    after:shadow-md
    peer-checked:bg-green-400 duration-300 ease-in-out after:duration-300
    peer-checked:after:translate-x-5
    "
  />
</label>
