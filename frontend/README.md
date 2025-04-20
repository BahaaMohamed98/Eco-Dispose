# Eco-Dispose Frontend

Vue.js single-page application for the Eco-Dispose e-waste management system.

## Features

- Responsive design
- Component-based architecture
- Vue Router for navigation
- State management with reactive store
- Form validation and error handling

## Project Structure

```text
frontend/
├── public/             # Static assets
├── src/
│   ├── assets/         # Images, fonts, etc.
│   ├── components/     # Reusable Vue components
│   ├── router/         # Vue Router configuration
│   ├── store/          # State management
│   ├── views/          # Page components
│   ├── App.vue         # Root component
│   └── main.js         # Application entry point
├── index.html          # HTML template
└── vite.config.js      # Vite configuration
```

## Setup

### Install dependencies

```bash
npm install
```

This will install all the required dependencies listed in `package.json`.

### Run development server

```bash
npm run dev
```

This will start a local development server at `http://localhost:5000`.

### Build for production

```bash
npm run build
npm run preview
```

This will create a production build in the `dist` directory and start a local server to preview it.

## Views

- `HomePage`: Landing page with project overview
- `Register`: User registration page
- `Login`: User login page
- `Profile`: User profile page
- `Listings`: List of submitted devices
- `Upload`: Form for submitting new devices
- `Admin`: Admin dashboard for device evaluation
- `About`: Information about the project and team
- `NotFound`: 404 error page

## Components

- `Navbar`: Navigation bar with links to different pages
- `Footer`: Footer with links and copyright
- `ToastContainer`: Container for toast notifications

## Development Notes

- API base URL is configured in [`jsconfig.json`](jsconfig.json).
- Authentication state is managed in [`store.js`](src/store/store.js).
