<script>
  import { _, dictionary } from 'svelte-i18n'
  dictionary.set({
    en: { description: 'Just a button that counts up when you click it' },
    fr: { description: 'Juste un bouton qui compte lorsque vous cliquez dessus' },
    es: { description: 'Solo un botón que cuenta cuando lo haces clic' },
  });

  let count = 0
  const increment = () => {
    count++;
  }
</script>

<h3>
  { $_('description') }
</h3>

<button class="btn" on:click={increment}>
  Clicks: <span>{count}</span>
</button>
