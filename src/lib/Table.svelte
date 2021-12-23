<!-- create a svelte component -->
<script>
  // generate nested array of random data
  const data = Array.from({ length: 25 }, () =>
    Array.from({ length: 10 }, () => Math.random().toString(36).replace(/[^a-z]+/g, ''))
  );

  const header = Array.from({ length: 10 }, () => 
    Array.from({ length: 1 }, () => Math.random().toString(36).replace(/[^a-z]+/g, ''))
  );
</script>

<div class="table prose">
  <table>
    <thead>
      {#each header as head}
        <th>{head}</th>
      {/each}
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
