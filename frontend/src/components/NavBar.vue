<template>
  <nav class="navbar is-dark" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <RouterLink class="navbar-item brandlogo nohover" to="/">
        <img
          src="/static/images/SizeSquirrelLogoMainSquare.svg"
          height="88"
          width="80"
          alt="SizeSquirrel"
        />
      </RouterLink>
      <span class="navbar-item navbar-item-brand">SizeSquirrel</span>
      <a
        role="button"
        class="navbar-burger burger"
        :class="{ 'is-active': isActive }"
        aria-label="menu"
        aria-expanded="false"
        data-target="navbarBasic"
        @click="isActive = !isActive"
      >
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
      </a>
    </div>

    <div id="navbarBasic" class="navbar-menu" :class="{ 'is-active': isActive }">
      <div class="navbar-start">
        <span class="navbar-item navbar-item-brand is-hidden-desktop pt-2">&nbsp;</span>
        <RouterLink class="navbar-item" to="/" @click.native="isActive = !isActive"
          >Home</RouterLink
        >
        <RouterLink
          v-if="isAuthenticated"
          to="/browse"
          class="navbar-item"
          @click.native="isActive = !isActive"
          >Browse Shoes</RouterLink
        >
        <RouterLink
          v-if="isAuthenticated"
          to="/my_profile"
          class="navbar-item"
          @click.native="isActive = !isActive"
          >My Profile</RouterLink
        >
        <RouterLink to="/sales" class="navbar-item" @click.native="isActive = !isActive"
          >Shoes On Sale</RouterLink
        >
        <RouterLink to="/recommend" class="navbar-item" @click.native="isActive = !isActive"
          >Recommend A Shoe</RouterLink
        >
      </div>
      <div class="navbar-end">
        <a v-if="isAuthenticated" href="#" class="navbar-item" @click.prevent.stop="logout()"
          >Log Out</a
        >
        <div class="navbar-item">
          <div class="buttons">
            <RouterLink
              v-if="!isAuthenticated"
              to="/register"
              class="button is-info"
              @click.native="isActive = !isActive"
            >
              <strong>Sign up</strong>
            </RouterLink>
            <RouterLink
              v-if="!isAuthenticated"
              to="/login"
              class="button is-light"
              @click.native="isActive = !isActive"
              >Log in</RouterLink
            >
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'NavBar',
  data() {
    return {
      isActive: false,
    };
  },
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
  methods: {
    logout() {
      this.$store.dispatch('AUTH_LOGOUT').then(() => {
        window.location = '/';
      });
    },
  },
};
</script>

<style scoped lang="scss">
$ss-transparent-gray: rgba(0, 0, 0, 0.6);
$squirrelDarkGray: #131313;

.navbar.is-dark {
  background-color: $ss-transparent-gray !important;
}
.navbar.is-dark .navbar-start > a.navbar-item:hover,
.navbar.is-dark .navbar-start > a.navbar-item.is-active,
.navbar.is-dark .navbar-start .navbar-link:hover,
.navbar.is-dark .navbar-start .navbar-link.is-active,
.navbar.is-dark .navbar-end > a.navbar-item:hover,
.navbar.is-dark .navbar-end > a.navbar-item.is-active,
.navbar.is-dark .navbar-end .navbar-link:hover,
.navbar.is-dark .navbar-end .navbar-link.is-active {
  background-color: $ss-transparent-gray;
}
.navbar-item-brand {
  font-family: Lato, 'Helvetica Neue', Helvetica, Roboto, Arial, sans-serif;
  font-weight: 900;
  font-variant: small-caps;
  letter-spacing: 0.05em;
  font-size: 1.3rem;
}
.navbar-item.brandlogo {
  overflow: visible;
  padding-right: 0;
  padding-bottom: 0;
  padding-top: 0;
  height: 3.5rem;
  img {
    max-height: none;
    margin-top: 28px;
    background-color: $squirrelDarkGray;
    padding: 1em;
    width: 80px;
    height: 88px;
  }
}
.nohover:hover {
  background-color: transparent !important;
}
a.navbar-item:hover {
  color: $white;
}
.pt-2 {
  padding-top: 2rem;
}
</style>
