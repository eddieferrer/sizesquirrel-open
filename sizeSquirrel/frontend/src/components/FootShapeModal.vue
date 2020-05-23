<template>
  <Modal :modal-size="modalSize" :show="show" @close="close">
    <header class="modal-card-head">
      <p class="modal-card-title">Foot Shapes</p>
      <span class="close-button is-size-4" aria-label="close" @click.prevent.stop="close"
        >&#215;</span
      >
    </header>
    <section class="modal-card-body">
      <div class="columns">
        <div class="column is-narrow">
          <div class="box is-clearfix">
            <img class="profile_foot_shape_img" src="/static/images/footshape/shape1.jpg" alt />
            <h4 class="has-text-weight-bold">Egyptian</h4>
            <span class="has-text-grey is-size-6">Big toe longest, other toes taper off</span>
          </div>
          <div class="box is-clearfix">
            <img class="profile_foot_shape_img" src="/static/images/footshape/shape2.jpg" alt />
            <h4 class="has-text-weight-bold">Roman</h4>
            <span class="has-text-grey is-size-6"
              >First 2 or 3 toes the same length, the rest taper off</span
            >
          </div>
          <div class="box is-clearfix">
            <img class="profile_foot_shape_img" src="/static/images/footshape/shape3.jpg" alt />
            <h4 class="has-text-weight-bold">Greek</h4>
            <span class="has-text-grey is-size-6">2nd toe is longest, other toes taper off</span>
          </div>
        </div>
        <div class="column">
          <div class="box is-clearfix">
            <img class="profile_foot_shape_img" src="/static/images/footshape/shape4.jpg" alt />
            <h4 class="has-text-weight-bold">Germanic</h4>
            <span class="has-text-grey is-size-6"
              >Big toe longest, other toes about even or very slight taper</span
            >
          </div>
          <div class="box is-clearfix">
            <img class="profile_foot_shape_img" src="/static/images/footshape/shape5.jpg" alt />
            <h4 class="has-text-weight-bold">Celtic</h4>
            <span class="has-text-grey is-size-6">2nd toe is longest, other toes about even</span>
          </div>
        </div>
      </div>
    </section>
    <section class="modal-card-body">
      <button class="button is-pulled-left" @click.prevent.stop="close">Cancel</button>
    </section>
  </Modal>
</template>

<script>
import Modal from '../components/Modal';

export default {
  name: 'FootShapeModal',
  components: { Modal },
  props: {
    show: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      modalSize: 'medium',
    };
  },
  methods: {
    close() {
      this.$emit('close');
    },
  },
};
</script>

<style scoped lang="scss">
//foot shape table
.profile_foot_shape_img {
  float: left;
  height: 75px;
}
.box {
  padding: 0.5em;
}
</style>
