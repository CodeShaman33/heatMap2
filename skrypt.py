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

#usuwam header, ustawiam odczyt csv-ki
csv = pandas.read_csv(file_path, header=None, delimiter=';', encoding='utf-8', skiprows=1)

#przypisuję interesujące mnie kolumny do zmiennych 
csvID = csv[[2]]
csvTime = csv[[0]]


zeros = []

#usuwam "F" z rekordów z flasha
csvID = csvID.apply(lambda x: int(x[2].replace(" F", "")), axis=1)

#pusta tablica dla rekordów
dziury = []
for i in range(1, len(csvID)):
    tempTable = []
    tempZerosTable = []
    
    #jeśli id
    if csvID.iloc[i] - 1 != csvID.iloc[i - 1]:
        
        framesNum = abs(int(csvID.iloc[i] - csvID.iloc[i - 1]))
        # print(framesNum)
        

            
        
        tempString = str(csvTime.iloc[i])
        
        for i in range(len(tempString)):
            
            # print(tempString[i], i)
        
            subString = tempString[5:24]
            
        tempTable.append(int(csvID.iloc[i]))
        tempTable.append(subString)
        tempTable.append('framesNumber:')
        tempTable.append(framesNum)
        dziury.append(tempTable)
        
        if framesNum == 0:
            tempZerosTable.append(int(csvID.iloc[i]))
            tempZerosTable.append(subString)
            zeros.append(tempZerosTable)
        
print(zeros)




with open('dziury.json', 'w') as f:
    json.dump(dziury, f)

with open('zera.json', 'w') as f1:
    json.dump(zeros, f1)

with open('dziury.txt', 'w') as f2:
    k = 0
    for item in dziury:
        for j in item:
            f2.write(str(j))
            if k == 0 or k == 1:
                f2.write(' ')
                k += 1
        f2.write("\n")
        k = 0
    
    


with open('zera.txt', 'w') as f3:
    for item in zeros:
        line = ' '.join(map(str, item))  # Convert elements to strings and join with space
        f3.write(line + '\n')
