import pandas
import json
import argparse
from io import StringIO
import tempfile
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import matplotlib.pyplot as plt

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()


csv = pandas.read_csv(file_path, header=None, delimiter=';', encoding='utf-8', skiprows=1)

csvKM = csv[[5]]
csvTime = csv[[0]]

skoki = []
przypadek = [] 
allFrames = []

for i in range(1, 1000):
    if int(csvKM.iloc[i]) != int(csvKM.iloc[i]) - 1:
        for j in range(9):
            temp1 = csv.iloc[i - (10 - j)]
            przypadek.append(temp1)
        for k in range(9):
            temp2 = csv.iloc[i + (k)]
            przypadek.append(temp2)
        allFrames.append(przypadek)
        

# with open('kilometry.json', 'w') as f:
#     json.dump(allFrames, f)

# with open('zera.json', 'w') as f1:
#     json.dump(zeros, f1)

# with open('dziury.txt', 'w') as f2:
#     k = 0
#     for item in dziury:
#         for j in item:
#             f2.write(str(j))
#             if k == 0 or k == 1:
#                 f2.write(' ')
#                 k += 1
#         f2.write("\n")
#         k = 0
    
    


# with open('zera.txt', 'w') as f3:
#     for item in zeros:
#         line = ' '.join(map(str, item))  # Convert elements to strings and join with space
#         f3.write(line + '\n')
