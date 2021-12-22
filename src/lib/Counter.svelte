<script>
  let count = 0
  const increment = () => {
    count++;
  }
</script>

<button class="btn" on:click={increment}>
  Clicks: <span>{count}</span>
</button>
