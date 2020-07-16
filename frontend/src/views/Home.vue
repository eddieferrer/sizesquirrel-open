<template>
  <div>
    <div id="fb-root"></div>

    <div class="container">
      <h2 v-if="isAuthenticated" class="is-size-4 has-text-centered has-text-primary">
        Welcome Back
      </h2>
      <h2 v-if="!isAuthenticated" class="is-size-4 has-text-centered has-text-primary">
        How It Works
      </h2>
      <h5 v-if="!isAuthenticated" class="is-size-5 has-text-centered">It's super easy</h5>
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
          <div class="fb_wrapper">
            <div
              class="fb-page"
              data-href="https://www.facebook.com/sizesquirrel/"
              data-tabs="timeline"
              data-height="300"
              data-small-header="true"
              data-adapt-container-width="true"
              data-hide-cover="false"
              data-show-facepile="false"
            >
              <blockquote
                cite="https://www.facebook.com/sizesquirrel/"
                class="fb-xfbml-parse-ignore"
              >
                <a href="https://www.facebook.com/sizesquirrel/">SizeSquirrel</a>
              </blockquote>
            </div>
          </div>
        </div>
        <div class="column">
          <h2 class="is-size-4 has-text-centered has-text-primary">Contact Us</h2>
          <h5 class="is-size-5 has-text-centered">We'd love to hear from you</h5>
          <hr />
          <p>
            Have a comment or suggestion? Want us to add a shoe to the site? Found a bug? The
            easiest way to reach us is to send us a message on
            <a href="https://www.facebook.com/sizesquirrel/">Facebook</a>!
          </p>
          <br />
          <p>
            Don't want to use
            <a href="https://www.facebook.com/sizesquirrel/">Facebook</a>? You can send us an old
            fashioned email:
            <a
              data-name="eddie"
              data-domain="sizesquirrel"
              data-tld="com"
              href="#"
              class="cryptedmail"
              onclick="window.location.href = 'mailto:' + this.dataset.name + '@' + this.dataset.domain + '.' + this.dataset.tld"
              >email</a
            >
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

import PopularShoes from '@/components/PopularShoes';
import HomeCards from '@/components/HomeCards';

export default {
  name: 'Home',
  components: {
    PopularShoes,
    HomeCards,
  },
  metaInfo: {
    // title will be injected into parent titleTemplate
    title: 'Climbing shoe sizing, recommendations, and deals',
  },
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
  mounted() {
    // eslint-disable-next-line func-names
    (function (d, s, id) {
      const fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) return;
      const js = d.createElement(s);
      js.id = id;
      js.src =
        'https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0&appId=943851385727348&autoLogAppEvents=1';
      fjs.parentNode.insertBefore(js, fjs);
    })(document, 'script', 'facebook-jssdk');
  },
};
</script>

<style scoped lang="scss"></style>
