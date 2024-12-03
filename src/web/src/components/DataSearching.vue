<template>
  <div v-if="Object.keys(data).length" class="data-grid">
    <h4>{{ headerText }}</h4>
    <div v-if="latitude && longitude" class="subtitle">
      <!-- <p>Latitude: {{ latitude }}</p>
      <p>Longitude: {{ longitude }}</p> -->
    </div>
 
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>Year</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(entry, year) in data" :key="year">
            <td>{{ year }}</td>
            <td>{{ entry }}</td>
          </tr>
        </tbody>
      </table>
      
    </div>
    <DataVisualization :data="data" 
    :longitude="longitude" 
    :latitude="latitude" 
    :componentType="dataOption" 
    :saltApplicationRate="rateOption" />

  </div>
</template>
<!-- <script src="../scripts/DataSearching.js"></script> -->
<script>
import DataVisualization from '../components/DataVisualization.vue';
import { determineFilePath, parseCSVAndFindData } from '@/scripts/DataSearching';

export default {
  name: 'DataSearching',
  components: {
    DataVisualization,
  },
  props: ['longitude', 'latitude', 'dataOption', 'rateOption'],
  data() {
    return {
      data: {},
    };
  },
  computed: {
    headerText() {
      return `Data for (${this.latitude}, ${this.longitude})`;
    },
  },
  watch: {
    longitude() {
      this.searchData();
    },
    latitude() {
      this.searchData();
    },
    dataOption() {
      this.searchData();
    },
    rateOption() {
      this.searchData();
    },
  },
  mounted() {
    this.searchData();
  },
  methods: {
    searchData() {
      if (!this.longitude || !this.latitude) {
        this.data = {};
        return;
      }

      try {
        const filePath = determineFilePath(this.dataOption, this.rateOption);
        parseCSVAndFindData(
          filePath,
          parseFloat(this.latitude),
          parseFloat(this.longitude),
          (result) => {
            this.data = result;
          },
          (error) => {
            console.error('Error loading CSV:', error);
          }
        );
      } catch (error) {
        console.error(error.message);
        this.data = {};
      }
    },
  },
};
</script>
<style src="../styles/DataSearching.css"></style>
