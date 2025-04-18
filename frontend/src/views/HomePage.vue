<script setup>
import { userStore } from "@/store/userStore.js";
</script>

<template>
  <section>
    <div class="container">
      <div class="px-3 px-md-5" style="margin-top: 80px">
        <div
          class="px-3 px-md-5 d-flex flex-column align-items-center justify-content-center text-center mt-5"
        >
          <h1 class="display-4 text-center mb-3 fw-bold">
            Eco-Dispose For E-Waste Recycling
          </h1>
          <blockquote class="blockquote">
            This project focuses on the proper collection, recycling, and
            disposal of electronic waste (e-waste) to minimize environmental
            impact. It includes awareness campaigns, e-waste collection drives,
            and partnerships with recycling facilities to ensure safe processing
            of discarded electronics. The project aims to reduce pollution,
            recover valuable materials, and promote sustainable practices in
            e-waste management.
          </blockquote>
        </div>
      </div>

      <div class="d-grid gap-2 d-md-flex justify-content-center my-3">
        <!-- login and register buttons -->
        <router-link
          v-if="!userStore.currentUser"
          to="/login"
          class="btn btn-lg btn-primary fw-bold"
          ><i class="fa-solid fa-right-to-bracket"></i> Login
        </router-link>
        <router-link
          v-if="!userStore.currentUser"
          to="/register"
          class="btn btn-lg btn-outline-primary fw-bold"
          ><i class="fa-solid fa-user-plus"></i> Register
        </router-link>
        <router-link
          v-if="userStore.currentUser"
          to="/upload"
          class="btn btn-lg btn-primary fw-bold"
          ><i class="fa-solid fa-arrow-up-from-bracket"></i> Upload Now
        </router-link>
      </div>
    </div>
  </section>

  <div class="container mx-auto d-flex justify-content-center mt-5">
    <img src="@/assets/banner.png" class="w-75 Image img-fluid rounded" />
  </div>

  <section>
    <div class="container mt-5">
      <!-- title -->
      <div class="container">
        <h2 class="mb-4 text-start fw-bold">
          What can I recycle in Eco-Dispose?
        </h2>
      </div>

      <!-- card group -->
      <div class="card-group gap-4">
        <div class="card myCard rounded shadow-sm">
          <img src="@/assets/smartphones.png" class="card-img-top" />
          <div class="card-body">
            <h4 class="fw-bold card-title">Smart Phones</h4>
            <p class="card-text">
              Smartphones, PDAs that support cellular phones, touch screen
              technology, and mobile devices.
            </p>
          </div>
        </div>

        <div class="card myCard rounded shadow-sm">
          <img src="@/assets/dumpster.png" class="card-img-top" />
          <div class="card-body">
            <h4 class="fw-bold card-title">Computers</h4>
            <p class="card-text">
              Computers and all their components such as motherboards, cables,
              and internal parts.
            </p>
          </div>
        </div>

        <div class="card myCard rounded shadow-sm">
          <img src="@/assets/laptops.png" class="card-img-top rounded h-100" />
          <div class="card-body">
            <h4 class="fw-bold card-title">Laptops & Tablets</h4>
            <p class="card-text">
              Includes laptops and tablets, along with their parts like screens,
              CPUs, and other useful components.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container mt-5">
      <h2 class="mb-4 fw-bold">How can I recycle my device in Eco-Dispose?</h2>

      <div class="row align-items-center">
        <!-- Left Side: Content -->
        <div class="col-lg d-flex flex-column">
          <div class="d-flex flex-column gap-3">
            <div class="p-3 shadow-sm rounded border myCard">
              <h5 class="fw-bold">Sign up</h5>
              <p class="mb-0 text-muted">
                Create an account and fill in your details to place an order.
              </p>
            </div>

            <div class="p-3 shadow-sm rounded border myCard">
              <h5 class="fw-bold">Share your Device</h5>
              <p class="mb-0 text-muted">
                Provide details and upload photos of your device.
              </p>
            </div>

            <div class="p-3 shadow-sm rounded border myCard">
              <h5 class="fw-bold">Accept Offer</h5>
              <p class="mb-0 text-muted">
                Receive offers from recycling companies. Accept one, and we will
                send a delivery person to complete the process.
              </p>
            </div>
          </div>

          <router-link
            to="/upload"
            class="btn btn-primary mt-4 align-self-start"
            ><i class="fa-solid fa-arrow-up-from-bracket"></i> Upload Now
          </router-link>
        </div>

        <!-- Right Side: Image -->
        <div class="col-lg d-flex justify-content-center">
          <img
            src="@/assets/kidsRecycling.png"
            class="Image img-fluid rounded w-75"
          />
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container mt-5">
      <div class="row gx-0 mb-3">
        <div class="col">
          <h2 class="fw-bold mb-3 text-start px-0">Why recycling?</h2>
        </div>
      </div>

      <div class="row">
        <div class="col">
          <img
            src="@/assets/RRR.png"
            class="Image img-fluid rounded img-fixed mb-3"
          />
          <h4 class="fw-bold">Energy Efficiency</h4>
          <p>Reduces energy consumption compared to producing new materials.</p>
        </div>

        <div class="col">
          <img
            src="@/assets/recycle.png"
            class="Image img-fluid rounded img-fixed mb-3"
          />
          <h4 class="fw-bold">Resource Conservation</h4>
          <p>Saves natural resources by recovering valuable materials.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="contact" class="py-5">
    <div class="container">
      <h2 class="fw-bold mb-4 text-center">Contact Us</h2>

      <div class="card shadow-lg rounded-4 border-0 overflow-hidden">
        <div class="row g-0">
          <!-- Contact information side -->
          <div class="col-md-5 contact-sidebar text-white p-4 p-md-5">
            <div class="h-100 d-flex flex-column justify-content-between">
              <div>
                <h3 class="mb-4 fw-bold">Get in Touch</h3>
                <p class="mb-4">
                  Have questions about recycling your device? We're here to help
                  with all your inquiries.
                </p>

                <div class="contact-details">
                  <div class="d-flex mb-3 align-items-center">
                    <div class="contact-icon me-3">
                      <i class="fas fa-map-marker-alt"></i>
                    </div>
                    <p class="mb-0">1 SAMS Street, Maadi, Cairo</p>
                  </div>

                  <div class="d-flex mb-3 align-items-center">
                    <div class="contact-icon me-3">
                      <i class="fas fa-envelope"></i>
                    </div>
                    <p class="mb-0">contact@eco-dispose.com</p>
                  </div>

                  <div class="d-flex mb-3 align-items-center">
                    <div class="contact-icon me-3">
                      <i class="fas fa-phone"></i>
                    </div>
                    <p class="mb-0">+20 (2) 555-0123</p>
                  </div>
                </div>
              </div>

              <div class="social-links mt-4">
                <h5 class="mb-3">Connect With Us</h5>
                <div class="d-flex gap-3">
                  <a href="#" class="social-icon"
                    ><i class="fab fa-facebook-f"></i
                  ></a>
                  <a href="#" class="social-icon"
                    ><i class="fab fa-twitter"></i
                  ></a>
                  <a href="#" class="social-icon"
                    ><i class="fab fa-instagram"></i
                  ></a>
                  <a href="#" class="social-icon"
                    ><i class="fab fa-linkedin-in"></i
                  ></a>
                </div>
              </div>
            </div>
          </div>

          <!-- Contact form side -->
          <div class="col-md-7 p-4 p-md-5">
            <h3 class="mb-4 fw-bold">Send us a Message</h3>

            <form>
              <div class="row g-3">
                <div class="col-md-6">
                  <div class="form-floating mb-3">
                    <input
                      type="text"
                      class="form-control"
                      id="name"
                      placeholder="Your Name"
                    />
                    <label for="name"
                      ><i class="fas fa-user text-primary me-2"></i>Your Name
                    </label>
                  </div>
                </div>

                <div class="col-md-6">
                  <div class="form-floating mb-3">
                    <input
                      type="email"
                      class="form-control"
                      id="email"
                      placeholder="Your Email"
                    />
                    <label for="email"
                      ><i class="fas fa-envelope text-primary me-2"></i>Your
                      Email</label
                    >
                  </div>
                </div>

                <div class="col-12">
                  <div class="form-floating mb-3">
                    <input
                      type="text"
                      class="form-control"
                      id="subject"
                      placeholder="Subject"
                    />
                    <label for="subject"
                      ><i class="fas fa-pencil-alt text-primary me-2"></i
                      >Subject</label
                    >
                  </div>
                </div>

                <div class="col-12">
                  <div class="form-floating mb-3">
                    <textarea
                      class="form-control"
                      id="message"
                      style="height: 150px"
                      placeholder="Message"
                    ></textarea>
                    <label for="message"
                      ><i class="fas fa-comment text-primary me-2"></i>Your
                      Message</label
                    >
                  </div>
                </div>

                <div class="col-12">
                  <div class="form-check mb-4">
                    <input
                      class="form-check-input"
                      type="checkbox"
                      id="terms"
                    />
                    <label class="form-check-label" for="terms">
                      I agree to the
                      <a href="#" class="text-decoration-none"
                        >terms and conditions</a
                      >
                    </label>
                  </div>
                </div>

                <div class="col-12">
                  <button type="submit" class="btn btn-primary btn-lg">
                    <i class="fas fa-paper-plane me-2"></i>Send Message
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.contact-sidebar {
  background: linear-gradient(135deg, #5a9eff 0%, #3a7bd5 100%);
  position: relative;
}

.contact-sidebar::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.15);
  z-index: 0;
}

