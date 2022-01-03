<script>
  import "/src/style.css";
  import Switch from "/src/lib/input/switch.svelte";

  let shown = false;
  let isDarkMode = false;

  $: if (isDarkMode) {
    document.querySelector("html").classList.add("dark");
  } else {
    document.querySelector("html").classList.remove("dark");
  }
</script>

<nav>
  <div class="flex justify-between items-center p-1 bg-inherit">
    <!-- logo -->
    <div class="flex items-center">
      <a href="/" class="mr-3">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-4 w-4"
          viewBox="0 0 24 24"
          stroke="currentColor"
          ><path
            d="M.87 18.257c-.248.382-.53.875-.763 1.245a.764.764 0 0 0 .255 1.04l4.965 3.054a.764.764 0 0 0 1.058-.26c.199-.332.454-.763.733-1.221 1.967-3.247 3.945-2.853 7.508-1.146l4.957 2.337a.764.764 0 0 0 1.028-.382l2.364-5.346a.764.764 0 0 0-.382-1 599.851 599.851 0 0 1-4.965-2.361C10.911 10.97 5.224 11.185.87 18.257zM23.131 5.743c.249-.405.531-.875.764-1.25a.764.764 0 0 0-.256-1.034L18.675.404a.764.764 0 0 0-1.058.26c-.195.335-.451.763-.734 1.225-1.966 3.246-3.945 2.85-7.508 1.146L4.437.694a.764.764 0 0 0-1.027.382L1.046 6.422a.764.764 0 0 0 .382 1c1.039.49 3.105 1.467 4.965 2.361 6.698 3.246 12.392 3.029 16.738-4.04z"
          /></svg
        >
      </a>
      <!-- primary nav -->
      <div class="space-x-1">
        <a href="/one">App One</a>
        <a href="/two">App Two</a>
        <a href="/three">App Three</a>
        <a href="/four">App Four</a>
        <a href="/five">App Five</a>
        <a href="/six">App Six</a>
      </div>
    </div>
    <!-- secondary nav -->
    <div>
      <Switch label="Dark Mode" bind:toggle={isDarkMode} />
    </div>
    <!-- language selector -->
    <div class="dropdown inline-block relative bg-inherit">
      <button
        on:click={() => (shown = !shown)}
        class="text-grey-700 font-semibold py-2 px-4 rounded inline-flex items-center"
      >
        <span class="mr-1">Language</span>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-4 w-4"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M19 9l-7 7-7-7"
          />
        </svg>
      </button>
      {#if shown}
        <ul class="dropdown-menu absolute bg-inherit">
          <li>
            <a class="block py-2 px-4 rounded-t" href="/language/en">English</a>
          </li>
          <li>
            <a class="block py-2 px-4" href="/language/fr">French</a>
          </li>
          <li>
            <a class="block py-2 px-4 rounded-b" href="/language/es">Spanish</a>
          </li>
        </ul>
      {/if}
    </div>
  </div>
  <!-- mobile menu -->
</nav>

<style>
  a:hover {
    @apply bg-blue-400 rounded;
  }

  a {
    @apply px-3 py-2;
  }
</style>
