<script>
  import Editor from '/src/lib/Editor.svelte'
  import Counter from '/src/lib/Counter.svelte'

  import { _, dictionary, locale } from 'svelte-i18n'

  dictionary.set({
        en: {
            app: {
                title: 'Quill WYSISYG Editor Test',
                subtitle: 'loaded from CDN using <code class="font-bold">&lt;svelte:head&gt;</code>',
            },
        },
        fr: {
            app: {
                title: 'Test de l\'éditeur WYSIWYG Quill',
                subtitle: 'chargé à partir du CDN à l\'aide de <code class="font-bold">&lt;svelte:head&gt;</code>',
            },
        },
    });
    locale.set('en');

  console.log(window.user)
</script>

<h3 class="font-bold mb-5">
  { $_('app.title') }
</h3>

<div class="mb-5">
  {@html $_('app.subtitle') }
</div>

<Counter />

<Editor />

<style>
  h3 {
    @apply mt-5 font-bold;
  }
</style>