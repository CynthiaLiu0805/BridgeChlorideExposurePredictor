<template>
  <div id="app">
    <nav>
      <div class="nav-left">Bridge Chloride Exposure Predictor</div>
      <div class="nav-right">
        <a href="#" @click.prevent="toggleModal">About</a>
      </div>
    </nav>
    <CoordinateChecker />
    <!-- <DataVisualization :data="data" /> -->
    <AboutPage :show="isModalVisible" @close="toggleModal" />
  </div>
</template>

<script src="./scripts/AppScript.js"></script>

<style src="./styles/AppStyle.css"></style>

