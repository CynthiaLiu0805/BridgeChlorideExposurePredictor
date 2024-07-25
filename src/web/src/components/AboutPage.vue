<template>
  <div v-if="show" class="modal-overlay" @click="close">
    <div class="modal-content" @click.stop>
      <span class="close" @click="close">&times;</span>
      <h2>About</h2>
      <p>This is the Bridge Chloride Exposure Predictor application. Here you can find information about bridge chloride exposure prediction and how to use the app.</p>
      <!-- Add more information as needed -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'AboutPage',
  props: {
    show: {
      type: Boolean,
      required: true,
    },
  },
  methods: {
    close() {
      this.$emit('close');
    },
  },
};
</script>

<style>
.modal-overlay {
  position: fixed;
  top: 0vh;
  right: 0;
  width: 300px;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: flex-end;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background-color: white;
  padding: 20px;
  width: 300px;
  height: 100%;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
}

.close {
  position: absolute;
  top: 10px;
  right: 20px;
  font-size: 1.5em;
  cursor: pointer;
}
</style>
