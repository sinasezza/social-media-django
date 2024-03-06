/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../templates/**/*.html",
    "../static/**/*.{js}",
    "./node_modules/tw-elements/js/**/*.js",
  ],
  theme: {
    extend: {},
  },
  darkMode: "class",
  plugins: [require("tw-elements/plugin.cjs")],
};