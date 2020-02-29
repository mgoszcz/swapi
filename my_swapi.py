import requests


class SWApi:
    """
    SWAPI handling
    """
    def __init__(self):
        self.planets = list()
        self.initialize_planets()


    def initialize_planets(self):
        planets = requests.get('http://swapi.co/api/planets')
        for i in range(1, planets.json()['count'] + 1):
            planet = requests.get('http://swapi.co/api/planets/{}'.format(i))
            self.planets.append(planet)
