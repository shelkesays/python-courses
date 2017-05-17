#! /usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt
%pylab inline

data = pd.read_csv("hubble_data.csv")
data.head()

headers = ["dist","rec_vel"]

data_no_headers = pd.read_csv("hubble_data_no_headers.csv", names = headers)

data_no_headers.head()

data_no_headers["dist"]

data.set_index("distance", inplace= True)
data.head()

data.plot()
plt.show()
