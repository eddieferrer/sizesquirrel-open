<template>
  <footer class="footer">
    <div class="container">
      <div class="columns">
        <div class="column is-narrow">
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
        </div>
        <div class="column">
          <p class="is-pulled-right">
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
