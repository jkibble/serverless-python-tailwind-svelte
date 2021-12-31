<script>
  import { LoremIpsum } from "lorem-ipsum";
  const lorem = new LoremIpsum({
    sentencesPerParagraph: {
      max: 8,
      min: 4,
    },
    wordsPerSentence: {
      max: 16,
      min: 4,
    },
  });

  import Blog from "/src/lib/Post.svelte";
</script>

<h2>Responsive Blog Posts</h2>

<div class="grid gap-3 xl:grid-cols-2 sm:grid-cols-1">
  {#each Array(5) as i}
    <Blog title={lorem.generateSentences(1)} article={lorem.generateParagraphs(3).split('\n')} />
  {/each}
</div>