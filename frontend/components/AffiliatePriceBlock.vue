<template>
  <div class="price_buy_button">
    <span class="info_label muted">{{ datafeed.Retailer_Name }}</span>
    <a
      :href="datafeed.Product.Buy_Link"
      target="_blank"
      class="is-clearfix"
      :onclick="
        'return gtag_report_conversion(\'' + datafeed.Product.Buy_Link + '\');'
      "
    >
      <span class="sales_red sales_retailer_price"
        >${{ datafeed.Product.Sale_Price }}</span
      >
      <span
        class="sales_retailer_logo"
        :style="{ 'background-image': 'url(' + datafeed.Retailer_Logo + ')' }"
      ></span>
      <span class="sales_percent_off">{{ datafeed.Percent_Off }}% Off</span>
      <span class="sales_buy_now">Buy Now</span>
    </a>
  </div>
</template>

<script>
export default {
  name: 'AffiliatePriceBlock',
  props: {
    datafeed: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {};
  },
};
</script>

<style scoped lang="scss">
.price_buy_button {
  a {
    overflow: hidden;
    position: relative;
    display: table;
    border: 1px solid gray;
    width: 100%;
    height: 37px;
    table-layout: fixed;
    background-color: white;
    &:hover {
      .sales_buy_now {
        width: 110px;
      }
    }

    /* No greater than 900px, no less than 400px */
    @media (max-width: 1405px) and (min-width: 768px) {
      &:hover {
        .sales_buy_now {
          width: 90px;
        }
      }
    }
  }

  * {
    display: table-cell;
    vertical-align: middle;
    line-height: 35px;
  }

  .sales_buy_now {
    color: $white;
    background-color: $purple;
    width: 85px;
    text-align: right;
    padding-right: 10px;
    -webkit-transition: width 1s; /* For Safari 3.1 to 6.0 */
    transition: width 1s;
    font-weight: bold;
    border-left: 3px solid $amazon_red;
  }

  .sales_retailer_logo {
    width: 100%;
    background-size: cover;
    background-position-y: center;
  }

  .sales_retailer_price {
    font-family: Lato, 'Helvetica Neue', Helvetica, Roboto, Arial, sans-serif;
    font-weight: bold;
    width: 76px;
    text-align: left;
    padding-left: 4px;
    font-size: 19px;
  }
  .sales_percent_off {
    &:before {
      position: absolute;
      content: '';
      width: 0;
      height: 0;
      bottom: 0;
      border-top: 36px solid transparent;
      border-right: 20px solid $amazon_red;
      margin-left: -20px;
    }

    font-family: Lato, 'Helvetica Neue', Helvetica, Roboto, Arial, sans-serif;
    width: 58px;
    text-align: left;
    color: $white;
    font-weight: bold;
    background-color: $amazon_red;
    @media (max-width: 1280px) and (min-width: 768px) {
      display: none;
    }
  }
  .sales_red {
    color: $amazon_red !important;
  }
}
</style>
