#Importing necesary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Create dictionaries to store the data of countries

countries = {
    "Austria": {"r":0.195,"N":14700},
    "Italy": {"r":0.099,"N":216600},
    "Netherlands": {"r":0.114,"N":42580},
    "Switzerland": {"r":0.163,"N":28400},
    "Turkey": {"r":0.144,"N":133700}
}

#Initialize the days of analysis
days = 31

#Initial amount of people infected

#Storing the results in "results"
result = {}

#Iterate through the dictionary