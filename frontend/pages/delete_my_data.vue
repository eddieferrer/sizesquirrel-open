<template>
  <div class="columns is-centered">
    <div class="column is-two-thirds-desktop">
      <h2 class="is-size-4 has-text-centered has-text-primary">
        Delete My Data
      </h2>
      <h5 class="is-size-5 has-text-centered">User Data Deletion</h5>
      <hr />
      <p>SizeSquirrel tries to be as respectful with user data as possible.</p>
      <p>
        <strong>How can I delete all my user data?</strong>
      </p>
      <p>
        We do not keep or hold any data outside of your user profile. We do not
        sell this data to any other entities.
      </p>
      <p>
        If you would like to absolutely and completely remove all your user data
        from SizeSquirrel, and any history of this data all you have to do is
        delete your account. Please follow these steps:
      </p>
      <ol>
        <li><NuxtLink to="/login">Log in to the site</NuxtLink></li>
        <li>
          <NuxtLink to="/my_profile">Visit your profile page</NuxtLink>
        </li>
        <li>
          Click on "
          <NuxtLink to="/my_user_details">Change User Details</NuxtLink>" in
          your User Details section
        </li>
        <li>Click on "<em>Delete Account</em>"</li>
      </ol>
      <p>
        After these steps we will have no data that relates to you in any way.
      </p>
      <p>
        If you are having trouble following this step please email us at:
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
</template>

<script>
export default {
  name: 'DeleteMyData',
  layout: 'noHomepageForm',
  head() {
    return {
      title: 'Delete My Data',
    };
  },
};
</script>

<style scoped lang="scss">
p {
  margin-bottom: 1em;
}
ol {
  margin: 0 0 1rem 2rem;
}
</style>
