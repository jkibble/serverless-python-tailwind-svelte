<script>
  import { onMount, onDestroy } from "svelte";

  const id = Math.random()
    .toString(36)
    .replace(/[^a-z]+/g, "");

  let editor;

  onMount(() => {
    let script = document.querySelector("#hljs");
    script.addEventListener("load", function () {
      editor = new Quill(`#${id}`, { theme: 'snow' });
    });
  });

  onDestroy(() => {
    document.querySelector('.ql-toolbar').remove()
  })
</script>

<svelte:head>
  <link href="https://cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet">
  <script id="hljs" src="https://cdn.quilljs.com/1.3.6/quill.js"></script>
</svelte:head>

<div {id} />
