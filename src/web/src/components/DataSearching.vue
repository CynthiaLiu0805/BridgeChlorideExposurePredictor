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
      closestLatitude: null,
      closestLongitude: null,
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
      this.loadData();
    },
    latitude() {
      this.resetData();
      this.loadData();
    },
    dataOption() {
      this.resetData();
      this.loadData();
    },
    rateOption() {
      this.resetData();
      this.loadData();
    },
  },
  mounted() {
    this.loadData();
  },
  methods: {
    resetData() {
      this.data = {};
      this.closestLatitude = null;
      this.closestLongitude = null;
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
    //   console.log("f", filePath);

      Papa.parse(filePath, {
        download: true,
        // header: true,
        complete: (results) => {
        //   this.data = this.findClosest(results.data);
          const closestPointData = this.findClosest(results.data);
          this.data = closestPointData.values;
          console.log("data", this.data)
        },
        error: (error) => {
          console.error('Error loading CSV:', error);
        },
      });
    },
    findClosest(data) {
      const lon = parseFloat(this.longitude);
      const lat = parseFloat(this.latitude);
      const years = data[0].slice(2);
      console.log("year", years);


      const distances = data.slice(1).map(row => {
        const lon_calculate = parseFloat(lon) < 0 ? parseFloat(lon) + 360 : parseFloat(lon);
        // console.log("row lon", parseFloat(row[0]));
        // console.log("row lat", parseFloat(row[1]));
        // console.log("lat", lat);
        // console.log("lon", lon_calculate);
        // console.log("(parseFloat(row[1]) - parseFloat(lat))", (parseFloat(row[1]) - parseFloat(lat)));
        // console.log("(parseFloat(row[0]) - parseFloat(lon))", (parseFloat(row[0]) - lon_calculate));

        const d = Math.sqrt((parseFloat(row[1]) - parseFloat(lat)) ** 2 + (parseFloat(row[0]) - lon_calculate) ** 2);
        // console.log("d", d);

        return d;
      });
      // console.log("distance", distances)
      const closestIndex = distances.indexOf(Math.min(...distances.filter(d => !isNaN(d))));
          // console.log("closest index", closestIndex);
          // console.log(data[closestIndex+1])

      const resultR = data.filter((_, index) => index === closestIndex+1);
    // console.log("result", resultR);



    //   const validDistances = distances.filter(d => !isNaN(d));
    //   const minDistance = Math.min(...validDistances);

    //   console.log("min dis", validDistances);
    //   console.log("min", minDistance);


    //   const closestIndex = distances.indexOf(Math.min(...validDistances));
    //   const closestRow = data[closestIndex + 1]; // +1 to account for the header row
    //   console.log("cloest row", distances.indexOf(minDistance));


      // Merge year and data together
      const result = years.reduce((acc, year, index) => {
        acc[year] = resultR[0][index+2]; // +2 to skip latitude and longitude columns
        return acc;
      }, {});

        return {
        values: result,
        latitude: resultR[1],
        longitude: resultR[0],
      };


    //   console.log("data", validDistances);
    //   console.log("cloestindex", Math.min(...validDistances));
    //   return data.filter((_, index) => index === closestIndex);
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