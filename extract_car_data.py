#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:36:48 2019

@author: mihirkhambete
"""
import json

"""
Parses car trace json file to get fuel, latitude, longitude, odometer
"""
def get_car_data():
    fuel_data = [] # list of fuel_level (floats)
    latitude_data = [] # list of latitudes (floats)
    longitude_data = [] # list of longitudes (floats)
    odometer_data = [] #list of odometer values (floats)
    
    with open('downtown-crosstown.json') as f:
        for line in f:
            data = json.loads(line)
            
            if data["name"] == "fuel_level":
                current_fuel = data["value"]
                fuel_data.append(current_fuel)
            elif data["name"] == "latitude":
                current_latitude = data["value"]
                latitude_data.append(current_latitude)
            elif data["name"] == "longitude":
                current_longitude = data["value"]
                longitude_data.append(current_longitude)
            elif data["name"] == "odometer":
                current_odometer = data["value"]
                odometer_data.append(current_odometer)
            else:
                continue
    return (fuel_data, latitude_data, longitude_data, odometer_data)

