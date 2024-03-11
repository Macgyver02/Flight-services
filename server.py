# server.py
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Mock data for flights
flights = [
    {
        'id': 1,
        'origin': 'New York',
        'destination': 'London',
        'departure': '2023-06-01T10:00:00',
        'arrival': '2023-06-01T18:00:00'
    },
    {
        'id': 2,
        'origin': 'Los Angeles',
        'destination': 'Tokyo',
        'departure': '2023-06-15T12:00:00',
        'arrival': '2023-06-16T16:00:00'
    }
]

# API endpoint to get available flights
@app.route('/flights', methods=['GET'])
def get_flights():
    return jsonify(flights)

# API endpoint for booking a flight
@app.route('/book', methods=['POST'])
def book_flight():
    data = request.get_json()
    flight_id = data.get('flightId')
    # Perform booking logic here
    return jsonify({'message': 'Flight booked successfully'})

if __name__ == '__main__':
    app.run(debug=True)