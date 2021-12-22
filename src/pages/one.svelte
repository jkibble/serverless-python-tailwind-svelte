<script>
  import Countdown from '/src/lib/Countdown.svelte'
  import Table from '/src/lib/Table.svelte'
  import Text from '/src/lib/input/text.svelte'

  const url = 'https://baconipsum.com/api/?type=meat-and-filler&paras=10&start-with-lorem=1';
  let words = [];
  fetch(url).then((response) => response.json()).then((result) => { words = result; onClick() })
  let content = '';
  let bgColor = '';
  let textColor = '';

  const onClick = () => {
    content = words[Math.floor(Math.random()*words.length)];
    let colors = getColors();
    bgColor = colors[0];
    textColor = colors[1];
  }

  const getColors = () => {
    let bgColor = `#${Math.floor(Math.random()*16777215).toString(16)}`;
    let textColor = getComplementaryColor(bgColor);

    return [bgColor, textColor]
  }

  const getComplementaryColor = (color = '') => {
    const colorPart = color.slice(1);
    const ind = parseInt(colorPart, 16);
    let iter = ((1 << 4 * colorPart.length) - 1 - ind).toString(16);
    while (iter.length < colorPart.length) {
      iter = '0' + iter;
    };
    return '#' + iter;
  };

</script>
<p class="h-24 first-line:uppercase first-line:tracking-widest
first-letter:text-7xl first-letter:font-bold first-letter:text-grey-900
first-letter:mr-3 first-letter:float-left">{content}</p>

<div>
  <button id="btn" class="p-4 mt-4 mb-4 rounded-xl" style="background: {bgColor}; color: {textColor}" on:click={onClick}>Click Me!</button>
</div>

<Text label="Email"/>
<Text label="Password" inputType="password" />
<Text label="Favourite Movie" value="foo" autofocus="true" placeholder="here is the place holder" size="10" />

<Countdown />
<Table />