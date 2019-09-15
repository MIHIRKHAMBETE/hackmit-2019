#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:36:48 2019

@author: mihirkhambete
"""
import json
import time
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
        first_line = f.readline()
        first_line_data = json.loads(first_line)
        
        #timestamp of first data point in the json file
        json_start_time = first_line_data["timestamp"] 
        
        # time the function was called
        execution_start_time = time.time() 
        for line in f:
            data = json.loads(line)
            line_relative_time = data["timestamp"] - json_start_time
            
            post_data = {}
            if data["name"] == "fuel_level":
                current_fuel = data["value"]
                fuel_data.append(current_fuel)
                post_data["fuel_level"] = line_relative_time, current_fuel
                
                
            elif data["name"] == "latitude":
                current_latitude = data["value"]
                latitude_data.append(current_latitude)
                post_data["latitude"] = line_relative_time, current_latitude
                
            elif data["name"] == "longitude":
                current_longitude = data["value"]
                longitude_data.append(current_longitude)
                post_data["longitude"] = line_relative_time, current_longitude
                
            elif data["name"] == "odometer":
                current_odometer = data["value"]
                odometer_data.append(current_odometer)
                post_data["odometer"] =line_relative_time, current_odometer
                
            else:
                continue
            # post data in "real time"
            while(time.time() - execution_start_time > line_relative_time):
                # wait until the time the data is supposed to be sent
                time.sleep(0.0001)
            #POST to suzie's URL
    return (fuel_data, latitude_data, longitude_data, odometer_data)

