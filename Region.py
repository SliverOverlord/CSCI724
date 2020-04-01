"""
Author: Joshua DeNio
Date: 04/01/2020

Description:
    This class builds a region object.
    Conditions:
    This class accepts a region name.
"""

import random

class Region:
    #string: (each region will have a name)
    name = ""
    #int ID: (each region will have an id)
    id = -1

    # list of adjoining_regions (by id)
    adjoining_regions = []
    #int elevation: (in meters)
    elevation = -1

    # int x_value;
    x_value = -1
    # int y_value;
    y_value = -1

    #string wind_direction;(N,E,W,S)
    #double Temp; (the temperature)
    temp = -1

    # double rainfall (in cm per hour)
    rainfall = 0
    #double drainage (in cm per hour)
    drainage = random.randINT(0,50)

##    bool fire;
##    bool thunderstorm;
##    bool blizzard;
##    bool snowfall;
##    bool snow_cover;
##    bool flooding;

    #Constructor takes a name and an id
    def __init__(self, name, id):
        self.name = name
        self.id = id

##make getters and setters for all attributes

## Make a toString method