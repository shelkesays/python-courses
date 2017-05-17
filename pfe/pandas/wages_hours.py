#! /usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
#%pylab inline

data = pd.read_csv("wages_hours.csv")
data.head()


data = pd.read_csv("wages_hours.csv", sep = "\t")
data.head()


data2 = data[["AGE", "RATE"]]
data2.head()

data_sorted = data2.sort_values(["AGE"])
data_sorted.head()

data_sorted.set_index("AGE", inplace=True)
data_sorted.head()

data_sorted.plot()
plt.show()
