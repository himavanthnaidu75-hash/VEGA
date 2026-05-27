/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "var(--color-primary, #F7F7F5)",
        secondary: "var(--color-secondary, #F5C518)",
        ink: "#0A0F2C",
        success: "#00B37E",
        danger: "#E83535",
        kill: "#CC2200",
      }
    },
  },
  plugins: [],
}
