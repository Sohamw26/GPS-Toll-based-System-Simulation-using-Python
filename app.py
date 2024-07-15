from flask import Flask, render_template, request, jsonify
from geopy.distance import geodesic
import random

app = Flask(__name__)

# Define toll rates and distances between cities
toll_rates = {
    ('Mumbai', 'Bangalore'): 1.5,
    ('Mumbai', 'Pune'): 1.5,
    ('Mumbai', 'Chennai'): 1.5,
    ('Chennai', 'Pune'): 1.5,
    ('Pune', 'Bangalore'): 1.5
}

# Coordinates for cities
city_coords = {
    'Mumbai': (19.0760, 72.8777),
    'Pune': (18.5204, 73.8567),
    'Bangalore': (12.9716, 77.5946),
    'Chennai': (13.0827, 80.2707)
}

# Toll booth locations
toll_booths_data = {
    ('Mumbai', 'Bangalore'): [
        {'name': 'Toll Booth A', 'location': [16.5, 75.0]},
        {'name': 'Toll Booth B', 'location': [14.5, 76.0]},
        {'name': 'Toll Booth C', 'location': [15.5, 75.5]}
    ],
    ('Mumbai', 'Pune'): [
        {'name': 'Toll Booth D', 'location': [18.75, 73.5]},
        {'name': 'Toll Booth E', 'location': [18.6, 73.75]},
        {'name': 'Toll Booth F', 'location': [18.65, 73.6]}
    ],
    ('Mumbai', 'Chennai'): [
        {'name': 'Toll Booth G', 'location': [17.0, 75.0]},
        {'name': 'Toll Booth H', 'location': [14.0, 78.0]},
        {'name': 'Toll Booth I', 'location': [16.0, 76.5]}
    ],
    ('Chennai', 'Pune'): [
        {'name': 'Toll Booth J', 'location': [15.0, 77.0]},
        {'name': 'Toll Booth K', 'location': [17.0, 75.0]},
        {'name': 'Toll Booth L', 'location': [16.5, 76.0]}
    ],
    ('Pune', 'Bangalore'): [
        {'name': 'Toll Booth M', 'location': [16.0, 75.0]},
        {'name': 'Toll Booth N', 'location': [14.5, 77.0]},
        {'name': 'Toll Booth O', 'location': [15.5, 76.0]}
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/calculate_toll', methods=['POST'])
def calculate_toll():
    data = request.get_json()
    source = data['source']
    destination = data['destination']
    
    if (source, destination) in toll_rates:
        source_coords = city_coords[source]
        destination_coords = city_coords[destination]
        distance_km = geodesic(source_coords, destination_coords).kilometers
        rate_per_km = toll_rates[(source, destination)]
        toll = distance_km * rate_per_km
        return jsonify({"toll": round(toll, 2), "distance": round(distance_km, 2)})
    else:
        return jsonify({"error": "Route not found"})

@app.route('/get_toll_booths', methods=['POST'])
def get_toll_booths():
    data = request.get_json()
    source = data['source']
    destination = data['destination']
    
    if (source, destination) in toll_booths_data:
        toll_booths = toll_booths_data[(source, destination)]
        return jsonify({"toll_booths": toll_booths})
    else:
        return jsonify({"error": "Route not found"})

@app.route('/simulate_speed', methods=['POST'])
def simulate_speed():
    speeds = [random.randint(60, 100) for _ in range(10)]  # Simulate 10 speed readings
    points = sum(1 for speed in speeds if speed <= 80)
    average_speed = sum(speeds) / len(speeds)
    return jsonify({'speeds': speeds, 'points': points, 'average_speed': round(average_speed, 2)})

if __name__ == '__main__':
    app.run(debug=True)
