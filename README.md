 # IoT 3-Room Virtual Dashboard

This project simulates a smart IoT system with 3 virtual rooms. It tracks temperature and humidity for each room and displays the data on a real-time web dashboard built with Flask. Graphs are generated using Matplotlib, and alerts are triggered when values exceed thresholds. Optional integration with ThingSpeak allows cloud monitoring.  

---

## Objective

The IoT 3-Room Dashboard demonstrates real-time IoT data simulation, visualization, and alert mechanisms. It helps learners understand IoT workflows: sensor → cloud → dashboard, without requiring physical hardware.  

---

## Project Overview

This project is divided into two main components for clarity and modularity:

1. **Simulation Script (`IoT3Rooms.py`)** – Generates random temperature and humidity data for 3 rooms.  
2. **Dashboard (`iot_dashboard.py`)** – Visualizes data in real-time using Flask and Matplotlib.  

---

## Components

### 1. IoT Simulation (`IoT3Rooms.py`)
- **Purpose:** Simulates three rooms with varying temperature and humidity.  
- **Key Features:**
  - Randomized sensor data generation for multiple rooms.  
  - Adjustable thresholds for alert notifications.  
  - Optional API integration with ThingSpeak for cloud storage.  

### 2. Dashboard (`iot_dashboard.py`)
- **Purpose:** Displays real-time temperature and humidity data on a web dashboard.  
- **Key Features:**
  - Flask-based web server for live updates.  
  - Matplotlib-generated graphs embedded in the dashboard.  
  - Alerts for rooms exceeding thresholds.  
- **Dependencies:** Flask, Matplotlib, Pandas, Requests.  
- **Usage:**  
  1. Install dependencies:
     ```bash
     pip install flask matplotlib pandas requests
     ```
  2. Run the script:
     ```bash
     python iot_dashboard.py
     ```
  3. Open your browser at:
     ```
     http://127.0.0.1:5000/
     ```
  4. Press `CTRL+C` in PowerShell to stop the server.  
---

## Challenges Faced
- Generating realistic sensor data for multiple rooms.  
- Updating Matplotlib graphs in real-time within Flask.  
- Integrating optional ThingSpeak API for cloud simulation.  

---

## Future Enhancements
- Connect to real IoT sensors (e.g., DHT11/DHT22).  
- Add more rooms and multiple types of sensor data (CO2, light, motion).  
- Include interactive dashboard controls for thresholds and alerts.  
- Integrate with cloud platforms like Azure IoT Hub or AWS IoT Core.  

---

## Folder Structure

IoT-3Room-Dashboard/
│
├── IoT3Rooms.py # Simulation script
├── iot_dashboard.py # Flask dashboard
├── README.md # Project documentation

---
![iot recording](https://github.com/user-attachments/assets/71061556-cd99-470e-ba6e-658da022c8d3)


## Learning Outcomes
- Python scripting for IoT simulation  
- Real-time data visualization with Flask and Matplotlib  
- Understanding IoT architecture: sensor → cloud → dashboard  
- Working with web frameworks and API integrations  
