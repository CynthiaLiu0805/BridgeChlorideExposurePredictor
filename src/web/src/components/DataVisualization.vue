<template>
  <div>
    <div ref="chartWrapper">
    <line-chart class="chart-wrapper" v-if="data" :data="chartData"  :options="chartOptions"/>
    </div>
    <div class="button-container">

    <button @click="downloadData">Download Data</button>
    <button @click="downloadJPG">Download Chart (JPG)</button>
    </div>
  </div>
</template>

<!-- <script src="../scripts/DataVisualization.js"></script> -->

<script>
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, PointElement, LinearScale, CategoryScale } from 'chart.js';
import { generateChartData, downloadData, downloadJPG } from '@/scripts/DataVisualization';

ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, LinearScale, CategoryScale);

export default {
  name: 'DataVisualization',
  components: {
    LineChart: Line,
  },
  props: {
    data: {
      type: Object,
      required: true,
    },
    longitude: {
      type: Number,
      required: true,
    },
    latitude: {
      type: Number,
      required: true,
    },
    componentType: {
      type: String,
      required: true,
    },
    saltApplicationRate: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      chartData: {
        labels: [],
        datasets: [],
      },
      chartOptions: {},
    };
  },
  watch: {
    data: {
      immediate: true,
      handler(newData) {
        if (newData) {
          const { chartData, chartOptions } = generateChartData(newData);
          this.chartData = chartData;
          this.chartOptions = chartOptions;
        }
      },
    },
  },
  methods: {
    handleDownloadData() {
      downloadData(
        this.data,
        this.longitude,
        this.latitude,
        this.componentType,
        this.saltApplicationRate
      );
    },
    handleDownloadJPG() {
      downloadJPG(
        this.$refs.chartWrapper,
        this.longitude,
        this.latitude,
        this.componentType,
        this.saltApplicationRate
      );
    },
  },
};
</script>
<style src="../styles/DataVisualization.css"></style>
