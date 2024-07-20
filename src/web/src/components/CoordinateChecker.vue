<template>
  <div class="map-container">
    <div id="map" class="map" ></div>
    <div class="controls">
      <!-- <h5>Check if a Coordinate is in Ontario</h5> -->
      <form @submit.prevent="checkCoordinate">
        <div>
          <label for="latitude">Latitude:</label>
          <input type="number" v-model.number="latitude" step="any" required>
        </div>
        <div>
          <label for="longitude">Longitude:</label>
          <input type="number" v-model.number="longitude" step="any" required>
        </div>
        <div>
          <label for="dataOption">Select Data Source:</label>
          <select v-model="selectedOption" @change="handleDataOptionChange">
            <option value="deck">Deck</option>
            <option value="pier">Pier</option>
          </select>
        </div>
        <div v-if="selectedOption === 'pier'">
          <label for="rateOption">Select Rate:</label>
          <select v-model="rateOption">
            <option value="high">High Rate</option>
            <option value="low">Low Rate</option>
          </select>
        </div>
        <!-- <button type="submit">Check</button> -->
      </form>
      <div v-if="result !== null">
        <!-- <p v-if="result === true">The coordinate is within Ontario.</p> -->
        <!-- <p v-if="result === false">The coordinate is not within Ontario.</p> -->
        <p v-if="errorMessage">{{ errorMessage }}</p>
        <DataGrid v-if="result === true" :longitude="longitude" :latitude="latitude" :dataOption="selectedOption" :rateOption="rateOption" />
      </div>
    </div>
  </div>
</template>

<script>
import * as turf from '@turf/turf';
import ontario from './ontario.json';
import L from 'leaflet';
import DataGrid from './DataGrid.vue';

export default {
  name: 'InputCheck',
  components: {
    DataGrid,
  },
  data() {
    return {
      latitude: null,
      longitude: null,
      result: null,
      errorMessage: null,
      map: null,
      selectedOption: 'deck',  // Default option
      rateOption: 'high',      // Default rate option
    };
  },
  mounted() {
    this.initMap();
  },
  methods: {
    convertLongitude(lon) {
      try {
        const floatLon = parseFloat(lon);
        if (isNaN(floatLon)) {
          throw new Error('InputTypeMismatchError: Invalid longitude');
        }
        return floatLon > 0 ? floatLon - 360 : floatLon;
      } catch (error) {
        this.errorMessage = error.message;
        return null;
      }
    },
    convertLatitude(lat) {
      try {
        const floatLat = parseFloat(lat);
        if (isNaN(floatLat)) {
          throw new Error('InputTypeMismatchError: Invalid latitude');
        }
        return floatLat;
      } catch (error) {
        this.errorMessage = error.message;
        return null;
      }
    },
    initMap() {
      this.map = L.map('map').setView([44.0, -80.0], 6); // Set initial view to Ontario

      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(this.map);

      this.map.on('click', this.handleMapClick);
    },
    handleMapClick(event) {
      const lat = event.latlng.lat;
      const lon = event.latlng.lng;

      this.latitude = lat;
      this.longitude = lon;

      this.checkCoordinate();
    },
    checkCoordinate() {
      if (!ontario) {
        this.errorMessage = 'Ontario GeoJSON data is not loaded or is invalid.';
        this.result = false;
        return;
      }

      const convertedLongitude = this.convertLongitude(this.longitude);
      const convertedLatitude = this.convertLatitude(this.latitude);

      if (convertedLongitude === null || convertedLatitude === null) {
        this.result = false;
        return;
      }

      const point = turf.point([convertedLongitude, convertedLatitude]);

      this.result = turf.booleanPointInPolygon(point, ontario);
      this.errorMessage = this.result ? null : 'The coordinate is not within Ontario.';
    },
    handleDataOptionChange() {
      // Reset rate option when switching data options
      if (this.selectedOption !== 'pier') {
        this.rateOption = 'high';  // Reset to default for non-pier options
      }
    },
  },
};
</script>

<style scoped>
.map-container {
  position: relative;
  height: 90vh;
}

.map {
  height: 100%;
}

.controls {
  position: absolute;
  top: 10px;
  left: 10px;
  background: white;
  padding: 5px;
  border-radius: 5px;
  z-index: 1000;
  
}
</style>
