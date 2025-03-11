<template>
  <!-- About Section with improved layout -->
  <section class="container py-5">
    <div class="row align-items-center">
      <div class="col-lg-7">
        <h1 class="about-title">About Us</h1>
        <div class="about-text">
          At <strong class="text-primary">Eco-Dispose</strong>, we believe that
          every electronic device has an end, but that doesn't mean its value is
          lost! We are a team of five passionate individuals who came together
          to create a platform that reduces electronic waste (E-Waste) and
          transforms it into new opportunities. <br /><br />
          Our mission is to connect individuals with old electronic devices to
          recycling companies, ensuring that salvageable parts are reused in
          other industries and devices. This not only helps minimize electronic
          pollution but also maximizes resource efficiency.
          <br /><br />
          We strive to build a sustainable cycle where outdated electronics are
          repurposed rather than discarded, contributing to a cleaner
          environment and a more responsible use of technology.
          <br /><br />
          Join us in making a difference—one device at a time!
        </div>
      </div>
      <div class="col-lg-5 d-flex justify-content-center align-items-center">
        <div class="about-image-container">
          <img
            class="img-fluid about-image"
            src="@/assets/team/logo.png"
            alt="Eco-Dispose Image"
          />
        </div>
      </div>
    </div>
  </section>

  <!-- Team Section with improved spacing -->
  <section class="container py-5">
    <div class="section-header text-center mb-5">
      <h2 class="team-title">Meet Our Team</h2>
      <div class="section-divider mx-auto"></div>
    </div>

    <!-- Team members with more spacing -->
    <div class="row justify-content-center g-4">
      <div class="col-md-4 col-lg-2 mx-3">
        <div class="team-member">
          <div class="member-image-container">
            <img
              class="rounded-circle"
              src="@/assets/team/bahaa.png"
              alt="Bahaa Mohamed"
            />
          </div>
          <div class="team-member-name">Bahaa Mohamed</div>
        </div>
      </div>
      <div class="col-md-4 col-lg-2 mx-3">
        <div class="team-member">
          <div class="member-image-container">
            <img
              class="rounded-circle"
              src="@/assets/team/farouk.png"
              alt="Abdelrahman Hany"
            />
          </div>
          <div class="team-member-name">Abdelrahman Hany</div>
        </div>
      </div>
      <div class="col-md-4 col-lg-2 mx-3">
        <div class="team-member">
          <div class="member-image-container">
            <img
              class="rounded-circle"
              src="@/assets/team/salah.png"
              alt="Ahmed Salah"
            />
          </div>
          <div class="team-member-name">Ahmed Salah</div>
        </div>
      </div>
      <div class="col-md-4 col-lg-2 mx-3">
        <div class="team-member">
          <div class="member-image-container">
            <img
              class="rounded-circle"
              src="@/assets/team/ehab.png"
              alt="Ahmed Ehab"
            />
          </div>
          <div class="team-member-name">Ahmed Ehab</div>
        </div>
      </div>
      <div class="col-md-4 col-lg-2 mx-3">
        <div class="team-member">
          <div class="member-image-container">
            <img
              class="rounded-circle"
              src="@/assets/team/youssef.png"
              alt="Youssef Waleed"
            />
          </div>
          <div class="team-member-name">Youssef Waleed</div>
        </div>
      </div>
    </div>

    <div class="row mt-5">
      <div class="col-lg-10 mx-auto">
        <div class="team-description p-4 bg-light rounded-3">
          We are a team of five driven individuals united by a shared passion
          for sustainability and technology. With diverse skills and a common
          goal, we founded
          <span class="highlight text-primary">Eco-Dispose</span> to make
          electronic recycling easier and more impactful. <br /><br />
          Our strength lies in <span class="teamwork">teamwork</span>,
          innovation, and a commitment to environmental change. Together, we're
          not just building a platform—we're shaping a future where e-waste
          finds new purpose, and sustainability becomes a way of life.
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
body {
  font-family: "Inter", sans-serif;
  overflow-x: hidden;
}

.about-title {
  color: #0d6efd;
  font-size: 64px;
  font-weight: 700;
  margin-top: 30px;
  margin-bottom: 30px;
}

.about-text {
  font-size: 20px;
  font-weight: 500;
  line-height: 30px;
  margin-bottom: 50px;
}

.about-text strong {
  font-weight: 800;
}

.about-image-container {
  position: relative;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  background: #ffffff;
}

.team-title {
  color: #0d6efd;
  font-size: 48px;
  font-weight: 700;
  display: inline-block;
  position: relative;
  margin-bottom: 10px;
}

.section-divider {
  height: 4px;
  width: 80px;
  background: #0d6efd;
  margin-bottom: 40px;
  border-radius: 2px;
}

.team-member {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 30px;
  transition: all 0.3s ease;
}

.team-member:hover {
  transform: translateY(-10px);
}

.member-image-container {
  padding: 5px;
  border-radius: 50%;
  background: linear-gradient(145deg, #ffffff, #f0f0f0);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.team-member img {
  width: 160px;
  height: 160px;
  object-fit: cover;
  border: 4px solid white;
}

.team-member-name {
  color: #0d6efd;
  font-size: 22px;
  font-weight: 600;
  margin-top: 10px;
  text-align: center;
}

.team-description {
  font-size: 22px;
  font-weight: 500;
  line-height: 1.6;
  border-left: 5px solid #0d6efd;
}

.team-description .highlight {
  font-weight: 900;
}

.team-description .teamwork {
  font-weight: 800;
  color: #0d6efd;
}

@media (max-width: 992px) {
  .about-title {
    font-size: 48px;
  }

  .about-text {
    font-size: 18px;
  }

  .team-title {
    font-size: 36px;
  }

  .team-description {
    font-size: 20px;
  }

  .team-member img {
    width: 140px;
    height: 140px;
  }
}

@media (max-width: 768px) {
  .about-title {
    font-size: 36px;
    text-align: center;
  }

  .about-image {
    margin-top: 30px;
    margin-bottom: 30px;
  }

  .member-image-container {
    padding: 4px;
  }

  .team-member img {
    width: 120px;
    height: 120px;
  }

  .row.g-4 {
    row-gap: 2rem !important;
  }
}
</style>
