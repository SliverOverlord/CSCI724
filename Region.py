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
    name = "*"
    #int ID: (each region will have an id)
    id = -1

    # list of adjoining_regions (by id)
    adjoining_regions = []
    #int elevation: (in meters)
    elevation = -1

    # Road
    road = false

    # River
    river = false

    # int x_value;
    x_value = -1
    # int y_value;
    y_value = -1

    #string wind_direction;(N,E,W,S)
    wind_direction = "*"
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

    #List of hazard warnings for this region
    warnings = []

    #Constructor takes a name and an id
    def __init__(self, name, id):
        self.name = name
        self.id = id

##make getters and setters for all attributes
def get_warnings(self):
    return self.warnings

def set_elevation(self,new_elevation):
    self.elevation = new_elevation

def get_elevatio(self):
    return self.elevation

## Make a toString method
"""
Description:
String function returns a string.
"""
def __str__(self):

    hazard_warings = get_warnings
    if hazard_warings.length() > 0:
        tmp = ""
        tmp += "\n"
        tmp += "Warnings for region" + self.get_name + "\n"
        tmp += "{"
        for item in self.get_warnings():
            tmp += str(item)+" "
        tmp += "}" + "\n"
        

        return tmp
