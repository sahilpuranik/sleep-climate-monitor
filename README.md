# 💤 Smart Sleep Climate Monitor

A Raspberry Pi-powered smart sleep monitor that uses real-time sensor data and an LSTM neural network to detect anomalies in your room’s climate during sleep. It helps maintain ideal sleeping conditions (~68–69°F) by learning your room’s nightly temperature/humidity patterns and alerting you to disruptions such as AC failure, open windows, or unexpected heat spikes.

---

## 🧠 What This Project Does

- Collects **real-time temperature, humidity**, and (optionally) **air quality** data using sensors connected to a Raspberry Pi.
- Trains an **LSTM model** on your room’s normal nighttime data to learn its behavior.
- Uses the model to **predict what the next temperature should be**, and compares it to the actual reading.
- If the actual value is off by a certain threshold, it triggers an **alert** (email, SMS, or buzzer).
- Runs **entirely on the edge** — no cloud required, just Python and Pi.

---

## ⚙️ Hardware Used

| Component | Purpose |
|----------|---------|
| **Raspberry Pi 4 (4GB or 8GB)** | The core computing unit that runs Python scripts and ML models |
| **DHT22 or BME280 Sensor** | Reads real-time temperature and humidity data |
| *(Optional)* CCS811 / BME680 | Tracks air quality (VOCs/CO₂) |
| **Jumper wires + Breadboard** | Connect sensors to GPIO pins |
| *(Optional)* Buzzer / LED | Provides physical alert for anomalies |
| *(Optional)* OLED screen | Displays current climate conditions |

---

## 📂 Project Structure
### Folder/Module Breakdown:

#### `Data/`
- `raw_logs.csv` – Raw sensor readings (timestamp, temp, humidity).
- `cleaned_logs.csv` – Cleaned + preprocessed data for training the LSTM.
- `anomaly_log.csv` – Stores all detected anomalies for review/logging.

#### `DSmodel/`
- `train_lstm.py` – Prepares training data and trains an LSTM time-series model.
- `predict.py` – Loads trained model to make next-step temperature predictions.
- `sleep_model.h5` – Saved trained LSTM model file.
- `scaler.pkl` – Scaler object used to normalize data (needed during prediction too).

#### `Monitor/`
- `anomaly_detector.py` – Compares real-time temp to model predictions; detects anomalies.
- `alert.py` – Sends alerts via email, SMS (Twilio), or triggers a buzzer/LED.

#### `Sensors/`
- `read_sensor.py` – Reads data from DHT22/BME280 using GPIO.
- `sensor_setup.py` – Handles sensor initialization, pin config, and retries.

#### `Utils/`
- `config.py` – Global constants (e.g., threshold values, sleep hours).
- `helpers.py` – Utility functions (normalization, time formatting, etc).

#### Root:
- `main.py` – Main runner script that ties together sensor reading, prediction, anomaly checking, and alerting.
- `requirements.txt` – List of Python libraries (`pip install -r requirements.txt`)
- `README.md` – You’re reading it :)

---

## 🚀 Roadmap / To-Dos

- [ ] Collect at least 3–5 nights of baseline climate data
- [ ] Train and validate LSTM model locally
- [ ] Build real-time monitoring loop
- [ ] Integrate email or SMS alert system
- [ ] Add night-only mode (10PM–8AM monitoring)
- [ ] (Optional) Display live stats on OLED screen
- [ ] (Optional) Push sensor data to a Flask-based web dashboard

---

## 🧠 Concepts Demonstrated

- 🧩 Sensor interfacing via GPIO
- 📊 Time-series preprocessing for ML
- 🧠 LSTM-based sequence modeling (Keras/TensorFlow)
- 📡 Real-time anomaly detection on the edge
- 📬 Alert systems via APIs (SMTP, Twilio)
- 🔧 Modular, scalable Python architecture

---

## 🛠️ Setup Instructions (Coming Soon)

This section will walk users through:
- Wiring sensors to the Raspberry Pi
- Installing Python dependencies
- Running data collection + model training
- Starting live monitoring

---

## 🧑‍💻 Created by

**Sahil Puranik**  
[`github.com/sahilpuranik`](https://github.com/sahilpuranik)

---
