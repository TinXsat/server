"""
I guess that's the only file that will ever be here haha
"""
from flask import Flask
from flask_restplus import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)


class Satellite:
    """
    This is a class containing all data about the satellite

    Use instance of this when serving http responses
    """

    def __init__(self):
        self.is_connected: bool = False
        self.battery_percentage: int = None
        self.cpu_temperature: float = None
        self.lora_signal_rssi: int = None
        self.location_lat: float = None
        self.location_lng: float = None
        self.location_height: float = None


sat = Satellite()


@api.route('/satellite')
class Satellite(Resource):
    def get(self):
        return {'connected': sat.is_connected}


@api.route('/satellite/battery')
class SatelliteBattery(Resource):
    def get(self):
        return {'percentage': sat.battery_percentage}


@api.route('/satellite/cpu/temperature')
class SatelliteCpuTemperature(Resource):
    def get(self):
        return {'celsius': sat.cpu_temperature}


@api.route('/satellite/lora/signal')
class SatelliteLoraSignal(Resource):
    def get(self):
        return {'rssi': sat.lora_signal_rssi}


@api.route('/satellite/location')
class SatelliteLocation(Resource):
    def get(self):
        return {'latitude': sat.location_lat, 'longitude': sat.location_lng, 'height': sat.location_height}


if __name__ == '__main__':
    app.run()
