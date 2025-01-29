# Approval Analytics 📊

Approval Analytics is a web-based analytics system designed to track approval statuses of reports across multiple levels: Extensionist, Chairperson, and Dean. The system extracts data from Firebase, processes it using an ETL pipeline, and visualizes the insights through dynamic charts in a React frontend.

## Features 🚀
- **ETL Pipeline**: Extracts data from Firebase, transforms it, and loads it into MySQL.
- **Dockerized Deployment**: Uses Docker for containerized application management.
- **Flask Backend API**: Provides analytics endpoints to retrieve processed report data.
- **React Frontend**: Displays approval statistics and user reports via interactive charts.

## Project Structure 📁
```
C:\midnight
├── docker
│   └── docker-compose.yml       # Docker configuration for services
├── script
│   ├── etl.py                   # Extracts data from Firebase and loads it into MySQL
│   ├── backend
│   │   ├── app.py               # Flask API to serve analytics data
│   │   ├── Dockerfile           # Docker container setup for Flask backend
│   │   ├── requirements.txt     # Dependencies for Flask
│   ├── frontend
│   │   ├── Dockerfile           # Docker container setup for React frontend
│   │   ├── nginx.conf           # Nginx configuration for frontend deployment
│   │   ├── package.json         # Frontend dependencies
│   │   ├── public
│   │   │   └── index.html       # React entry point
│   │   ├── src
│   │   │   ├── App.js           # Main React component
│   │   │   ├── index.js         # React DOM entry point
├── venv                          # Python virtual environment
│   ├── bin
│   ├── include
│   ├── lib
│   ├── pyvenv.cfg 
├── eqar-remote-firebase-adminsdk-fbsvc-e9bfec6efa.json # Firebase Admin SDK credentials
```

## Technologies Used 🛠️
The development of this project is made possible through:

[![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)](https://react.dev/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat&logo=firebase&logoColor=black)](https://firebase.google.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=flat&logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)
[![NGINX](https://img.shields.io/badge/NGINX-009639?style=flat&logo=nginx&logoColor=white)](https://www.nginx.com/)

## Setup Instructions ⚙️
### Prerequisites
- Docker installed ([Download here](https://www.docker.com/))
- Firebase Admin SDK JSON file configured

### Running the Project
1. **Clone the repository:**
   ```sh
   git clone https://github.com/Valerio-SirLance/Approval_Analytics.git
   cd Approval_Analytics
   ```
2. **Run the Docker containers:**
   ```sh
   docker-compose up --build
   ```
3. **Access the frontend:**
   ```sh
   http://localhost
   ```
4. **Access the backend API:**
   ```sh
   http://localhost:5000/api/analytics
   ```

## Understanding the Technology Stack
### What is Docker? 🐳
Docker is a containerization platform that allows applications to run in isolated environments, ensuring consistent behavior across different systems.

### Benefits of Docker in Deployment 💖
- Ensures consistency across environments (development, testing, production).
- Simplifies dependency management.
- Makes scaling easier with containerized microservices.

### ETL Process in the Project 🔄
- **Extract**: Retrieves report data from Firebase.
- **Transform**: Maps and cleans data for structured storage.
- **Load**: Saves the processed data into MySQL for analytics.

### How the Project Works 🏗️
1. Firebase stores report data.
2. The ETL script fetches the data and loads it into MySQL.
3. The Flask backend provides an API to retrieve processed reports.
4. The React frontend visualizes analytics in interactive charts.

## Author
[![Author: Valerio-SirLance🍀](https://img.shields.io/badge/Author-Valerio--SirLance-%2300A86B?style=flat&logo=github&logoColor=white)](https://github.com/Valerio-SirLance)
