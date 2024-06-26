
from app import app
from flask import Flask, jsonify, render_template, request, url_for


@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'

API_KEY = "S1sr7CjdRJLHTSdbHzA7GyWBGVDLJf-d"

@app.route('/api/restricted/solcastMock/', methods=['GET'])
def solcastMock():
    # Check for API key in the request headers
    api_key = request.headers.get('Authorization')
    if not api_key or api_key != f"Bearer {API_KEY}":
        return jsonify({"error": "Unauthorized"}), 401

    # Extract query parameters
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    hours = request.args.get('hours', '48')
    period = request.args.get('period', 'PT30M')
    output_parameters = request.args.get('output_parameters', 'pv_power_rooftop')
    capacity = request.args.get('capacity')
    azimuth = request.args.get('azimuth')
    tilt = request.args.get('tilt')
    loss_factor = request.args.get('loss_factor', '0.90')
    format = request.args.get('format', 'json')

    for i in [latitude, longitude, capacity, azimuth, tilt]:
        if not i:
            return jsonify({"error": "missing parameters"}), 422

    # Mock response mimicking Solcast API response
    mock_response = {
    "forecasts": [
        {
            "pv_power_rooftop": 19.241,
            "period_end": "2024-06-26T13:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 18.692,
            "period_end": "2024-06-26T14:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 15.597,
            "period_end": "2024-06-26T15:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 10.575,
            "period_end": "2024-06-26T16:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 7.377,
            "period_end": "2024-06-26T17:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 4.24,
            "period_end": "2024-06-26T18:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 1.802,
            "period_end": "2024-06-26T19:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0.537,
            "period_end": "2024-06-26T20:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-26T21:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-26T22:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-26T23:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-27T00:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-27T01:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-27T02:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-27T03:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-27T04:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0.381,
            "period_end": "2024-06-27T05:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 3.561,
            "period_end": "2024-06-27T06:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 5.701,
            "period_end": "2024-06-27T07:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 5.899,
            "period_end": "2024-06-27T08:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 9.217,
            "period_end": "2024-06-27T09:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 13.45,
            "period_end": "2024-06-27T10:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 15.297,
            "period_end": "2024-06-27T11:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 16.589,
            "period_end": "2024-06-27T12:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 17.292,
            "period_end": "2024-06-27T13:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 17.025,
            "period_end": "2024-06-27T14:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 14.823,
            "period_end": "2024-06-27T15:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 12.021,
            "period_end": "2024-06-27T16:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 8.437,
            "period_end": "2024-06-27T17:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 3.721,
            "period_end": "2024-06-27T18:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0.509,
            "period_end": "2024-06-27T19:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0.177,
            "period_end": "2024-06-27T20:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-27T21:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-27T22:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-27T23:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-28T00:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-28T01:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-28T02:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-28T03:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0,
            "period_end": "2024-06-28T04:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 0.811,
            "period_end": "2024-06-28T05:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 5.087,
            "period_end": "2024-06-28T06:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 9.795,
            "period_end": "2024-06-28T07:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 13.472,
            "period_end": "2024-06-28T08:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 16.358,
            "period_end": "2024-06-28T09:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 18.133,
            "period_end": "2024-06-28T10:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 18.552,
            "period_end": "2024-06-28T11:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 18.513,
            "period_end": "2024-06-28T12:00:00.0000000Z",
            "period": "PT1H"
        },
        {
            "pv_power_rooftop": 18.707,
            "period_end": "2024-06-28T13:00:00.0000000Z",
            "period": "PT1H"
        }
    ]
}

    
    return jsonify(mock_response)
