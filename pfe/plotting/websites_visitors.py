import pandas as pd
import matplotlib.pyplot as plt
%pylab inline

headers = ["date", "visitors"]
data = pd.read_csv("visitors.csv", skiprows=4, names=headers)
data.head()

headers = ["date", "visitors_new"]
data_new = pd.read_csv("visitors-new.csv", skiprows=4, names=headers)
data_new.heade()

data_combined = pd.merge(data, data_new)
data_combined.head()

data_combined.sort_values(["date"], inplace=True)

data_combined.set_index("date", inplace=True)
data_combined.head()

data_combined.plot()
plt.show()

data = pd.read_csv("operating-systems.csv")
data.head()

data.columns

data["Value"]

data["Item"]

data.rename(columns = {'Item' : "Operating System"}, inplace=True)
data.head()

os_new = data[["Operating System", "Value Percent"]]

os_new.set_index("Operating System", inplace=True)
os_new.head()

explode = (0.1, 0, 0, 0, 0)
colors_mine = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'lightcyan']
os_new[:5].plot(kind="pie", y="Value Percent",autopct='%.2f%%', shadow=True,
                explode=explode, legend = False, colors = colors_mine)
