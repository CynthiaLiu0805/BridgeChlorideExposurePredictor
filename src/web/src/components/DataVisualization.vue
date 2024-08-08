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

<script src="../scripts/DataVisualization.js"></script>

<style src="../styles/DataVisualization.css"></style>
