import pandas as pd

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_genders = data_frame_of_features.iloc[521][2:]
series_of_counts = series_of_genders.value_counts().sort_index()
total_count = series_of_counts.sum()
series_of_proportions = series_of_counts / total_count
print(series_of_proportions)