<script>
  export const delay = 2000;

  let counter = 0
  setInterval(function() {
    counter++
  }, delay);
</script>

<div class="bg-blue-100">
  {counter}
</div>