
import * as turf from '@turf/turf';
import ontario from './ontario.json';
import L from 'leaflet';
import DataGrid from '../components/DataSearching.vue';

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
      selectedOption: 'deck',  // Default option
      rateOption: 'high',      // Default rate option
    };
  },
  mounted() {
    this.initMap();
  },
  watch: {
    latitude(newVal) {
      if (newVal !== null) {
        this.checkCoordinate();
      }
    },
    longitude(newVal) {
      if (newVal !== null) {
        this.checkCoordinate();
      }
    }
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
        this.isWithinOntario = false;
        return;
      }

      const convertedLongitude = this.convertLongitude(this.longitude);
      const convertedLatitude = this.convertLatitude(this.latitude);

      if (convertedLongitude === null || convertedLatitude === null) {
        this.isWithinOntario = false;
        return;
      }

      const point = turf.point([convertedLongitude, convertedLatitude]);

      this.isWithinOntario = turf.booleanPointInPolygon(point, ontario);
      this.errorMessage = this.isWithinOntario ? null : 'The coordinate is not within Ontario.';
    },
    handleDataOptionChange() {
      // Reset rate option when switching data options
      if (this.selectedOption !== 'pier') {
        this.rateOption = 'high';  // Reset to default for non-pier options
      }
    },
  },
};