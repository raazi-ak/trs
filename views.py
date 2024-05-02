
from app import app
from flask import Flask, jsonify, render_template, request, url_for


@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'

