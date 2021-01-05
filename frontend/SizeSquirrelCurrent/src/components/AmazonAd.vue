<template>
  <div class="column is-12">
    <div id="amazon_ad" class="ad"></div>
  </div>
</template>

<script>
// This component is not currently in use
/* eslint-disable no-useless-escape */
import postscribe from 'postscribe';

export default {
  name: 'AmazonAd',
  props: {
    searchTerm: {
      type: String,
      default: 'climbing shoes',
    },
  },
  mounted() {
    postscribe(
      '#amazon_ad',
      `<script type="text/javascript">
        amzn_assoc_placement = "adunit0";
        amzn_assoc_tracking_id = "sizesq-20";
        amzn_assoc_ad_mode = "search";
        amzn_assoc_ad_type = "smart";
        amzn_assoc_marketplace = "amazon";
        amzn_assoc_region = "US";
        amzn_assoc_default_search_phrase = "${this.searchTerm}";
        amzn_assoc_default_category = "All";
        amzn_assoc_linkid = "3e8280212bd08f5c1cf79301e00fede4";
        amzn_assoc_design = "in_content";
        <\/script>
        <script src="//z-na.amazon-adsystem.com/widgets/onejs?MarketPlace=US"><\/script>`
    );
  },
};
</script>

<style scoped lang="scss">
.ad {
  margin: 0 auto;
  text-align: center;
}
</style>
