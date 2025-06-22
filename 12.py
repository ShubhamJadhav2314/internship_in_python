import pandas as pd
import numpy as np

# Read a CSV file
# df = pd.read_csv("nba.csv", index_col="Name")

# Working with rows and columns
# emp = {
#     'name': ['John', 'Doe'],
#     'email': ['john@gmail.com', 'doe@gmail.com'],
#     'degree' : ['BCA', 'MCA']
# }
# df = pd.DataFrame(emp)
# print(df)
# print(df[['name', 'degree']])

# Rows
# loc => label based selection
# df1 = df.loc["Jordan Mickey"]
# print(df1)

# df1 = df.loc["Markel Brown"]
# print(df1)

# iloc => indexing based selection
# df1 = df.iloc[3]
# print(df1)

# Check missing values (NaN)
# print(df.isnull())

# Filling missing values
# data = {
#     'score_1': [100,90,56,95],
#     'score_2': [40,80,64,89],
#     'score_3': [np.nan,20,69,93],
# }

# df = pd.DataFrame(data)
# print(df)
# # df.fillna(0, inplace=True)
# # print(df)

# df.dropna(inplace=True)
# print(df)


# Matplotlib
# pip install matplotlib

import matplotlib.pyplot as plt
X = [0,1,2,3,4,5,6,7]
y = [0,1,4,8,16,12,9,15]

fig, ax = plt.subplots()
ax.plot(X, y, marker="o", label="Data Points")
ax.set_title("Example")
ax.set_xlabel("X-Axis")
ax.set_ylabel("y-Axis")

plt.show()

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# df=pd.read_csv("nba.csv")
# # print(df)

# # print(df["Name"])
# df1 = df.loc["Marcus Smart"]
# print(df1)