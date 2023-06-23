import pandas
import json
import argparse
from io import StringIO
import tempfile
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import matplotlib.pyplot as plt
from math import isnan

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()


csv = pandas.read_csv(file_path, header=None, delimiter=';', encoding='utf-8', skiprows=1)

csvInput = csv[[3]]
csvInput = csvInput[:205]
csvTime = csv[[0]]

csvKm = csv[[5]]

# for i in range(1, len(csvInput)):
#     currentValue = csvInput.iloc[i].values[0]
    
#     if str(csvInput.iloc[i].values[0]) == 'nan':
#         print('true', currentValue)
    
#     else: 




def checkIfActive(x1, x2):
    activeFrames = 0
    inactiveFrames = 0
    
    for j in range(x1, x2):
        if '1' in str(csvInput.iloc[j].values[0]):
            activeFrames += 1
        else:
            inactiveFrames += 1
            
    print('active: ', activeFrames, ' inactive: ', inactiveFrames)
    
    return [activeFrames, inactiveFrames, (activeFrames + inactiveFrames)]

checkIfActive(1, 100)

def usage(x1, x2):
    
    return int(csvKm.iloc[x1].values[0]) - int(csvKm.iloc[x2].values[0])
    
    
    
def checkIt(x1, x2):
    results = checkIfActive(x1, x2)
    wasActive = (float(results[0])/float(results[2]))*100
    print('ACTIVITY METER: ', wasActive)
    
checkIt(1, 100)