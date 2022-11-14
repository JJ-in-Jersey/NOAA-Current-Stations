import os
from pathlib import Path
from objects import Waypoint
import requests
from bs4 import BeautifulSoup as bs

if __name__ == '__main__':

    stationsURL = 'https://tidesandcurrents.noaa.gov/noaacurrents/Stations?g=444'
    noaaWaypoints = Path(str(os.environ['USERPROFILE']) + '/Documents/GPX/noaaCurrentStationWaypoints/')
    os.makedirs(noaaWaypoints, exist_ok=True)

    tree = bs(requests.get(stationsURL).text, 'html.parser')

    for tag in tree.find_all('a'):
        if 'Predictions?' in str(tag.get('href')):
            wp = Waypoint(tag)
            wp.writeMe(noaaWaypoints)