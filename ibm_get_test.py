#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:52:17 2019

@author: mihirkhambete
"""
import requests

def get_ibm_weather_at(latitude, longitude):
    """
    Get the weather at a specific geographical coordinate
    """
    #build the coordinate-specific url
    url_beginning = 'https://b3ee9e0e-83ab-4f79-bc9b-df412f1a8052:8CvJAp46TI@twcservice.mybluemix.net/api/weather/v1/geocode/'
    url_bridge = '/'
    url_end = '/observations.json?language=en-US'
    location_url = url_beginning + str(latitude) + url_bridge + str(longitude) + url_end
    
    
    #get the location's ibm weather as a json object
    r = requests.get(url = location_url, params = {}) 
    data = r.json()
    return data
   