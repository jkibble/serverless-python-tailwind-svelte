<script>
  import Email from "/src/lib/input/email.svelte";
  import Checkbox from "/src/lib/input/checkbox.svelte";
  import Password from "/src/lib/input/password.svelte";
  import Search from "/src/lib/input/search.svelte";
  import Date from "/src/lib/input/date.svelte";

  let form;
</script>

<h2>Different Input Components</h2>

<div class="grid gap-3 xl:grid-cols-2 sm:grid-cols-1">
  <form
    action="/"
    method="POST"
    bind:this={form}
    on:submit={() => form.reportValidity()}
  >
    <Email label="Email" name="email" required="true" />
    <Checkbox label="Checkbox" name="checkbox" />
    <Password label="Password" name="password" required="true" />
    <Search label="Search (not required)" name="search" />
    <Date label="Date" name="date" required="true" />
    <input type="submit" class="btn" value="send" />
  </form>
</div>
