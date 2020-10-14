"""
I guess that's the only file that will ever be here haha
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_there():
    return 'Hello from TinX server!'


@app.route('/satellite')
def satellite():
    return {'connected': True}


@app.route('/satellite/battery')
def satellite_battery():
    return {'percentage': 69}


@app.route('/satellite/cpu/temperature')
def satellite_cpu_temperature():
    return {'celsius': 47}


@app.route('/satellite/lora/signal')
def satellite_lora_signal():
    return {'rssi': -81}


@app.route('/satellite/location')
def satellite_location():
    return {'latitude': 49.88345, 'longitude': 19.49253, 'height': 2137}


if __name__ == '__main__':
    app.run()
