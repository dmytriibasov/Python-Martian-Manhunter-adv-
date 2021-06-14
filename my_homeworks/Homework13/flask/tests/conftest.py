import os
import tempfile

import pytest
from flask import Flask
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


class ApiMock:
    def __init__(self, *args, **kwargs):
        self.api_data = {'message': 'accurate', 'cod': '200', 'count': 1,
                         'list': [{'id': 2267057, 'name': 'Lisbon',
                                   'coord': {'lat': 38.7167, 'lon': -9.1333},
                                   'main': {'temp': 17.22, 'feels_like': 17.45,
                                            'temp_min': 16.67, 'temp_max': 17.78,
                                            'pressure': 1018, 'humidity': 94},
                                   'dt': 1623651008,
                                   'wind': {'speed': 3.6, 'deg': 320},
                                   'sys': {'country': 'PT'},
                                   'rain': None,
                                   'snow': None,
                                   'clouds': {'all': 20},
                                   'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]}]}
        self.status_code = 200

    def json(self):
        return self.api_data
