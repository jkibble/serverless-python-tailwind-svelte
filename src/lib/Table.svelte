<!-- create a svelte component -->
<script>
  import { readable } from "svelte/store";

  const getData = async () => {
    const res = await fetch("/table");
    if (!res.ok) throw new Error("Bad response");
    return await res.json();
  };

  const data = readable({ header: [], body: [] }, (set) => {
    getData()
      .then(set)
      .catch((err) => {
        console.error("Failed to fetch", err);
      });
    return () => {};
  });

  // // generate nested array of random data
  // const data = Array.from({ length: 25 }, () =>
  //   Array.from({ length: 10 }, () =>
  //     Math.random()
  //       .toString(36)
  //       .replace(/[^a-z]+/g, "")
  //   )
  // );

  // const header = Array.from({ length: 10 }, () =>
  //   Array.from({ length: 1 }, () =>
  //     Math.random()
  //       .toString(36)
  //       .replace(/[^a-z]+/g, "")
  //   )
  // );
</script>

<table class="min-w-full divide-y divide-gray-500">
  <thead class="bg-slate-200 dark:bg-slate-700">
    {#each $data.header as head}
      <th
        class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider"
        >{head}</th
      >
    {/each}
  </thead>
  <tbody class="divide-y divide-gray-500">
    {#each $data.body as row}
      <tr>
        {#each row as cell}
          <td class="px-6 py-4 whitespace-nowrap">{cell}</td>
        {/each}
      </tr>
    {/each}
  </tbody>
</table>
