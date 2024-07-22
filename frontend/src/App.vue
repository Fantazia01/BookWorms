<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <div class="container">
    <header class="header">
      <h1>Book Worms</h1>
    </header>
    <div class="content">
      <div class="books-container">
        <div v-for="(book, index) in books" :key="index" class="book-row">
          <img src="./assets/3145765.png" alt="Book Image" class="book-image">
          <span class="book-name">{{ book }}</span>
        </div>
      </div>
      <div class="form-container">
        <form @submit.prevent="submitForm" class="user-form">
          <h2>Submit Your Details</h2>
          <div class="form-group">
            <label for="firstName">First Name</label>
            <input type="text" v-model="form.firstName" id="firstName" required>
          </div>
          <div class="form-group">
            <label for="lastName">Family Name</label>
            <input type="text" v-model="form.lastName" id="lastName" required>
          </div>
          <div class="form-group">
            <label for="email">E-mail</label>
            <input type="email" v-model="form.email" id="email" required>
          </div>
          <div class="form-group">
            <label for="motivation">Motivational Letter</label>
            <textarea v-model="form.motivation" id="motivation" required></textarea>
          </div>
          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      books: [],
      form: {
        firstName: '',
        lastName: '',
        email: '',
        motivation: ''
      }
    };
  },
  mounted() {
    fetch('https://backend-broken-fog-2845.fly.dev/books')
      .then(response => response.json())
      .then(data => {
        this.books = data;
      })
      .catch(error => {
        console.error('There was an error fetching the books!', error);
      });
  },
  methods: {
    submitForm() {
      // Handle form submission
      console.log('Form submitted:', this.form);
    },
    getBookImage(imageUrl) {
      // Function to handle image URL, return placeholder if URL is invalid
      return imageUrl ? imageUrl : './assets/placeholder.png';
    }
  }
};
</script>

<style scoped>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #303030; /* Darker background color */
  color: #fff; /* Text color */
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
  background-color: #303030; /* Darker background color */
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.header {
  text-align: center;
  margin-bottom: 2rem;
}

.header h1 {
  font-size: 2.5rem;
  color: #fff; /* Title text color */
}

.content {
  width: 100%;
  max-width: 800px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.books-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 2rem;
}

.book-row {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 1rem;
}

.book-image {
  width: 100px;
  height: 100px;
  margin-bottom: 0.5rem;
}

.book-name {
  text-align: center;
}

.form-container {
  width: 100%;
  max-width: 400px;
  display: flex;
  justify-content: center;
}

.user-form {
  width: 100%;
  padding: 2rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: rgba(255, 255, 255, 0.95); /* Semi-transparent white background */
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.user-form h2 {
  margin-bottom: 1rem;
  text-align: center;
}

.form-group {
  width: 100%;
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #333; /* Label text color */
}

input, textarea {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9; /* Input background color */
  color: #333; /* Input text color */
}

textarea {
  resize: vertical;
}

button {
  width: 100%;
  padding: 0.5rem 1rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>

