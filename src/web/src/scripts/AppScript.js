
import CoordinateChecker from '../components/CoordinateChecker.vue';
import AboutPage from '../components/AboutPage.vue';
import 'leaflet/dist/leaflet.css';
// import DataVisualization from './components/DataVisualization.vue';

export default {
  name: 'App',
  components: {
    CoordinateChecker,
    AboutPage,
    // DataVisualization,
  },
  data() {
    return {
      isModalVisible: false,
    };
  },
  methods: {
    toggleModal() {
      this.isModalVisible = !this.isModalVisible;
    },
  },
};