import { createApp } from "vue";
import App from "@/App.vue";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/js/index.esm.js";
import "bootstrap"
import "@/css/main.css";
import router from "@/router/routes.js";
import "bootstrap/dist/js/bootstrap.bundle.min.js";

const app = createApp(App);

app.use(router);

app.mount("#app");
