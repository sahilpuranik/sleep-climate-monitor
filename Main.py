# main.py
# -------------------------------
# This is the main runner script.
# It pulls all the modules together:
# - Reads sensor data (live or mock)
# - Feeds recent readings to LSTM predictor
# - Compares predicted vs. actual values
# - Triggers alerts if an anomaly is detected
# Runs as a loop (e.g., every 5 minutes during sleep hours).
