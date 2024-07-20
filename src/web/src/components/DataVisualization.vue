<template>
  <div>
    <line-chart v-if="data" :data="chartData" />
  </div>
</template>

<script>
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, PointElement, LinearScale, CategoryScale } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, LineElement, PointElement, LinearScale, CategoryScale);

export default {
  name: 'DataVisualization',
  components: {
    LineChart: Line,
  },
  props:  {
    data: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      chartData:  {
        labels: [ ],
        datasets: [ ]
      },
    };
  },
  watch: {
    data: {
      immediate: true,
      handler(newData) {
        if (newData) {
          this.generateChartData(newData);
        }
      },
    },
  },
  methods: {
    generateChartData(data) {
      console.log(data);
      const labels = Object?.keys(data);
      const values = Object?.values(data);
      console.log(labels);

      this.chartData = {
        labels: labels,
        datasets:
        [
          {
            label: 'Value Over Time',
            backgroundColor: '#f87979',
            data: values,
          },
        ],
      };

      console.log("chart data", data);
    },
  },
};
</script>

<style scoped>
</style>