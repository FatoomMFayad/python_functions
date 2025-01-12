#5.	Write a Python program to read the JSON data from the link: https://gbfs.citibikenyc.com/gbfs/en/station_information.json , retrieve only the capacities of all stations and store them in a list.
from zoneinfo import reset_tzpath

import requests
def reading_json(url):
    response = requests.get(url)
    result = response.json()['data']
    capacities = []
    for station in result['stations']:
        capacities.append(station['capacity'])

    return capacities

url = "https://gbfs.citibikenyc.com/gbfs/en/station_information.json"
print(f"Stations capacities : {reading_json(url)}")