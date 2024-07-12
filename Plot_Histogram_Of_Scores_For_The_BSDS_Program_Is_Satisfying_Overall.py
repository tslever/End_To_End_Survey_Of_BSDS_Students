import matplotlib.pyplot as plt
import pandas as pd

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_scores = pd.to_numeric(data_frame_of_features.iloc[0][2:])
score_counts = series_of_scores.value_counts().sort_index()
plt.bar(score_counts.index, score_counts.values, width = 1.0, edgecolor = "black")
plt.title("Histogram of Scores for \"The BSDS program was satisfying overall.\"")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.xticks(score_counts.index)
plt.grid()
plt.show()