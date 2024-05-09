<template>
  <div v-if="totalPages > 1" class="pagination columns is-centered">
    <div class="column has-text-centered">
      Showing {{ startIndex(currentPage) + 1 }} -
      {{ endIndex(currentPage) + 1 }} of {{ total }} {{ noun }}
      <nav
        class="pagination is-centered"
        role="navigation"
        aria-label="pagination"
      >
        <ul class="pagination-list">
          <li>
            <a
              class="pagination-link"
              :disabled="isInFirstPage"
              aria-label="Go to first page"
              @click.prevent.stop="onClickFirstPage"
            >
              &laquo;
            </a>
          </li>

          <li>
            <a
              class="pagination-link"
              :disabled="isInFirstPage"
              aria-label="Go to previous page"
              @click.prevent.stop="onClickPreviousPage"
            >
              &lsaquo;
            </a>
          </li>

          <li v-for="page in pages" :key="page.name">
            <a
              class="pagination-link"
              :disabled="page.isDisabled"
              :class="{ 'is-current': isPageActive(page.name) }"
              :aria-label="`Go to page number ${page.name}`"
              @click.prevent.stop="onClickPage(page.name)"
            >
              {{ page.name }}
            </a>
          </li>

          <li>
            <a
              class="pagination-link"
              :disabled="isInLastPage"
              aria-label="Go to next page"
              @click.prevent.stop="onClickNextPage"
            >
              &rsaquo;
            </a>
          </li>

          <li>
            <a
              class="pagination-link"
              :disabled="isInLastPage"
              aria-label="Go to last page"
              @click.prevent.stop="onClickLastPage"
            >
              &raquo;
            </a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Pagination',
  props: {
    noun: {
      type: String,
      required: true,
    },
    maxVisibleButtons: {
      type: Number,
      required: false,
      default: 10,
    },
    total: {
      type: Number,
      required: true,
    },
    perPage: {
      type: Number,
      required: true,
    },
    currentPage: {
      type: Number,
      required: true,
    },
  },
  computed: {
    totalPages() {
      return Math.ceil(this.total / this.perPage);
    },
    startPage() {
      if (this.currentPage === 1) {
        return 1;
      }

      if (this.currentPage === this.totalPages) {
        return Math.max(this.totalPages - this.maxVisibleButtons + 1, 1);
      }

      return this.currentPage - 1;
    },
    endPage() {
      return Math.min(
        this.startPage + this.maxVisibleButtons - 1,
        this.totalPages
      );
    },
    pages() {
      const range = [];
      let whereToStart = this.startPage;

      if (this.endPage - this.startPage < this.maxVisibleButtons - 1) {
        whereToStart = Math.max(this.endPage - this.maxVisibleButtons + 1, 1);
      }
      for (let i = whereToStart; i <= this.endPage; i += 1) {
        range.push({
          name: i,
          isDisabled: i === this.currentPage,
        });
      }

      return range;
    },
    isInFirstPage() {
      return this.currentPage === 1;
    },
    isInLastPage() {
      return this.currentPage === this.totalPages;
    },
  },
  methods: {
    startIndex(page) {
      return (page - 1) * this.perPage;
    },
    endIndex(page) {
      if (this.startIndex(page) + this.perPage > this.total) {
        return this.total - 1;
      }
      return this.startIndex(page) + this.perPage - 1;
    },

    onClickFirstPage() {
      this.$emit('pagechanged', 1, this.startIndex(1), this.endIndex(1));
    },
    onClickPreviousPage() {
      this.$emit(
        'pagechanged',
        this.currentPage - 1,
        this.startIndex(this.currentPage - 1),
        this.endIndex(this.currentPage - 1)
      );
    },
    onClickPage(page) {
      this.$emit(
        'pagechanged',
        page,
        this.startIndex(page),
        this.endIndex(page)
      );
    },
    onClickNextPage() {
      this.$emit(
        'pagechanged',
        this.currentPage + 1,
        this.startIndex(this.currentPage + 1),
        this.endIndex(this.currentPage + 1)
      );
    },
    onClickLastPage() {
      this.$emit(
        'pagechanged',
        this.totalPages,
        this.startIndex(this.totalPages),
        this.endIndex(this.totalPages)
      );
    },
    isPageActive(page) {
      return this.currentPage === page;
    },
  },
};
</script>

<style scoped lang="scss">
.pagination {
  margin-top: 0.65em;
}
</style>
