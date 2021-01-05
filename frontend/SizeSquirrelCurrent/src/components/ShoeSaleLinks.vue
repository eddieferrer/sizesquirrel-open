<template>
  <div v-if="page === 'match' || saleLinks.length > 0" class="columns">
    <div class="column">
      <h5 class="has-text-weight-bold">Buy This Shoe</h5>
      <hr />
      <div class="columns is-multiline">
        <div v-if="saleLinks[0]" class="column">
          <!-- repeated code -->
          <template v-for="(datafeed, index) in saleLinks[0].datafeeds">
            <!--  if loop.first  -->
            <div v-if="index === 0" :key="index + '_1'" class="columns">
              <div class="column is-12">
                <h4 class="is-capitalized">{{ shoe.brand['name'] }} {{ shoe.model }}</h4>
                <span class="is-size-6 is-capitalized is-italic has-text-grey"
                  >{{ shoe.gender['name_pretty'] }} {{ shoe.type | capitalize }} Shoe</span
                >
                <h6 class="is-pulled-right">
                  <strong>Retail Price&nbsp;</strong>
                  ${{ datafeed.Product.Retail_Price }}
                </h6>
              </div>
            </div>
            <!--  endif  -->
          </template>

          <div class="columns is-multiline">
            <template v-for="(datafeed, index) in saleLinks[0].datafeeds">
              <div :key="index + '_2'" class="column is-6 is-no-top-padding">
                <AffiliatePriceBlock :datafeed="datafeed"></AffiliatePriceBlock>
              </div>
            </template>
          </div>
        </div>
        <template v-if="page === 'match'">
          <AvantLinkAd :number-of-sale-links="saleLinks.length" />
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import { capitalize } from '@/filters';
import AffiliatePriceBlock from '@/components/AffiliatePriceBlock';
import AvantLinkAd from '@/components/AvantLinkAd';

export default {
  name: 'ShoeSaleLinks',
  components: { AffiliatePriceBlock, AvantLinkAd },
  filters: {
    capitalize,
  },
  props: {
    page: {
      type: String,
      default: 'shoe',
    },
    saleLinks: {
      type: Array,
      default() {
        return [];
      },
    },
    shoe: {
      type: Object,
      default() {
        return {};
      },
    },
  },
};
</script>

<style scoped lang="scss">
.is-no-top-padding {
  padding-top: 0px;
}
</style>
