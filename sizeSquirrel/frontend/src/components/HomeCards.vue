<template>
  <div>
    <div v-if="isAuthenticated" class="columns">
      <div class="column is-one-third-tablet">
        <div class="card has-equal-height">
          <div class="card-content content">
            <div class="box-icon">
              <span class="fi-magnifying-glass"></span>
            </div>
            <div class="info_homepage has-text-centered">
              <h4 class="step"></h4>
              <h4>Browse Shoes</h4>
              <p>
                See all the shoes SizeSquirrel found a size for,
                <em>just for you</em>
              </p>
              <p class="has-text-centered">
                <RouterLink to="/browse" class="button is-info is-normal is-marginless"
                  >Browse Shoes</RouterLink
                >
              </p>
            </div>
          </div>
        </div>
      </div>
      <div class="column is-one-third-tablet">
        <div class="card has-equal-height">
          <div class="card-content">
            <div class="box-icon">
              <span class="fi-pricetag-multiple"></span>
            </div>
            <div class="info_homepage has-text-centered">
              <h4 class="step"></h4>
              <h4>Climbing Shoes On Sale</h4>
              <p>See climbing shoes on sale, from all major online retailers.</p>
              <p class="has-text-centered">
                <RouterLink to="/sales" class="button is-info is-normal is-marginless"
                  >Shoes On Sale</RouterLink
                >
              </p>
            </div>
          </div>
        </div>
      </div>
      <div class="column is-one-third-tablet">
        <div class="card has-equal-height">
          <div class="card-content content">
            <div class="box-icon">
              <span class="fi-results-demographics"></span>
            </div>
            <div class="info_homepage has-text-centered">
              <h4 class="step"></h4>
              <h4>Visit Your Profile</h4>
              <p>Add shoes, delete shoes, see your shoe buddies or change user details.</p>
              <p class="has-text-centered">
                <RouterLink to="/my_profile" class="button is-info is-normal is-marginless"
                  >My Profile</RouterLink
                >
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="!isAuthenticated" class="columns">
      <div class="column is-one-third-tablet">
        <div class="card has-equal-height">
          <div class="card-content content">
            <div class="box-icon">
              <span class="fi-results-demographics"></span>
            </div>
            <div class="info_homepage has-text-centered">
              <h4 class="step">Step 1</h4>
              <h4>Register for an account. Its completely free.</h4>
              <p>
                We wont spam you. We wont sell your information. All you need is an email address,
                or log in with your Facebook account.
              </p>
            </div>
          </div>
        </div>
      </div>
      <div class="column is-one-third-tablet">
        <div class="card has-equal-height">
          <div class="card-content">
            <div class="box-icon">
              <span class="fi-plus"></span>
            </div>
            <div class="info_homepage has-text-centered">
              <h4 class="step">Step 2</h4>
              <h4>Add shoes that you already own to your profile.</h4>
              <p>
                SizeSquirrel will use this information to find the sizes for the shoes you
                <em>don't</em> own. The more shoes you add to your profile, the more accurate your
                results will be.
              </p>
            </div>
          </div>
        </div>
      </div>
      <div class="column is-one-third-tablet">
        <div class="card has-equal-height">
          <div class="card-content content">
            <div class="box-icon">
              <span class="fi-magnifying-glass"></span>
            </div>
            <div class="info_homepage has-text-centered">
              <h4 class="step">Step 3</h4>
              <h4>SizeSquirrel finds the perfect size for the shoes you don't own.</h4>
              <p>
                Using
                <em>math</em> we give you a best guess of what size you'll be for the shoes you
                don't own.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="!isAuthenticated" class="columns is-centered">
      <div class="column is-one-quarter">
        <p class="has-text-centered">
          <RouterLink to="/register" class="button is-info is-medium is-fullwidth"
            >Sign Up</RouterLink
          >
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'HomeCards',
  components: {},
  computed: {
    ...mapGetters(['isAuthenticated']),
  },
};
</script>

<style scoped lang="scss">
.columns {
  .column {
    margin-top: 2.5em;
  }
}
.has-equal-height {
  display: flex;
  flex-direction: column;
  height: 100%;
}
.has-equal-height .card-footer {
  margin-top: auto;
}

.box-icon {
  background-color: $aqua;
  border-radius: 50%;
  display: table;
  height: 100px;
  margin: 0 auto;
  width: 100px;
  margin-top: -61px;
  font-size: 3rem;
  span {
    color: $white;
    display: table-cell;
    text-align: center;
    vertical-align: middle;
  }
}

.info_homepage {
  h4 {
    margin-top: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    &.step {
      font-family: 'Shadows Into Light', cursive;
      text-transform: uppercase;
    }
  }
  p {
    color: $medgray;
    padding-top: 10px;
  }
}
</style>
