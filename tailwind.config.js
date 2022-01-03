const { colors } = require("tailwindcss/defaultTheme");

module.exports = {
  content: ["./src/**/*.svelte", "./pages/**/*.html"],
  mode: "jit",
  darkMode: "class", // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        gray: {},

        grey: colors["gray"],
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
