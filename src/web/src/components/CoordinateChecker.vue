<template>
  <div class="map-container">
    <div id="map" class="map"></div>
    <div class="controls">
      <form @submit.prevent="checkCoordinate" class="form-container">
        <div class="lat-lon-container">
          <div class="form-group">
            <label for="latitude">Latitude:</label>
            <input type="number" v-model.number="latitude" step="any" required>
          </div>
          <div class="form-group">
            <label for="longitude">Longitude:</label>
            <input type="number" v-model.number="longitude" step="any" required>
          </div>
        </div>
        <div class="data-option-container">
          <div class="form-group">
            <label for="dataOption">Component:</label>
            <select v-model="selectedOption" @change="handleDataOptionChange">
              <option value="deck">Deck</option>
              <option value="pier">Pier</option>
            </select>
          </div>
          <div class="form-group" v-if="selectedOption === 'pier'">
            <label for="rateOption">Select Rate:</label>
            <select v-model="rateOption">
              <option value="high">High Rate</option>
              <option value="low">Low Rate</option>
            </select>
          </div>
        </div>
        <!-- <button type="submit">Check</button> -->
      </form>
      <div v-if="isWithinOntario !== null">
        <p v-if="errorMessage">{{ errorMessage }}</p>
        <DataGrid v-if="isWithinOntario === true" :longitude="longitude" :latitude="latitude" :dataOption="selectedOption" :rateOption="rateOption" />
      </div>
    </div>
  </div>
</template>


<script src="../scripts/CoordinateChecker.js"></script>

<style src="../styles/CoordinateChecker.css"></style>
