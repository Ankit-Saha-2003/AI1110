# CBSE Statistics Grade 9
# Exercise 14.1.1

# Name: Ankit Saha
# Roll number: AI21BTECH11004

""" Problem Statement
Give five examples of data that you can collect from your day-to-day life
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Figure 1
df = pd.read_excel(r'data.xlsx', 'Sheet1')
data = np.array(df)
fig, ax = plt.subplots()
ax.bar(data[0], data[1])
plt.title('Figure 1')
plt.xlabel('Department')
plt.ylabel('Number of Students')
plt.savefig('../figs/fig-1')
plt.show()


# Figure 2
df = pd.read_excel(r'data.xlsx', 'Sheet2')
data = np.array(df)
fig, ax = plt.subplots()
ax.bar(data[0], data[1])
plt.title('Figure 2')
plt.xlabel('Date (April)')
plt.ylabel('Temperature (in C)')
plt.savefig('../figs/fig-2')
plt.show()

# Figure 3
df = pd.read_excel(r'data.xlsx', 'Sheet3')
data = np.array(df)
fig, ax = plt.subplots()
ax.bar(data[0], data[1])
plt.title('Figure 3')
plt.xlabel('Month')
plt.ylabel('Rainfall (in mm)')
plt.savefig('../figs/fig-3')
plt.show()

# Figure 4
df = pd.read_excel(r'data.xlsx', 'Sheet4')
data = np.array(df)
fig, ax = plt.subplots()
ax.bar(data[0], data[1])
plt.title('Figure 4')
plt.xlabel('Program')
plt.ylabel('Number of Students')
plt.savefig('../figs/fig-4')
plt.show()

# Figure 5
df = pd.read_excel(r'data.xlsx', 'Sheet5')
data = np.array(df)
fig, ax = plt.subplots()
ax.bar(data[0], data[1])
plt.title('Figure 5')
plt.xlabel('Medal')
plt.ylabel('Number of Medals')
plt.savefig('../figs/fig-5')
plt.show()
