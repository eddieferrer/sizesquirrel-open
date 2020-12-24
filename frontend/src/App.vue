<template>
  <div>
    <loading :active="!isInitialized" :is-full-page="true" color="#0776bc" :z-index="3000">
      <!-- possible loading icon 
        <template slot="default">
        <img src="/static/images/SizeSquirrelLogoMainSquare.svg" alt class="icon" />
      </template> -->
    </loading>

    <FlashMessage></FlashMessage>
    <PWAUpdateButton></PWAUpdateButton>

    <section class="hero">
      <v-lazy-image
        class="hero-img"
        srcset="
          /static/images/hero_image_1920w.jpg 1920w,
          /static/images/hero_image_1366w.jpg 1366w,
          /static/images/hero_image_980w.jpg   980w,
          /static/images/hero_image_768w.jpg   768w,
          /static/images/hero_image_360w.jpg   360w
        "
        src-placeholder="/static/images/hero_image_lofi.jpg"
        src="/static/images/hero_image_980w.jpg"
        alt="SizeSquirrel"
      />
      <NavBar />
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-10">
              <div v-if="isAuthenticated" v-cloak class="intro-text">
                <span class="is-size-3-mobile is-size-2 script">Hi,&nbsp;</span>
                <span v-if="user" class="is-size-4-mobile is-size-3 block-text">{{
                  user.username
                }}</span>
              </div>
              <div v-if="!isAuthenticated" v-cloak class="intro-text">
                <span class="is-size-3-mobile is-size-2 script"
                  >Hello, I can help you find the right shoe size.
                </span>
              </div>
            </div>
          </div>
          <div class="columns is-centered">
            <div class="column is-full-mobile is-two-thirds-desktop is-three-quarters-tablet">
              <ItemMatchForm v-if="showHomePageForm"></ItemMatchForm>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <RouterView :key="$route.fullPath"></RouterView>
      </div>
    </section>

    <section v-if="isAuthenticated" class="section">
      <div class="container">
        <ShoeBuddies
          v-if="isAuthenticated && user && user.id"
          :target-user-id="user.id"
        ></ShoeBuddies>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h2 class="is-size-4 has-text-centered has-text-primary">Did you know?</h2>
        <h5 class="is-size-5 has-text-centered">Some helpful information</h5>
        <hr />
        <div class="columns">
          <div class="column is-4">
            <div>
              <p>
                Follow us on Facebook and Instagram for deal alerts and SizeSquirrel news!
                <a href="https://www.facebook.com/sizesquirrel/">Facebook</a>&nbsp;|&nbsp;
                <a href="https://www.instagram.com/sizesquirrel/">Instagram</a>
              </p>
            </div>
          </div>
          <div class="column is-4">
            <div>
              <p v-if="isAuthenticated">
                The more shoes you have on your profile the better our chances are of finding a size
                for the shoes you don't have.
              </p>
              <p v-if="!isAuthenticated">
                If you register for an account and fill out your profile we can help you find your
                size better!
              </p>
            </div>
          </div>
          <div class="column is-4">
            <div>
              <p>
                Can't find a shoe you want to add? We're sorry. Email us and we'll add it to the
                site:
                <a
                  data-name="eddie"
                  data-domain="sizesquirrel"
                  data-tld="com"
                  href="#"
                  aria-label="email"
                  class="cryptedmail"
                  onclick="window.location.href = 'mailto:' + this.dataset.name + '@' + this.dataset.domain + '.' + this.dataset.tld"
                ></a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <footer class="footer">
      <div class="container">
        <div class="columns">
          <div class="column is-narrow">
            <nav class="breadcrumb has-dot-separator" aria-label="breadcrumbs">
              <ul>
                <li>
                  <RouterLink to="/faq">FAQ</RouterLink>
                </li>
                <li>
                  <RouterLink to="/terms">Terms</RouterLink>
                </li>
                <li>
                  <RouterLink to="/privacy">Privacy</RouterLink>
                </li>
                <li>
                  <a href="https://www.facebook.com/sizesquirrel/">Facebook</a>
                </li>
                <li>
                  <a href="https://www.instagram.com/sizesquirrel/">Instagram</a>
                </li>
                <li>
                  <a href="https://github.com/eddieferrer/sizesquirrel-open">GitHub</a>
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
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import Loading from 'vue-loading-overlay';

import FlashMessage from '@/components/FlashMessage';
import PWAUpdateButton from '@/components/PWAUpdateButton';
import NavBar from '@/components/NavBar';
import ItemMatchForm from '@/components/ItemMatchForm';
import ShoeBuddies from '@/components/ShoeBuddies';

import router from '@/router';

