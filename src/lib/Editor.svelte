<script>
  import { onMount } from "svelte";
  const id = Math.random()
    .toString(36)
    .replace(/[^a-z]+/g, "");

  onMount(() => {
    let script = document.querySelector("#hljs");
    script.addEventListener("load", function () {
      new Quill(`#${id}`, { theme: 'snow' });
    });
  });
</script>

<svelte:head>
  <link href="https://cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet">
  <script id="hljs" src="https://cdn.quilljs.com/1.3.6/quill.js"></script>
</svelte:head>

<div {id} />
