import matplotlib.pyplot as plt 		
import csv
import numpy as np
import pandas as pd

#TODO FIND A WAY TO ELIMINATE THE OVERLAP 
x = []
y = []

with open('C:/Users/wosker4yan/Desktop/Work and Study/sendtex/Python_tutorials/matplotlib_habits_visualization/workouts.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        y.append(str(row[1]))
plt.plot(x,y, label='workouts')
#TODO CHANGE THE SIZES of values on x and y scale
ax = plt.gca()
plt.axis([0,100,0,100])
plt.xticks(rotation = 90)
for label in ax.get_xaxis().get_ticklabels()[::2]:
    label.set_visible(False)
for label in ax.get_yaxis().get_ticklabels()[::2]:
    label.set_visible(False)




plt.plot()
plt.title('')
plt.legend()
plt.show()

