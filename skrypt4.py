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

root = tk.Tk()
root.withdraw()

# ZAKRES ZAKRES ZAKRES ZAKRES ZAKRES ZAKRES ZAKRES 
xMin = 1
xMax = 26182
zakres = [xMin, xMax]

# generowanie punktów do wykresu 
points = []
for i in range(1, xMax):
    points.append(i)
    

#otwieranie pliku, okno wyboru 
file_path = filedialog.askopenfilename()
csv = pandas.read_csv(file_path, header=None, delimiter=';', encoding='utf-8', skiprows=1)



csvKM = csv[[5]]
csvTime = csv[[0]]
csvFuel = csv[[10]]
csvId = csv[[2]]
csvDate = csv[[0]]
csvActivity = csv[[1]]
csvTemp1 = csv[[20]]

# MATPLOTLIB DATA 
data = csvId[zakres[0]:zakres[1]]      
values = csvKM[zakres[0]:zakres[1]]       
dateValues = csvDate[zakres[0]:zakres[1]]
temp = csvTemp1[zakres[0]:zakres[1]]
newTable = []
newTable2 = []
newTable3 = []

print(csvActivity.values[0])

data = data.apply(lambda x: int(x[2].replace(" F", "")) if pandas.notnull(x[2]) else 0, axis=1)

for i in range(len(data)):
    newTable.append(data.iloc[i])
    
for i in range(len(values)):
    newTable2.append(values.iloc[i])
    
for i in range(len(dateValues)):
    newTable3.append(dateValues.iloc[i].values[0])
    
    
colors = ['green' if value < 22 else 'orange' for value in newTable]

    
fig, ax = plt.subplots()
ax.plot(points, newTable)

# plt.ylim(min(values), max(values))

plt.axis('auto')

# plt.xlabel('Data')
plt.ylabel('Wartość')
plt.title('Wykres wartości w czasie')

cursor = Cursor(ax, useblit=True, color='red', linewidth=1)

coord_text = plt.annotate('', xy=(0.02, 0.95), xycoords='axes fraction', fontsize=10)


def on_move(event):
    if not event.inaxes:
        return
    x, y = event.xdata, event.ydata
    coord_text.set_text(f'x = {x:.2f}, y = {y:.2f}')
    fig.canvas.draw_idle()


    # print(f'x = {x}, y = {y}')

fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()


# Dodawanie obszaru powiększenia (zoom)
axins = ax.inset_axes([0.3, 0.6, 0.4, 0.3])
axins.plot(newTable, newTable2)
ax.indicate_inset_zoom(axins)

# Dodawanie przycisków do przybliżania i oddalania
axzoom = plt.axes([0.8, 0.9, 0.1, 0.04])
axzoomin = plt.axes([0.7, 0.9, 0.1, 0.04])
axzoomout = plt.axes([0.6, 0.9, 0.1, 0.04])

button_zoom = plt.Button(axzoom, 'Zoom')
button_zoomin = plt.Button(axzoomin, 'Zoom In')
button_zoomout = plt.Button(axzoomout, 'Zoom Out')

def zoom(event):
    axins.set_xlim(event.xdata - 500, event.xdata + 500)