let map;
let carMarker;

document.addEventListener('DOMContentLoaded', () => {
    map = L.map('map').setView([19.0760, 72.8777], 8);  // Center on Mumbai with zoom level 8
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(map);
    console.log("Map initialized");
});

function calculateToll() {
    const source = document.getElementById('source').value;
    const destination = document.getElementById('destination').value;
    fetch('/calculate_toll', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ source, destination }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            document.getElementById('toll_result').innerText = `Error: ${data.error}`;
            document.getElementById('distance_result').innerText = '';
        } else {
            document.getElementById('toll_result').innerText = `Estimated Toll: ₹${data.toll}`;
            document.getElementById('distance_result').innerText = `Distance: ${data.distance} km`;
        }
    });
}

function getTollBooths() {
    const source = document.getElementById('source').value;
    const destination = document.getElementById('destination').value;
    fetch('/get_toll_booths', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ source, destination }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error('Error fetching toll booths:', data.error);
            return;
        }
        
        const tollBooths = data.toll_booths;
        console.log("Toll booths data:", tollBooths);
        tollBooths.forEach(booth => {
            L.marker(booth.location).addTo(map)
              .bindPopup(booth.name).openPopup();
        });

        // Start the animation after toll booths are added
        const startLatLng = cityCoords[source];
        const endLatLng = cityCoords[destination];
        animateCar(startLatLng, endLatLng);
    });
}

const cityCoords = {
    'Mumbai': [19.0760, 72.8777],
    'Pune': [18.5204, 73.8567],
    'Bangalore': [12.9716, 77.5946],
    'Chennai': [13.0827, 80.2707]
};

function animateCar(startLatLng, endLatLng) {
    if (carMarker) {
        map.removeLayer(carMarker);
    }

    carMarker = L.marker(startLatLng, {icon: L.icon({iconUrl: 'static/car_icon.png', iconSize: [32, 32]})}).addTo(map);
    let progress = 0;
    const steps = 100;
    const interval = setInterval(() => {
        if (progress >= 1) {
            clearInterval(interval);
        } else {
            const lat = startLatLng[0] + progress * (endLatLng[0] - startLatLng[0]);
            const lng = startLatLng[1] + progress * (endLatLng[1] - startLatLng[1]);
            carMarker.setLatLng([lat, lng]);
            progress += 1 / steps;
        }
    }, 100);
}

function simulateSpeed() {
    fetch('/simulate_speed', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        const speedDetails = `Speeds: ${data.speeds.join(', ')} km/h\nAverage Speed: ${data.average_speed} km/h`;
        document.getElementById('speed_result').innerText = speedDetails;
        document.getElementById('reward_result').innerText = `Reward Points: ${data.points}`;
    });
}
