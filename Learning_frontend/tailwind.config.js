/** @type {import('tailwindcss').Config} */
export default {
  content: [],
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: 'media',
  theme: {
    extend: {
      colors: {
        'primary': '#4f0fbd',
        'secondary': '#000000',
        'tertiary': '#3db028',
      }
    },
  },
  plugins: [],
}

