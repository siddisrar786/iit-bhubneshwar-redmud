# iit-bhubneshwar-redmud
🌱 IoT-Based Soil Monitoring System 🌍 Developed at IIT Bhubaneswar under Prof. Dr. B.H. Rao, this project tracks real-time soil NPK, pH, and moisture levels to study the impact of red mud soil (highly alkaline). Features: 📊 Live data visualization, 🌐 IoT-enabled ESP32 system. Applications: Precision farming &amp; soil research! 🚀

# IoT System for Monitoring Soil NPK, pH, and Moisture Levels

This project is an Internet of Things (IoT) system that monitors soil health by measuring **NPK levels**, **pH**, and **moisture**. It is designed to assess the effect of adding **red mud soil**, a highly alkaline substance, on soil nutrients and pH levels. The system sends real-time data to a server and visualizes it on a dashboard.

---

## Features
1. **Real-Time Monitoring**:
   - Tracks NPK levels, pH, and moisture in the soil.
2. **Data Transmission**:
   - Sends data to a server via Wi-Fi.
3. **Visualization**:
   - Displays data trends using interactive graphs on a web dashboard.
4. **Ease of Deployment**:
   - Can be easily set up and calibrated for agricultural or research use.

---

## Components
### Hardware
- **ESP32**: Microcontroller to collect and transmit data.
- **Soil NPK Sensor**: Measures nitrogen, phosphorus, and potassium levels.
- **pH Sensor**: Monitors soil pH levels.
- **Moisture Sensor**: Measures soil moisture percentage.
- Breadboard, jumper wires, and a 5V power supply.

### Software
- **Firmware**: Python-based ESP32 code for sensor interfacing and data transmission.
- **Server**: Python Flask-based API to receive, store, and visualize data.
- **Database**: SQLite for storing sensor readings.
- **Dashboard**: Web interface for data visualization using Chart.js.

---

## Project Structure
soil-monitoring-iot/ ├── esp32/ │ └── main.py # ESP32 firmware for reading sensors and sending data ├── server/ │ ├── server.py # Flask-based server │ ├── soil_data.db # SQLite database (auto-created) │ └── templates/ │ └── dashboard.html # Web dashboard template └── README.md # Project documentation


---

## How It Works
1. **Data Collection**:
   - Sensors collect real-time soil data.
2. **Data Transmission**:
   - ESP32 sends sensor data to the Flask server via Wi-Fi.
3. **Data Storage**:
   - The Flask server stores data in an SQLite database.
4. **Data Visualization**:
   - Data is displayed on a web dashboard with interactive graphs.

---

## Setup and Usage
### 1. Clone the Repository
```bash
git clone https://github.com/siddisrar786/iit-bhubneshwar-redmud.git
cd soil-monitoring-iot
2. ESP32 Firmware Setup
Upload the Code:

Navigate to the esp32/ directory and edit main.py:
Replace Your_WiFi_SSID and Your_WiFi_Password with your Wi-Fi credentials.
Replace API_URL with your server's URL (e.g., http://<server-ip>:5000/api).
Use the Arduino IDE or other tools to upload main.py to the ESP32.
Connect Sensors:

NPK Sensor to GPIO32.
pH Sensor to GPIO33.
Moisture Sensor to GPIO34.
Power the ESP32:

Use a 5V USB or battery pack.
3. Server Setup
Install Dependencies:

Python 3.9+ required.
Install Flask:
pip install flask
Run the Server:

python server/server.py
Access the Dashboard:

Open a browser and visit http://127.0.0.1:5000/ (or the server's IP if hosted remotely).
Test the API:

Send data manually to http://127.0.0.1:5000/api using Postman or cURL:
curl -X POST -H "Content-Type: application/json" \
-d '{"npk": 50.5, "ph": 7.2, "moisture": 30.8}' \
http://127.0.0.1:5000/api
4. Data Visualization
The dashboard (http://127.0.0.1:5000/) displays the following:

NPK Levels:
Real-time graph showing nitrogen, phosphorus, and potassium percentages.
pH Levels:
Tracks the alkalinity/acidity of the soil.
Moisture Levels:
Displays soil moisture percentages over time.
Example Graphs:


Applications
Precision Agriculture:
Monitor soil health and optimize fertilization.
Environmental Research:
Study the effects of red mud soil on crop sustainability.
Educational Projects:
Learn about IoT, sensors, and data visualization.
Troubleshooting
Wi-Fi Connection Issues:

Ensure the correct SSID and password are configured in main.py.
Verify the ESP32 is in range of the Wi-Fi network.
Data Not Appearing on Dashboard:

Check if the Flask server is running.
Verify the API URL in main.py.
Sensor Calibration:

Follow the manufacturer's instructions to calibrate sensors.
Future Improvements
Advanced Analytics:
Integrate machine learning for trend prediction.
Cloud Deployment:
Host the server on AWS, Heroku, or Azure for remote access.
Battery Optimization:
Add solar panels for sustainable power.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

License
This project is licensed under the MIT License.
