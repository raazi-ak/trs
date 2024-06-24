
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

    if not latitude or longitude or hours or period or capacity or azimuth or tilt:
        return jsonify({"error": "missing parameters"}), 422

    # Mock response mimicking Solcast API response
    mock_response = {
        "forecasts": [
            {
                "pv_estimate": 2.652,
                "period_end": "2024-06-24T08:30:00.0000000Z",
                "period": "PT30M"
            },
            {
                "pv_estimate": 2.962,
                "period_end": "2024-06-24T09:00:00.0000000Z",
                "period": "PT30M"
            },
            {
                "pv_estimate": 3.217,
                "period_end": "2024-06-24T09:38:00.0000000Z",
                "period": "PT30M"
            },
            {
                "pv_estimate": 3.416,
                "period_end": "2024-06-24T10:00:00.00000eez",
                "period": "PT30M"
            }
        ]
    }
    
    return jsonify(mock_response)
