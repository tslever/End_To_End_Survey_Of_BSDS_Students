import matplotlib.pyplot as plt
import pandas as pd

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_genders = data_frame_of_features.iloc[521][2:]
series_of_counts_of_genders = series_of_genders.value_counts().sort_index()
plt.bar(series_of_counts_of_genders.index, series_of_counts_of_genders.values, edgecolor = "black")
plt.title("Bar Chart of Numbers of Students with Genders")
plt.xlabel("Gender")
plt.ylabel("Frequency")
plt.xticks(series_of_counts_of_genders.index)
plt.grid()
plt.show()