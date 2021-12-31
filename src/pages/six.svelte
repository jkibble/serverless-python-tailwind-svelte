<script>
  import Email from '/src/lib/input/email.svelte'
  import Checkbox from '/src/lib/input/checkbox.svelte'
  import Password from '/src/lib/input/password.svelte'
  import Search from '/src/lib/input/search.svelte'
  import Date from '/src/lib/input/date.svelte'
</script>

<h2>Different Input Components</h2>

<div class="grid gap-3 xl:grid-cols-2 sm:grid-cols-1">
  <Email label="Email" required="true" />
  <Checkbox label="Checkbox" required="true" />
  <Password label="Password" required="true" />
  <Search label="Search" required="true" />
  <Date label="Date" required="true" />
</div>