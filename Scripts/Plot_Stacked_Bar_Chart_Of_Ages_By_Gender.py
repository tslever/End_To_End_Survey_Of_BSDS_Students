import pandas as pd
import matplotlib.pyplot as plt

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_ages = pd.to_numeric(data_frame_of_features.iloc[520][2:])
series_of_genders = data_frame_of_features.iloc[521][2:]
data_frame = pd.DataFrame({
    "Age": series_of_ages,
    "Gender": series_of_genders
})
grouped = data_frame.groupby(["Gender", "Age"]).size().unstack(fill_value = 0)
ax = grouped.plot(kind = "bar", stacked = True, figsize = (10, 7))
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Stacked Bar Chart of Ages by Gender")
plt.legend(title = "Age")
ax.set_xticklabels(ax.get_xticklabels(), rotation = 0)
plt.grid()
plt.show()