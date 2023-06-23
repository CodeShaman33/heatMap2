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
#external funcitons 
from script4Functions import pointsGenerator, extractAll, generateData, modifyID

root = tk.Tk()
root.withdraw()

#setting up parameters 
xMin = 1
xMax = 10
zakres = [xMin, xMax]

#opening up the file 
file_path = filedialog.askopenfilename()
csv = pandas.read_csv(file_path, header=None, delimiter=';', encoding='utf-8', skiprows=1)

#generating points for figures that does not include data for x 
points = pointsGenerator(xMin, xMax)

#extracting interesting data in dictionary 
data = extractAll(csv)

#      [],xMin,xMax
figureData = generateData([data['csvID'], data['csvDate']],xMin,xMax)

# modify ID number so that i wont have 'F'
print(figureData[0])

