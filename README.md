# GPS-Toll-based-System-Simulation-using-Python

Sure, here are the concise instructions for your README file:



GPS Toll Simulation

Introduction

The GPS Toll Simulation application calculates toll fees, displays toll booth locations on a map, and simulates a speed reward system to encourage safe driving.

Prerequisites

- Python 3.x
- pip (Python package installer)

Installation

1. Clone the Repository

 
   clone the repo using the link
   cd gps-toll-simulation
  

2. Create a Virtual Environment

   
   python -m venv venv
   source venv\Scripts\activate
 

3. Install Dependencies

  
   pip install -r requirements.txt
  

4. Running the Application

1. Start the Flask Server

   
   python app.py
   

2. Access the Application

   Open your web browser and go to:

   
   http://127.0.0.1:5000/
   

Usage

- Calculate Toll Fees:** Select source and destination, then click "Get Toll".
- View Toll Booth Locations:** Select source and destination, then click "Get Toll Booths".
- Simulate Speed and Earn Rewards:** Click "Simulate Speed".

Files and Directories

- app.py:** Main Flask application file.
- templates/index.html:** Main HTML file for the user interface.
- static/css/styles.css:** CSS file for styling the application.
- static/js/scripts.js:** JavaScript file for frontend logic.
