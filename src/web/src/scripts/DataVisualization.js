
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, PointElement, LinearScale, CategoryScale } from 'chart.js';
// import jsPDF from 'jspdf';
// import 'jspdf-autotable';
import html2canvas from 'html2canvas';

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
            label: 'Surface Chloride Concentration Over Time',
            backgroundColor: '#c400a7',
            borderWidth: 1,
            borderColor: '#660057',
            pointRadius: 2.5,
            pointBackgroundColor: '#777B7E', // Set the point color here
            pointBorderColor: 'transparent', // Remove the point border here

            data: values,
          },
        ],
      };
      this.chartOptions = {
      scales: {
        x: {
          title: {
            display: true,
            text: 'Year' // Set your x-axis label here
          }
        },
        y: {
          title: {
            display: true,
            text: 'Chloride Concentration (kg/m^3)' // Set your y-axis label here
          }
        }
      }
    };

      console.log("chart data", data);
    },
    downloadData() {
      // const r = [Object.keys(this.data)];
      // r.push(Object.values(this.data));
      const r = Object.keys(this.data).map(key => [key, this.data[key]]);

      let csvContent = "data:text/csv;charset=utf-8," 
          + r.map(e => e.join(",")).join("\n");

      const downloadAnchorNode = document.createElement('a');
      downloadAnchorNode.setAttribute("href", encodeURI(csvContent));
      downloadAnchorNode.setAttribute("download", "data.csv");
      document.body.appendChild(downloadAnchorNode);
      downloadAnchorNode.click();
      downloadAnchorNode.remove();

      
  
    },
    downloadJPG() {
      this.$nextTick(() => {
        const chartWrapper = this.$refs.chartWrapper;
        if (chartWrapper) {
          html2canvas(chartWrapper).then((canvas) => {
            const imgData = canvas.toDataURL('image/jpeg');
            const link = document.createElement('a');
            link.href = imgData;
            link.download = 'chart.jpg';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
          }).catch((error) => {
            console.error('Error capturing chart:', error);
          });
        } else {
          console.error('chartWrapper is not defined');
        }
      });
    },
    
    
  },
};