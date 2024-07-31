<template>
  <div id="app">
    <nav>
      <div class="nav-left">Bridge Chloride Exposure Predictor</div>
      <div class="nav-right">
        <a href="#" @click.prevent="toggleModal">About</a>
      </div>
    </nav>
    <CoordinateChecker />
    <!-- <DataVisualization :data="data" /> -->
    <AboutPage :show="isModalVisible" @close="toggleModal" />
  </div>
</template>

<script>
import CoordinateChecker from './components/CoordinateChecker.vue';
import AboutPage from './components/AboutPage.vue';
import 'leaflet/dist/leaflet.css';
// import DataVisualization from './components/DataVisualization.vue';

export default {
  name: 'App',
  components: {
    CoordinateChecker,
    AboutPage,
    // DataVisualization,
  },
  data() {
    return {
      isModalVisible: false,
    };
  },
  methods: {
    toggleModal() {
      this.isModalVisible = !this.isModalVisible;
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}

nav {
  display: flex;
  height: 5vh;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #660057;
  color: white;
}

.nav-left {
  font-size: 1.5em;
}

.nav-right a {
  color: white;
  text-decoration: none;
  margin-left: 20px;
  cursor: pointer;
}

.nav-right a:hover {
  text-decoration: underline;
}
</style>
