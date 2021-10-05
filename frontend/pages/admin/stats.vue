<template>
  <div>
    <div class="columns">
      <div class="column">
        <h2 class="is-size-4 has-text-centered has-text-primary">
          Admin Stats
        </h2>
        <hr />
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <h5>User Items: {{ all_user_items_count }}</h5>
        <hr />
        <h5>Users: {{ all_users_count }}</h5>
        <hr />
        <h5>Shoes: {{ shoes_count }}</h5>
        <hr />
        <h5>Popular Shoes:</h5>
        <ul>
          <li v-for="item in user_item_count" :key="item.item.id">
            <NuxtLink
              :to="{
                name: 'shoes-brand-model',
                params: {
                  brand: item.item.brand['name_slug'],
                  model: item.item.model_slug,
                },
              }"
              >{{ item.item.model }}</NuxtLink
            >
            <br />
            Count:
            {{ item.count }} Id: {{ item.item.id }}
            <br />
            <small
              >{{ item.item.gender['name_pretty'] }}
              {{ item.item.type | capitalize }}</small
            >
          </li>
        </ul>
        <h5>Popular Shoes - Not Rock:</h5>
        <ul>
          <li v-for="item in user_item_count_not_rock" :key="item.item.id">
            <NuxtLink
              :to="{
                name: 'shoes-brand-model',
                params: {
                  brand: item.item.brand['name_slug'],
                  model: item.item.model_slug,
                },
              }"
              >{{ item.item.model }}</NuxtLink
            >
            <br />
            Count:
            {{ item.count }} Id: {{ item.item.id }}
            <br />
            <small
              >{{ item.item.gender['name_pretty'] }}
              {{ item.item.type | capitalize }}</small
            >
          </li>
        </ul>
        <hr />
      </div>
      <div class="column">
        <h5>Average shoes for user:</h5>
        <span>{{ average_count_per_user }}</span>
        <hr />
        <h5>Split sizing:</h5>
        <span
          >Left Shoe Slightly Larger Than Right:
          {{ users_with_split_shoes_1 }}</span
        >
        <br />
        <span
          >Right Shoe Slightly Larger Than Left:
          {{ users_with_split_shoes_2 }}</span
        >
        <hr />
        <h5>Gender:</h5>
        <span>Prefer not to say: {{ users_with_gender_0 }}</span>
        <br />
        <span>Male: {{ users_with_gender_1 }}</span>
        <br />
        <span>Female: {{ users_with_gender_2 }}</span>
        <br />
        <hr />
        <h5>Users with most shoes:</h5>
        <ul>
          <li v-for="user in users_with_the_most_items" :key="user.user.id">
            <NuxtLink
              :to="{
                name: 'profile-username',
                params: { username: user.user.username },
              }"
              >{{ user.user.username }}</NuxtLink
            >
            <br />
            <span>Shoes: {{ user.count }}</span>
            <br />
            <small>Created: {{ user.user.date_created_readable }}</small>
            <br />
            <small>Last Login: {{ user.user.date_last_login_readable }}</small>
            <strong>{{ user.username }}</strong>
            <br />
          </li>
        </ul>
        <hr />
      </div>
      <div class="column">
        <h5>Users with foot shape:</h5>
        <span> <strong>1</strong>Egyptian </span>
        - {{ users_with_footshape_1.length }}
        <br />
        <span> <strong>2</strong>Roman </span>
        - {{ users_with_footshape_2.length }}
        <br />
        <span> <strong>3</strong>Greek </span>
        - {{ users_with_footshape_3.length }}
        <br />
        <span> <strong>4</strong>Germanic </span>
        - {{ users_with_footshape_4.length }}
        <br />
        <span> <strong>5</strong>Celtic </span>
        - {{ users_with_footshape_5.length }}
        <br />
        <hr />
        <h5>Users with climbing skill:</h5>
        <span>Boulder</span>
        - {{ users_with_boulder }}
        <br />
        <span>Trad</span>
        - {{ users_with_trad }}
        <br />
        <span>Sport</span>
        - {{ users_with_sport }}
        <br />
        <hr />
      </div>
      <div class="column">
        <ul>
          <template v-for="(item, index) in user_items_popular1">
            <li v-if="index == 0" :key="index">
              <h5>
                Most Common Shoe for Users who have
                {{ item.item.brand['name'] }} {{ item.item.model }}:
              </h5>
            </li>
            <li v-if="index != 0" :key="index">
              <NuxtLink
                :to="{
                  name: 'shoes-brand-model',
                  params: {
                    brand: item.item.brand['name_slug'],
                    model: item.item.model_slug,
                  },
                }"
                >{{ item.item.model_slug }}</NuxtLink
              >
              <br />
              Count:
              {{ item.count }} Id: {{ item.item.id }}
              <br />
              <small
                >{{ item.item.gender['name_pretty'] }}
                {{ item.item.type | capitalize }}</small
              >
            </li>
          </template>
        </ul>
        <ul>
          <template v-for="(item, index) in user_items_popular2">
            <li v-if="index == 0" :key="index">
              <h5>
                Most Common Shoe for Users who have
                {{ item.item.brand['name'] }} {{ item.item.model }}:
              </h5>
            </li>
            <li v-if="index != 0" :key="index">
              <NuxtLink
                :to="{
                  name: 'shoes-brand-model',
                  params: {
                    brand: item.item.brand['name_slug'],
                    model: item.item.model_slug,
                  },
                }"
                >{{ item.item.model_slug }}</NuxtLink
              >
              <br />
              Count:
              {{ item.count }} Id: {{ item.item.id }}
              <br />
              <small
                >{{ item.item.gender['name_pretty'] }}
                {{ item.item.type | capitalize }}</small
              >
            </li>
          </template>
        </ul>
        <ul>
          <template v-for="(item, index) in user_items_popular3">
            <li v-if="index == 0" :key="index">
              <h5>
                Most Common Shoe for Users who have
                {{ item.item.brand['name'] }} {{ item.item.model }}:
              </h5>
            </li>
            <li v-if="index != 0" :key="index">
              <NuxtLink
                :to="{
                  name: 'shoes-brand-model',
                  params: {
                    brand: item.item.brand['name_slug'],
                    model: item.item.model_slug,
                  },
                }"
                >{{ item.item.model_slug }}</NuxtLink
              >
              <br />
              Count:
              {{ item.count }} Id: {{ item.item.id }}
              <br />
              <small
                >{{ item.item.gender['name_pretty'] }}
                {{ item.item.type | capitalize }}</small
              >
            </li>
          </template>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { capitalize } from '@/filters';

export default {
  name: 'Stats',
  filters: {
    capitalize,
  },
  layout: 'noHomepageForm',
  middleware: ['auth'],
  data() {
    return {
      shoes_count: 0,
      average_count_per_user: '',
      all_user_items_count: 0,
      all_users_count: 0,
      users_with_gender_0: 0,
      users_with_gender_1: 0,
      users_with_gender_2: 0,
      users_with_split_shoes_1: 0,
      users_with_split_shoes_2: 0,
      users_with_footshape_1: [],
      users_with_footshape_2: [],
      users_with_footshape_3: [],
      users_with_footshape_4: [],
      users_with_footshape_5: [],
      user_item_count: [],
      user_item_count_not_rock: [],
      users_with_the_most_items: [],
      user_items_popular1: [],
      user_items_popular2: [],
      user_items_popular3: [],
      users_with_boulder: [],
      users_with_trad: [],
      users_with_sport: [],
    };
  },
  head() {
    return {
      title: 'Admin',
    };
  },
  created() {
    this.$store.dispatch('GET_ADMIN_STATS').then((response) => {
      Object.keys(response.data).map((key) => {
        this[key] = response.data[key];
        return true;
      });
    });
  },
};
</script>