export default {
  name: 'App',
  components: {
    FlashMessage,
    ItemMatchForm,
    Loading,
    NavBar,
    PWAUpdateButton,
    ShoeBuddies,
  },
  metaInfo() {
    return {
      // Children can override the title.
      title: 'Climbing shoe sizing, recommendations, and deals',
      // Result: My Page Title | My Site
      // If a child changes the title to "My Other Page Title",
      // it will become: My Other Page Title ← My Site
      titleTemplate: '%s | SizeSquirrel',
      // Define meta tags here.
      meta: [
        // OpenGraph data (Most widely used)
        {
          vmid: 'og:title',
          property: 'og:title',
          content: 'Climbing shoe sizing, recommendations, and deals | SizeSquirrel',
        },
        { property: 'og:site_name', content: 'SizeSquirrel' },
        // The list of types is available here: http://ogp.me/#types
        { property: 'og:type', content: 'website' },
        // Should the the same as your canonical link, see below.
        { property: 'og:url', content: `https://www.sizesquirrel.com${this.$route.path}` },
        {
          vmid: 'og:image',
          property: 'og:image',
          content: 'https://www.sizesquirrel.com/static/images/OGImage1200x1200.jpg',
        },
        { vmid: 'og:image:width', property: 'og:image:width', content: '1200' },
        { vmid: 'og:image:height', property: 'og:image:height', content: '1200' },
        // Often the same as your meta description, but not always.
        {
          property: 'og:description',
          content:
            'Your climbing shoe resource. Climbing shoe sales, find your size for any climbing shoe, recommendations based on foot shape, and more.',
        },
        // FB
        { property: 'fb:app_id', content: '943851385727348' },
        // General
        {
          name: 'description',
          content:
            'Your climbing shoe resource. Climbing shoe sales, find your size for any climbing shoe, recommendations based on foot shape, and more.',
        },
        { name: 'author', content: 'SizeSquirrel' },
        { name: 'copyright', content: 'SizeSquirrel, Copyright (c) 2020' },
        // Twitter card
        { name: 'twitter:card', content: 'summary' },
        { name: 'twitter:site', content: 'https://www.sizesquirrel.com' },
        { name: 'twitter:title', content: 'SizeSquirrel' },
        {
          name: 'twitter:description',
          content:
            'Your climbing shoe resource. Climbing shoe sales, find your size for any climbing shoe, recommendations based on foot shape, and more.',
        },
        // Your twitter handle, if you have one.
        // { name: 'twitter:creator', content: '@sizesquirrel' },
        {
          name: 'twitter:image:src',
          content: 'https://www.sizesquirrel.com/static/images/OGImage1200x1200.jpg',
        },

        // Google / Schema.org markup:
        { itemprop: 'name', content: 'SizeSquirrel' },
        {
          itemprop: 'description',
          content:
            'Your climbing shoe resource. Climbing shoe sales, find your size for any climbing shoe, recommendations based on foot shape, and more.',
        },
        {
          itemprop: 'image',
          content: 'https://www.sizesquirrel.com/static/images/OGImage1200x1200.jpg',
        },
      ],
      links: [{ rel: 'canonical', href: `https://www.sizesquirrel.com${this.$route.path}` }],
    };
  },
  data() {
    return {
      showHomePageForm: true,
    };
  },
  computed: {
    ...mapGetters(['profile', 'user', 'isAuthenticated', 'isInitialized']),
    currentYear() {
      return new Date().getFullYear();
    },
  },
  watch: {
    $route() {
      this.showHomePageForm = !router.currentRoute.meta.hideItemMatchForm;
    },
  },
};
</script>

<style scoped lang="scss">
$white: rgba(255, 255, 255, 1);
$purple: #3e3895;

//homepage
.hero {
  position: relative;

  .hero-body {
    box-shadow: inset 0px 0px 0 2000px rgba(0, 0, 0, 0.4);
    position: relative;
  }

  .hero-img {
    position: absolute;
    object-fit: cover;
    width: 100%;
    height: 100%;
  }

  h4,
  span {
    color: $white;
  }
}

//lazy hero image
.v-lazy-image {
  filter: blur(10px);
  transition: filter 0.7s;
}

.v-lazy-image-loaded {
  filter: blur(0);
}

.intro-text {
  text-align: center;
}

.intro-text .script {
  font-family: 'Shadows Into Light', Georgia, Times, 'Times New Roman', serif;
}

.intro-text .block-text {
  font-weight: 900;
  text-transform: capitalize;
  font-family: 'Lato', sans-serif;
}

footer {
  background: url('/static/images/hero_image_footer.jpg');
  box-shadow: inset 0px 0px 0 2000px rgba(0, 0, 0, 0.4);
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

<style lang="scss">
@import '~vue-loading-overlay/dist/vue-loading.css';
@import '@/scss/custom_bulma.scss';
// Global SizeSquirrel Styles
body {
  background-color: $white-bis;
}

[v-cloak] {
  display: none;
}
hr,
hr.thin-hr {
  margin: 0.6rem 0 0.9rem 0;
}

//used for encrypting email address
.cryptedmail:after {
  content: attr(data-name) '@' attr(data-domain) '.' attr(data-tld);
}
.close-button {
  cursor: pointer;
}
.message {
  color: $white;
  a:link,
  a:visited,
  a:hover,
  a:active {
    color: $white;
    text-decoration: underline;
  }
  a:hover {
    color: #333;
    opacity: 0.5;
  }
}
progress {
  margin-top: 0.25em;
  margin-bottom: 0.25em;
}

// Icons
.icon-wrapper {
  font-size: 32px;
  float: left;
  color: $aqua;
  fill: $aqua;
  opacity: 0.25;
  width: 25px;
  .footshape {
    height: 34px;
    width: auto;
    margin-top: 7px !important;
    float: right !important;
  }
}
.icon-wrapper-search {
  color: $white;
  fill: $white;
  font-size: 25px;
}
.icon-wrapper-accordion {
  color: $bulmagray;
  fill: $bulmagray;
}
</style>
