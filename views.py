
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
            "pv_estimate": 4.657,
            "period_end": "2024-06-25T10:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 5.48,
            "period_end": "2024-06-25T11:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 5.119,
            "period_end": "2024-06-25T11:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 2.203,
            "period_end": "2024-06-25T12:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0.855,
            "period_end": "2024-06-25T12:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0.253,
            "period_end": "2024-06-25T13:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T13:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T14:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T14:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T15:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T15:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T16:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T16:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T17:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T17:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T18:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T18:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T19:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T19:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T20:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T20:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T21:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T21:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T22:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T22:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T23:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-25T23:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T00:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T00:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T01:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0.04,
            "period_end": "2024-06-26T01:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0.973,
            "period_end": "2024-06-26T02:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 2.496,
            "period_end": "2024-06-26T02:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 4.071,
            "period_end": "2024-06-26T03:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 5.675,
            "period_end": "2024-06-26T03:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 7.2,
            "period_end": "2024-06-26T04:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 8.458,
            "period_end": "2024-06-26T04:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 9.484,
            "period_end": "2024-06-26T05:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 9.996,
            "period_end": "2024-06-26T05:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 10.018,
            "period_end": "2024-06-26T06:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 9.869,
            "period_end": "2024-06-26T06:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 9.578,
            "period_end": "2024-06-26T07:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 9.093,
            "period_end": "2024-06-26T07:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 8.424,
            "period_end": "2024-06-26T08:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 7.685,
            "period_end": "2024-06-26T08:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 6.9,
            "period_end": "2024-06-26T09:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 6.282,
            "period_end": "2024-06-26T09:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 5.765,
            "period_end": "2024-06-26T10:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 5.074,
            "period_end": "2024-06-26T10:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 4.241,
            "period_end": "2024-06-26T11:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 3.272,
            "period_end": "2024-06-26T11:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 2.231,
            "period_end": "2024-06-26T12:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 1.126,
            "period_end": "2024-06-26T12:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0.157,
            "period_end": "2024-06-26T13:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T13:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T14:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T14:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T15:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T15:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T16:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T16:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T17:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T17:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T18:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T18:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T19:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T19:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T20:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T20:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T21:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T21:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T22:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T22:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T23:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-26T23:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-27T00:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-27T00:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0,
            "period_end": "2024-06-27T01:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0.024,
            "period_end": "2024-06-27T01:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 0.875,
            "period_end": "2024-06-27T02:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 2.256,
            "period_end": "2024-06-27T02:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 3.608,
            "period_end": "2024-06-27T03:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 4.901,
            "period_end": "2024-06-27T03:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 6.02,
            "period_end": "2024-06-27T04:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 7.175,
            "period_end": "2024-06-27T04:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 8.229,
            "period_end": "2024-06-27T05:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 8.687,
            "period_end": "2024-06-27T05:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 8.6,
            "period_end": "2024-06-27T06:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 8.473,
            "period_end": "2024-06-27T06:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 8.249,
            "period_end": "2024-06-27T07:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 7.865,
            "period_end": "2024-06-27T07:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 7.341,
            "period_end": "2024-06-27T08:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 6.684,
            "period_end": "2024-06-27T08:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 5.922,
            "period_end": "2024-06-27T09:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 5.454,
            "period_end": "2024-06-27T09:30:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 5.199,
            "period_end": "2024-06-27T10:00:00.0000000Z",
            "period": "PT30M"
        },
        {
            "pv_estimate": 4.677,
            "period_end": "2024-06-27T10:30:00.0000000Z",
            "period": "PT30M"
        }
    ]
}
    
    return jsonify(mock_response)
