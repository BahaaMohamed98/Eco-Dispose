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

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

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

## Development Notes

- API base URL is configured in [`jsconfig.json`](jsconfig.json).
- Authentication state is managed in [`store.js`](src/store/store.js).
