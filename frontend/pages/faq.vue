<template>
  <div class="columns is-centered">
    <div class="column is-two-thirds-desktop">
      <h2 class="is-size-4 has-text-centered has-text-primary">FAQ's</h2>
      <h5 class="is-size-5 has-text-centered">Frequently Asked Questions</h5>
      <hr />
      <p>
        <strong>I can't find my shoe on the site!</strong>
      </p>
      <p>
        Please send us an email at,
        <a
          data-name="eddie"
          data-domain="sizesquirrel"
          data-tld="com"
          aria-label="email"
          href="#"
          class="cryptedmail"
          onclick="window.location.href = 'mailto:' + this.dataset.name + '@' + this.dataset.domain + '.' + this.dataset.tld"
        ></a>
        and we will add the shoe to the site.
      </p>

      <p>
        <strong>Why is there no picture for a certain shoe?</strong>
      </p>
      <p>
        There are a lot of shoes on SizeSquirrel, and manually acquiring each
        picture would be an enormous task. For now, we are gathering the images
        from our affiliate network. So if your shoe is not currently for sale
        with our affiliate partners, then it probably will not have a picture
        associated with it.
      </p>
      <p>
        <strong>What about older models of the shoes?</strong>
      </p>
      <p>
        We understand that previous shoe models may be different. Because our
        images are gathered from the current models on sale, we don't have a
        reliable source to gather the images for old or discontinued models. We
        understand this is a problem, but haven't yet come up with a good
        solution to this.
      </p>
      <p>
        <strong>How can I support the site?</strong>
      </p>
      <p>
        SizeSquirrel is completely free, and would like to stay that way. It
        does cost us money and time to keep the site running. If you would like
        to support the site, please just tell a friend about it, or use the
        <NuxtLink to="/sales">Climbing Shoes On Sale!</NuxtLink> page next time
        you are in the market for new climbing shoes.
      </p>
      <br />
      <p>
        Is your question not here? Have comments? Send us an email:
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
  name: 'Faq',
  layout: 'no-homepage-form',
  middleware: ['auth'],
  head() {
    return {
      title: 'Frequently Asked Questions',
    };
  },
};
</script>

<style>
p {
  margin-bottom: 1em;
}
</style>
