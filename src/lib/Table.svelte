<!-- create a svelte component -->
<script>
  // generate nested array of random data
  const data = Array.from({ length: 25 }, () =>
    Array.from({ length: 5 }, () => Math.random().toString(36).replace(/[^a-z]+/g, ''))
  );
</script>

<div class="table">
  <table>
    <thead>
      <th>asldj</th>
      <th>lkj</th>
      <th>sdfasd</th>
      <th>klj</th>
      <th>lkj</th>
    </thead>
    <tbody>
      {#each data as row}
        <tr>
          {#each row as cell}
            <td>{cell}</td>
          {/each}
        </tr>
      {/each}
    </tbody>
  </table>
</div>
