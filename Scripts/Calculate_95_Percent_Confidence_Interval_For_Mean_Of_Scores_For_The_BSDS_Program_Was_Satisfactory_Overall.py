import pandas as pd
from scipy.stats import t, sem

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_scores = pd.to_numeric(data_frame_of_features.iloc[0][2:])
mean_score = series_of_scores.mean()
standard_error_of_the_mean = sem(series_of_scores)
confidence_interval = t.interval(0.95, len(series_of_scores) - 1, loc = mean_score, scale = standard_error_of_the_mean)
print(f"The 95% confidence interval for the mean of the scores is: {confidence_interval}")