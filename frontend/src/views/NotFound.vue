<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const goHome = () => {
  router.push('/home');
};
</script>

<template>
  <div class="not-found-container">
    <div class="content-box">
      <div class="error-code">404</div>
      <h1 class="fw-bold mb-4">Page Not Found</h1>
      <p class="mb-4">Oops! The page you're looking for doesn't exist or has been moved.</p>

      <div class="illustration mb-4">
        <div class="recycling-bin">
          <div class="bin-top"></div>
          <div class="bin-body">
            <div class="recycle-symbol">♻️</div>
          </div>
        </div>
      </div>

      <button @click="goHome" class="btn btn-primary px-4 py-2 fw-bold">
        <i class="fas fa-home me-2"></i>Return Home
      </button>
    </div>
  </div>
</template>

<style scoped>
.not-found-container {
  min-height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 2rem;
  background-color: #f8f9fa;
}

.content-box {
  max-width: 600px;
  padding: 3rem;
  background-color: white;
  border-radius: 1rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.error-code {
  font-size: 8rem;
  font-weight: bold;
  line-height: 1;
  color: var(--bs-primary);
  margin-bottom: 1rem;
  text-shadow: 3px 3px 0 rgba(0, 0, 0, 0.1);
}

.illustration {
  height: 180px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.recycling-bin {
  position: relative;
  width: 120px;
  height: 140px;
}

.bin-top {
  position: absolute;
  top: 0;
  width: 140px;
  height: 30px;
  background-color: var(--bs-primary);
  border-radius: 10px 10px 0 0;
  left: -10px;
}

.bin-body {
  position: absolute;
  top: 25px;
  width: 120px;
  height: 110px;
  background-color: #e9ecef;
  border: 3px solid var(--bs-primary);
  border-top: none;
  border-radius: 0 0 10px 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.recycle-symbol {
  font-size: 3rem;
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s;
}
</style>