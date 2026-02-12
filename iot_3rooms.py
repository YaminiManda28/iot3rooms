import requests
import random
import time
from datetime import datetime
import csv
API_KEY = "OQJC6R3Z4KE7TX7A"  # replace with your ThingSpeak Write API Key
rooms = ["Room1", "Room2", "Room3"]  # 3 simulated rooms
# Create CSV file and add header
with open("iot_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "Room", "Temperature", "Humidity"])
while True:
    for room in rooms:
        # Simulate temperature and humidity
        temperature = random.randint(20, 35)
        humidity = random.randint(40, 80)
        
        # Send to ThingSpeak
        url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={temperature}&field2={humidity}"
        requests.get(url)
        
        # Timestamp
        now = datetime.now().strftime("%H:%M:%S")
        
        # Print to terminal
        print(f"{now} | {room} | Temp: {temperature}°C | Humidity: {humidity}%")
        
        # Store in CSV
        with open("iot_data.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([now, room, temperature, humidity])
    
    # Wait 15 seconds before next batch
    time.sleep(15)

