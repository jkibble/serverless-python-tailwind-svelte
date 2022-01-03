<script>
  import { onMount, onDestroy } from "svelte";

  const id = Math.random()
    .toString(36)
    .replace(/[^a-z]+/g, "");

  let editor;
  let toolbar;

  onMount(() => {
    let script = document.querySelector("#hljs");
    script.addEventListener("load", function () {
      editor = new Quill(`#${id}`, { theme: "snow" });
      toolbar = editor.container.previousElementSibling;
    });
  });

  onDestroy(() => {
    toolbar.remove(); // toolbar is created outside editor div and must be destroyed manually when unloading editor
  });
</script>

<svelte:head>
  <link href="https://cdn.quilljs.com/1.3.6/quill.snow.css" rel="stylesheet" />
  <script id="hljs" src="https://cdn.quilljs.com/1.3.6/quill.js"></script>
  <title>Title set from &lt;svelte:head&gt;</title>
</svelte:head>

<div {id} />
