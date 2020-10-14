"""
I guess that's the only file that will ever be here haha
"""
from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)


@api.route('/satellite')
class Satellite(Resource):
    def get(self):
        return {'connected': True}


@api.route('/satellite/battery')
class SatelliteBattery(Resource):
    def get(self):
        return {'percentage': 69}


@api.route('/satellite/cpu/temperature')
class SatelliteCpuTemperature(Resource):
    def get(self):
        return {'celsius': 47}


@api.route('/satellite/lora/signal')
class SatelliteLoraSignal(Resource):
    def get(self):
        return {'rssi': -81}


@api.route('/satellite/location')
class SatelliteLocation(Resource):
    def get(self):
        return {'latitude': 49.88345, 'longitude': 19.49253, 'height': 2137}


if __name__ == '__main__':
    app.run()
