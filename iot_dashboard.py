from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import matplotlib
matplotlib.use('Agg')


app = Flask(__name__)

@app.route("/")
def dashboard():
    # Read CSV file (make sure this exists)
    df = pd.read_csv("iot_data.csv")

    # Group by Room and get last 10 readings
    temp_data = {}
    hum_data = {}
    for room in df['Room'].unique():
        room_data = df[df['Room'] == room].tail(10)
        temp_data[room] = room_data['Temperature'].values
        hum_data[room] = room_data['Humidity'].values

    # Plot Temperature
    plt.figure(figsize=(8,4))
    for room, temps in temp_data.items():
        plt.plot(temps, label=room)
    plt.title("Temperature (Last 10 readings)")
    plt.xlabel("Time Index")
    plt.ylabel("°C")
    plt.legend()
    plt.tight_layout()

    temp_img = io.BytesIO()
    plt.savefig(temp_img, format='png')
    temp_img.seek(0)
    temp_graph = base64.b64encode(temp_img.getvalue()).decode()
    plt.close()

    # Plot Humidity
    plt.figure(figsize=(8,4))
    for room, hums in hum_data.items():
        plt.plot(hums, label=room)
    plt.title("Humidity (Last 10 readings)")
    plt.xlabel("Time Index")
    plt.ylabel("%")
    plt.legend()
    plt.tight_layout()

    hum_img = io.BytesIO()
    plt.savefig(hum_img, format='png')
    hum_img.seek(0)
    hum_graph = base64.b64encode(hum_img.getvalue()).decode()
    plt.close()

    return render_template("dashboard.html", temp_graph=temp_graph, hum_graph=hum_graph)

if __name__ == "__main__":
    app.run(debug=True)