.contact-sidebar > * {
  position: relative;
  z-index: 1;
}

.contact-icon {
  width: 36px;
  height: 36px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.social-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 50%;
  color: white;
  text-decoration: none;
  transition: all 0.3s ease;
}

.social-icon:hover,
.contact-icon:hover {
  background: white;
  color: var(--bs-primary);
  transform: translateY(-3px);
}

.form-floating .form-control:focus {
  border-color: var(--bs-primary);
  box-shadow: 0 0 0 0.25rem rgba(66, 133, 244, 0.25);
}

.form-control {
  border: 1px solid #ced4da;
}

.form-check-input:checked {
  background-color: var(--bs-primary);
  border-color: var(--bs-primary);
}

.card {
  transition: all 0.3s ease;
}

@media (max-width: 767.98px) {
  .social-links {
    margin-top: 2rem;
  }
}

blockquote {
  border-left: 4px solid var(--bs-primary);
  padding-left: 1.5rem;
  font-style: italic;
  color: #6c757d;
}

h2 {
  position: relative;
  display: inline-block;
  margin-bottom: 1.5rem;
}

h2::after {
  content: "";
  position: absolute;
  width: 60%;
  height: 3px;
  background: linear-gradient(90deg, var(--bs-primary), transparent);
  bottom: -10px;
  left: 0;
}
</style>
