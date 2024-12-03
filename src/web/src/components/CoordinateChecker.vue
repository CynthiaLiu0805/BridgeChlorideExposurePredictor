<template>
  <div class="map-container">
    <div id="map" class="map"></div>
    <div class="controls">
      <form @submit.prevent="checkCoordinate" class="form-container">
        <div class="lat-lon-container">
          <div class="form-group">
            <label for="latitude">Latitude:</label>
            <input type="number" v-model.number="latitude" step="any" required>
          </div>
          <div class="form-group">
            <label for="longitude">Longitude:</label>
            <input type="number" v-model.number="longitude" step="any" required>
          </div>
        </div>
        <div class="data-option-container">
          <div class="form-group">
            <label for="dataOption">Component:</label>
            <select v-model="selectedOption" @change="handleDataOptionChange">
              <option value="deck">Deck</option>
              <option value="pier">Pier</option>
            </select>
          </div>
          <div class="form-group" v-if="selectedOption === 'pier'">
            <label for="rateOption">Select Salt Application Rate:</label>
            <select v-model="rateOption">
              <option value="high">High Rate</option>
              <option value="low">Low Rate</option>
            </select>
          </div>
        </div>
        <!-- <button type="submit">Check</button> -->
      </form>
      <div v-if="isWithinOntario !== null">
        <p v-if="errorMessage">{{ errorMessage }}</p>
        <DataGrid v-if="isWithinOntario === true" :longitude="longitude" :latitude="latitude" :dataOption="selectedOption" :rateOption="rateOption" />
      </div>
    </div>
  </div>
</template>


<script>

import L from 'leaflet';
import DataGrid from '../components/DataSearching.vue';
import {
  convertLongitude,
  convertLatitude,
  checkCoordinate,
  handleDataOptionChange,
} from '@/scripts/CoordinateChecker.js';
export default {
  name: 'InputCheck',
  components: {
    DataGrid,
  },
  data() {
    return {
      latitude: null,
      longitude: null,
      isWithinOntario: null,
      errorMessage: null,
      map: null,
      selectedOption: 'deck', // Default option
      rateOption: 'high', // Default rate option
    };
  },
  mounted() {
    this.initMap();
  },
  watch: {
    latitude(newVal) {
      if (newVal !== null) {
        this.updateCoordinateCheck();
      }
    },
    longitude(newVal) {
      if (newVal !== null) {
        this.updateCoordinateCheck();
      }
    },
  },
  methods: {
    convertLongitude,
    convertLatitude,
    initMap() {
      this.map = L.map('map').setView([44.0, -80.0], 6); // Set initial view to Ontario

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution:
          '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      }).addTo(this.map);

      this.map.on('click', this.handleMapClick);
    },
    handleMapClick(event) {
      const lat = event.latlng.lat;
      const lon = event.latlng.lng;

      this.latitude = lat;
      this.longitude = lon;

      this.updateCoordinateCheck();
    },
    updateCoordinateCheck() {
      const result = checkCoordinate(
        this.latitude,
        this.longitude
      );
      this.isWithinOntario = result.isWithinOntario;
      this.errorMessage = result.errorMessage;
    },
    handleDataOptionChange() {
      this.rateOption = handleDataOptionChange(
        this.selectedOption,
        this.rateOption
      );
    },
  },
};
</script>
<style src="../styles/CoordinateChecker.css"></style>
