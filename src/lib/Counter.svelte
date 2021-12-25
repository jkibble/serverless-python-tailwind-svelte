<script>
  import { _, dictionary } from 'svelte-i18n'
  dictionary.set({
    en: { title: 'Just a button that counts up when you click it' },
    fr: { title: 'Juste un bouton qui compte lorsque vous cliquez dessus' }
  });

  let count = 0
  const increment = () => {
    count++;
  }
</script>

<h3>
  { $_('title') }
</h3>

<button class="btn" on:click={increment}>
  Clicks: <span>{count}</span>
</button>
