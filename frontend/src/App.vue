<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <div>
    <ul>
      <li v-for="book in books">{{ book }}</li>
    </ul>
  </div>
</template>

<script>

export default {
  data() {
    return {
      books: []
    };
  },
  mounted() {
    fetch('http://localhost:8000/books')
    .then(response => response.json())  
    .then(data => {
        this.books = data;
      })
      .catch(error => {
        console.error('There was an error fetching the books!', error);
      });
  }
};
</script>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
