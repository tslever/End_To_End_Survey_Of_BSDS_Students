import pandas as pd
from scipy.stats import skew

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_scores = pd.to_numeric(data_frame_of_features.iloc[0][2:])
skewness_value = skew(series_of_scores)
print(f"The skewness of the distribution of scores is: {skewness_value}")