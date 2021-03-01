<template>
  <div>
    <div id="fb-root"></div>
    <div id="fb-script"></div>

    <div class="container">
      <h2
        v-if="isAuthenticated"
        class="is-size-4 has-text-centered has-text-primary"
      >
        Welcome Back
      </h2>
      <h2
        v-if="!isAuthenticated"
        class="is-size-4 has-text-centered has-text-primary"
      >
        How It Works
      </h2>
      <h5 v-if="!isAuthenticated" class="is-size-5 has-text-centered">
        It's super easy
      </h5>
      <hr />
    </div>

    <HomeCards></HomeCards>

    <PopularShoes></PopularShoes>

    <section class="section">
      <div class="columns">
        <div class="column">
          <h2 class="is-size-4 has-text-centered has-text-primary">News</h2>
          <h5 class="is-size-5 has-text-centered">Updates from Facebook</h5>
          <hr />
          <div class="has-text-centered">
            <div
              class="fb-page"
              data-href="https://www.facebook.com/sizesquirrel/"
              data-tabs="timeline"
              data-width="500"
              data-height="400"
              data-small-header="false"
              data-adapt-container-width="true"
              data-hide-cover="true"
              data-show-facepile="true"
            >
              <blockquote
                cite="https://www.facebook.com/sizesquirrel/"
                class="fb-xfbml-parse-ignore"
              >
                <a href="https://www.facebook.com/sizesquirrel/"
                  >SizeSquirrel</a
                >
              </blockquote>
            </div>
          </div>
        </div>

        <div class="column">
          <h2 class="is-size-4 has-text-centered has-text-primary">
            Contact Us
          </h2>
          <h5 class="is-size-5 has-text-centered">
            We'd love to hear from you
          </h5>
          <hr />
          <p>
            Have a comment or suggestion? Want us to add a shoe to the site?
            Found a bug? The easiest way to reach us is to send us a message on
            <a href="https://www.facebook.com/sizesquirrel/">Facebook</a>!
          </p>
          <br />
          <p>
            Don't want to use
            <a href="https://www.facebook.com/sizesquirrel/">Facebook</a>? You
            can send us an old fashioned email:
            <a
              data-name="eddie"
              data-domain="sizesquirrel"
              data-tld="com"
              href="#"
              class="cryptedmail"
              aria-label="email"
              onclick="window.location.href = 'mailto:' + this.dataset.name + '@' + this.dataset.domain + '.' + this.dataset.tld"
            ></a>
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
/* eslint-disable no-useless-escape */
import { mapGetters } from 'vuex';

import PopularShoes from '@/components/PopularShoes';
import HomeCards from '@/components/HomeCards';

export default {
  name: 'Index',
  layout: 'homepageForm',
  components: {
    PopularShoes,
    HomeCards,
  },
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
  mounted() {
    const postscribe = require('postscribe');
    postscribe(
      '#fb-script',
      `<script async defer crossorigin="anonymous" src="https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v8.0&appId=943851385727348&autoLogAppEvents=1" nonce="eIcxmal8"><\/script>`
    );
  },
  head() {
    return {
      title: 'Climbing shoe sizing, recommendations, and deals',
      links: [
        {
          rel: 'canonical',
          href: `https://sizesquirrel.com${this.$nuxt.$route.path}`,
        },
      ],
    };
  },
};
</script>
