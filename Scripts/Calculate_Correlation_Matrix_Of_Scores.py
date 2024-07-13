import pandas as pd

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_scores_in_row_0 = pd.to_numeric(data_frame_of_features.iloc[0][2:])
series_of_scores_in_row_1 = pd.to_numeric(data_frame_of_features.iloc[1][2:])
series_of_scores_in_row_2 = pd.to_numeric(data_frame_of_features.iloc[2][2:])
scores_df = pd.DataFrame({
    "Row 0": series_of_scores_in_row_0,
    "Row 1": series_of_scores_in_row_1,
    "Row 2": series_of_scores_in_row_2
})
correlation_matrix = scores_df.corr()
print(correlation_matrix)