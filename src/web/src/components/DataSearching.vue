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
    <DataVisualization :data="data" />

  </div>
</template>


<script>
import Papa from 'papaparse';
import DataVisualization from './DataVisualization.vue';


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
    }
  },
  watch: {
    longitude() {
      this.resetData();
      this.searchData();
    },
    latitude() {
      this.resetData();
      this.searchData();
    },
    dataOption() {
      this.resetData();
      this.searchData();
    },
    rateOption() {
      this.resetData();
      this.searchData();
    },
  },
  mounted() {
    this.searchData();
  },
  methods: {
    resetData() {
      this.data = {};
    },
    loadData() {
      let filePath = '';

      if (this.dataOption === 'deck') {
        filePath = '/deck.csv';
      } else if (this.dataOption === 'pier') {
        filePath = this.rateOption === 'high' ? '/pier_high.csv' : '/pier_low.csv';
      } else {
        console.error('Unknown data option:', this.dataOption);
        return;
        
      }
      return filePath
    },
    findClosest(data) {
      const lon = parseFloat(this.longitude);
      const lat = parseFloat(this.latitude);
      const years = data[0].slice(2);
      console.log("year", years);


      const distances = data.slice(1).map(row => {
        const lon_calculate = parseFloat(lon) < 0 ? parseFloat(lon) + 360 : parseFloat(lon);

        const d = Math.sqrt((parseFloat(row[1]) - parseFloat(lat)) ** 2 + (parseFloat(row[0]) - lon_calculate) ** 2);
        return d;
      });
      const closestIndex = distances.indexOf(Math.min(...distances.filter(d => !isNaN(d))));

      return closestIndex

    },
    searchData() {

      const filePath = this.loadData();
      Papa.parse(filePath, {
        download: true,
        complete: (results) => {
          const years = results.data[0].slice(2);
          const closestIndex = this.findClosest(results.data);
          const resultR = results.data.filter((_, index) => index === closestIndex+1);

          // Merge year and data together
          const result = years.reduce((acc, year, index) => {
            acc[year] = resultR[0][index+2]; // +2 to skip latitude and longitude columns
            return acc;
          }, {});

          this.data = result;
          console.log("data", this.data)
        },
        error: (error) => {
          console.error('Error loading CSV:', error);
        },
      });
    },
    
  },
};
</script>
<style scoped>
.data-grid {
  margin-top: -2.5vh;
  padding: 5px;
}

.table-container {
  margin-top: -1vh;
  max-height: 30vh; /* Adjust this value as needed */
  overflow-y: auto;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 6px;
}

th {
  background-color: #f4f4f4;
}
</style>