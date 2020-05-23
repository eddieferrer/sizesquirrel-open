<template>
  <div class="column" :class="{ 'is-narrow': numberOfSaleLinks > 0 }">
    <div
      v-if="numberOfSaleLinks > 0"
      id="avantlink_ad_square"
      style="width: 300px; height: 250px;"
      class="ad"
    ></div>
    <div v-if="numberOfSaleLinks === 0" id="avantlink_ad_wide" class="ad"></div>
  </div>
</template>

<script>
/* eslint-disable no-useless-escape */
import postscribe from 'postscribe';

export default {
  name: 'AvantLinkAd',
  props: {
    numberOfSaleLinks: {
      type: Number,
      default: 0,
    },
  },
  mounted() {
    if (this.numberOfSaleLinks > 0) {
      postscribe(
        '#avantlink_ad_square',
        `<script type="text/javascript" src="//www.avantlink.com/api.php?module=AdSearch&affiliate_id=157739&website_id=197019&output=js&search_results_count=1&search_results_sort_order=Random&ad_type=image&include_ad_group_ids=15457&image_height=250&image_width=300"><\/script>`
      );
    } else {
      // dynamic ads
      postscribe(
        '#avantlink_ad_wide',
        `<script type="text/javascript" src="//www.avantlink.com/api.php?module=AdSearch&affiliate_id=157739&website_id=197019&output=js&search_results_count=1&search_results_sort_order=Random&ad_type=image&include_ad_group_ids=15441&image_height=90&image_width=728&search_results_options=_blank"><\/script>`
      );
    }
  },
};
</script>

<style scoped lang="scss">
.ad {
  margin: 0 auto;
  text-align: center;
}
</style>
