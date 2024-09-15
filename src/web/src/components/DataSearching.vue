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
<script src="../scripts/DataSearching.js"></script>

<style src="../styles/DataSearching.css"></style>
