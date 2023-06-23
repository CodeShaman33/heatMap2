import pandas
import json
import argparse
from io import StringIO
import tempfile
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor


def extractAll(csvFile):
    csvDate = csvFile[[0]]
    csvActivity = csvFile[[1]]
    csvID = csvFile[[2]]
    csvBasics = csvFile[[3]]
    csvKM = csvFile[[4]]
    csvOutput = csvFile[[5]]
    csvRPM = csvFile[[6]]
    csvVelocity = csvFile[[7]]
    csvFuel = csvFile[[8]]
    csvFuelCan = csvFile[[9]]

    return {
        'csvDate' : csvDate,
        'csvActivity' : csvActivity,
        'csvID' : csvID,
        'csvBasics' : csvBasics,
        'csvKM' : csvKM,
        'csvOutput' : csvOutput,
        'csvRPM' : csvRPM,
        'csvVelocity' : csvVelocity,
        'csvFuel' : csvFuel,
        'csvFuelCan' : csvFuelCan
    }
    
def pointsGenerator(xMin, xMax):
    points = []
    for i in range(1, xMax):
        points.append(i)
    
    return points


def generateData(inputs, xMin, xMax):
    tempData = []
    for item in inputs:
        tempTable = []
        tempTable.append(item[xMin:xMax])
        tempData.append(tempTable)
        
    return tempData

def modifyID(data):
    data = data.apply(lambda x: int(x[2].replace(" F", "")) if pandas.notnull(x[2]) else 0, axis=1)
    return data
