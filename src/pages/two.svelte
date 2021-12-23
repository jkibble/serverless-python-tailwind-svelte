<svelte:head>
  <title>Here is the two page title from &lt;svelte:head&gt;</title>
</svelte:head>

<h3>
  Tailwind CSS Form test page
</h3>
<div class="grid grid-cols-1 md:grid-cols-2 gap-6 items-start">
  <div class="grid grid-cols-1 gap-6">
      <label>
        <span>Input (text)</span>
        <input type="text" placeholder="john@example.com">
      </label>
      <label>
        <span>Input (email)</span>
        <input type="email" placeholder="john@example.com">
      </label>
      <label>
        <span>Input (email, multiple)</span>
        <input type="email" multiple="" placeholder="john@example.com">
      </label>
      <label>
        <span>Input (password)</span>
        <input type="password" placeholder="john@example.com">
      </label>
      <label>
        <span>Input (date)</span>
        <input type="date">
      </label>
      <label>
        <span>Input (datetime-local)</span>
        <input type="datetime-local">
      </label>
      <label>
        <span>Input (month)</span>
        <input type="month">
      </label>
      <label>
        <span>Input (number)</span>
        <input type="number">
      </label>
      <label>
        <span>Input (search)</span>
        <input type="search">
      </label>
      <label>
        <span>Input (time)</span>
        <input type="time">
      </label>
      <label>
        <span>Input (week)</span>
        <input type="week">
      </label>
  </div>
  <div class="grid grid-cols-1 gap-6">
    <label>
      <span>Input (tel)</span>
      <input type="tel" multiple="" placeholder="john@example.com">
    </label>
    <label>
      <span>Input (url)</span>
      <input type="url" multiple="" placeholder="john@example.com">
    </label>
    <label>
      <span>Select</span>
      <select>
        <option>Option 1</option>
        <option>Option 2</option>
      </select>
    </label>
    <label>
      <span>Select (multiple)</span>
      <select multiple="true">
        <option>Option 1</option>
        <option>Option 2</option>
        <option>Option 3</option>
        <option>Option 4</option>
        <option>Option 5</option>
      </select>
    </label>
    <label>
      <span>Textarea</span>
      <textarea rows="3" placeholder="Enter some long form content."></textarea>
    </label>
    <div>
      <span>Checkboxes</span>
      <div>
        <div>
          <label>
            <input type="checkbox" checked="">
            <span>Option 1</span>
          </label>
        </div>
        <div>
          <label>
            <input type="checkbox">
            <span>Option 2</span>
          </label>
        </div>
        <div>
          <label>
            <input type="checkbox">
            <span>Option 3</span>
          </label>
        </div>
      </div>
    </div>
    <div>
      <span>Radio Buttons</span>
      <div>
        <div>
          <label>
            <input type="radio" checked="" name="radio-direct" value="1">
            <span>Option 1</span>
          </label>
        </div>
        <div>
          <label>
            <input type="radio" name="radio-direct" value="2">
            <span>Option 2</span>
          </label>
        </div>
        <div>
          <label>
            <input type="radio" name="radio-direct" value="3">
            <span>Option 3</span>
          </label>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
  h3 {
    @apply mt-5 font-bold;
  }
</style>