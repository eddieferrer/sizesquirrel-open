<template>
  <footer class="footer">
    <div class="container">
      <div class="columns is-justify-content-space-between">
        <div class="column is-narrow has-text-centered-mobile">
          <nav class="breadcrumb has-dot-separator" aria-label="breadcrumbs">
            <ul>
              <li>
                <NuxtLink to="/faq">FAQ</NuxtLink>
              </li>
              <li>
                <NuxtLink to="/terms">Terms</NuxtLink>
              </li>
              <li>
                <NuxtLink to="/privacy">Privacy</NuxtLink>
              </li>
              <li>
                <a href="https://www.facebook.com/sizesquirrel/">Facebook</a>
              </li>
              <li>
                <a href="https://www.instagram.com/sizesquirrel/">Instagram</a>
              </li>
              <li>
                <a href="https://github.com/eddieferrer/sizesquirrel-open"
                  >GitHub</a
                >
              </li>
            </ul>
          </nav>
          <a href="https://www.buymeacoffee.com/sizesquirrel"
            ><img
              src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=sizesquirrel&button_colour=5F7FFF&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00"
          /></a>
        </div>
        <div class="column is-narrow has-text-centered-mobile">
          <p>
            We love your shoes
            <br />
            © {{ currentYear }} SizeSquirrel
          </p>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  components: {},
  data() {
    return {};
  },
  computed: {
    currentYear() {
      return new Date().getFullYear();
    },
  },
};
</script>

<style scoped lang="scss">
footer {
  background: url('/images/hero_image_footer.jpg');
  box-shadow: inset 0 0 0 2000px rgba(0, 0, 0, 0.4);
  background-position: center center;
  background-size: cover;
  color: $white;

  a {
    color: $white;

    &:hover {
      color: $purple;
    }
  }

  li {
    line-height: 32px;
  }
}
</style>
