<template>
  <div id="app">
    <CoordinateChecker />
  </div>
</template>

<script>
import CoordinateChecker from './components/CoordinateChecker.vue';
import 'leaflet/dist/leaflet.css';

export default {
  name: 'App',
  components: {
    CoordinateChecker,
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
