<template>
  <div>
    <loading
      :active="!isInitialized"
      :is-full-page="true"
      color="#0776bc"
      :z-index="3000"
    >
      <!-- possible loading icon
        <template slot="default">
        <img src="/images/SizeSquirrelLogoMainSquare.svg" alt class="icon" />
      </template> -->
    </loading>

    <FlashMessage></FlashMessage>
    <!-- <PWAUpdateButton></PWAUpdateButton> -->

    <section class="hero">
      <v-lazy-image
        class="hero-img"
        srcset="
          /images/hero_image_1920w.jpg 1920w,
          /images/hero_image_1366w.jpg 1366w,
          /images/hero_image_980w.jpg   980w,
          /images/hero_image_768w.jpg   768w,
          /images/hero_image_360w.jpg   360w
        "
        src-placeholder="/images/hero_image_lofi.jpg"
        src="/images/hero_image_980w.jpg"
        alt="SizeSquirrel"
      />
      <NavBar />
      <div class="hero-body">
        <div class="container">
          <div class="columns is-centered">
            <div class="column is-10">
              <div v-if="isAuthenticated" v-cloak class="intro-text">
                <span class="is-size-3-mobile is-size-2 script">Hi,&nbsp;</span>
                <span
                  v-if="user"
                  class="is-size-4-mobile is-size-3 block-text"
                  >{{ user.username }}</span
                >
              </div>
              <div v-if="!isAuthenticated" v-cloak class="intro-text">
                <span class="is-size-3-mobile is-size-2 script"
                  >Hello, I can help you find the right shoe size.
                </span>
              </div>
            </div>
          </div>
          <div class="columns is-centered">
            <div
              class="column is-full-mobile is-two-thirds-desktop is-three-quarters-tablet"
            ></div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <Nuxt />
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
        <h2 class="is-size-4 has-text-centered has-text-primary">
          Did you know?
        </h2>
        <h5 class="is-size-5 has-text-centered">Some helpful information</h5>
        <hr />
        <div class="columns">
          <div class="column is-4">
            <div>
              <p>
                Follow us on Facebook and Instagram for deal alerts and
                SizeSquirrel news!
                <a href="https://www.facebook.com/sizesquirrel/">Facebook</a
                >&nbsp;|&nbsp;
                <a href="https://www.instagram.com/sizesquirrel/">Instagram</a>
              </p>
            </div>
          </div>
          <div class="column is-4">
            <div>
              <p v-if="isAuthenticated">
                The more shoes you have on your profile the better our chances
                are of finding a size for the shoes you don't have.
              </p>
              <p v-if="!isAuthenticated">
                If you register for an account and fill out your profile we can
                help you find your size better!
              </p>
            </div>
          </div>
          <div class="column is-4">
            <div>
              <p>
                Can't find a shoe you want to add? We're sorry. Email us and
                we'll add it to the site:
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

    <Footer />
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import Loading from 'vue-loading-overlay';

import FlashMessage from '@/components/FlashMessage';
// import PWAUpdateButton from '@/components/PWAUpdateButton';
import NavBar from '@/components/NavBar';
import ShoeBuddies from '@/components/ShoeBuddies';
import Footer from '@/components/Footer';

export default {
  components: {
    FlashMessage,
    Footer,
    Loading,
    NavBar,
    // PWAUpdateButton,
    ShoeBuddies,
  },
  data() {
    return {};
  },
  computed: {
    ...mapGetters(['profile', 'user', 'isAuthenticated', 'isInitialized']),
  },
};
</script>

<style scoped lang="scss">
//homepage
.hero {
  position: relative;

  .hero-body {
    box-shadow: inset 0 0 0 2000px rgba(0, 0, 0, 0.4);
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
</style>
