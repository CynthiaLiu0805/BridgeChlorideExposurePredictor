<template>
  <div id="app">
    <CoordinateChecker />
    <!-- <DataVisualization :data="data" /> -->

  </div>
</template>

<script>
import CoordinateChecker from './components/CoordinateChecker.vue';
import 'leaflet/dist/leaflet.css';
// import DataVisualization from './components/DataVisualization.vue';

export default {
  name: 'App',
  components: {
    CoordinateChecker,
    // DataVisualization,

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
  margin-top: 60px;
}
</style>
