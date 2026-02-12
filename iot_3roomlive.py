import pandas as pd
import random
import time

# Rooms
rooms = ["Room1", "Room2", "Room3"]

# Create CSV file if it doesn't exist
try:
    df = pd.read_csv("iot_data.csv")
except FileNotFoundError:
    df = pd.DataFrame(columns=["Room","Temperature","Humidity"])
    df.to_csv("iot_data.csv", index=False)

while True:
    new_data = []
    for room in rooms:
        temp = random.randint(20,35)       # simulate temperature
        hum = random.randint(40,70)        # simulate humidity
        new_data.append([room,temp,hum])

    # Append to CSV
    df_new = pd.DataFrame(new_data, columns=["Room","Temperature","Humidity"])
    df = pd.concat([df, df_new], ignore_index=True)
    df.to_csv("iot_data.csv", index=False)

    print("CSV Updated with new sensor data!")
    time.sleep(5)  # every 5 seconds
