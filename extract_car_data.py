#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:36:48 2019

@author: mihirkhambete
"""
import json
#import requests
#trying to push
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
            post_data = {}
            if data["name"] == "fuel_level":
                current_fuel = data["value"]
                fuel_data.append(current_fuel)
                post_data["fuel_level"] = current_fuel
                
                
            elif data["name"] == "latitude":
                current_latitude = data["value"]
                latitude_data.append(current_latitude)
                post_data_type = "latitude"
                post_data["curren"] = current_latitude
                
            elif data["name"] == "longitude":
                current_longitude = data["value"]
                longitude_data.append(current_longitude)
                post_data_type = "longitude"
                post_data_value = current_longitude
            elif data["name"] == "odometer":
                current_odometer = data["value"]
                odometer_data.append(current_odometer)
                post_data_type = "odometer"
                post_data_value = current_odometer
            else:
                continue
            
            #POST to suzie's URL
    return (fuel_data, latitude_data, longitude_data, odometer_data)

