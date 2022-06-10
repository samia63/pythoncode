"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display the number of confirmed cases per country/region using a pie chart
- Display the top 5 countries for deaths using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country or countries.

Each function should visualise the data using Matplotlib.
"""

# TODO: Your code here
from matplotlib import pyplot as plt
import numpy as np

country = ['Mainland China','Philippines','India','Sweden','Kiribati']
 
data = [22,1,1,0,1]
 
# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = country)
 
# show plot
plt.show()



import pandas as pd
from matplotlib import pyplot as plt
 
# Read CSV into pandas
data = pd.read_csv('C:/covid_19_data.csv')
df = pd.DataFrame(data)
 
name = df['Country/Region']
price = df['Deaths']
 
# Figure Size
fig = plt.figure(figsize =(10, 7))
 
# Horizontal Bar Plot
plt.bar(name[10:20], price[10:20])
 
# Show Plot
plt.show()



from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, writers
import numpy as np
  
fig = plt.figure(figsize = (6,4))
axes = fig.add_subplot(1,1,1)
axes.set_ylim(0, 300)
palette = ['blue', 'red', 'green', 
           'darkorange', 'maroon', 'black']
  
y1, y2, y3, y4, y5 = [], [], [], [], []
  
def animation_function(i):
    y1 = i
    y2 = 5 * i
    y3 = 3 * i
    y4 = 2 * i
    y5 = 6 * i
  
    plt.xlabel("Country/Region")
    plt.ylabel("Deaths")
      
    plt.bar(["Mainland China", "China", "India", 
             "Sweden", "Kiribati"],
            [y1, y2, y3, y4, y5],
            color = palette)
    plt.title("Bar Chart Animation")
    animation = FuncAnimation(fig, animation_function, interval = 50)
    plt.show()


