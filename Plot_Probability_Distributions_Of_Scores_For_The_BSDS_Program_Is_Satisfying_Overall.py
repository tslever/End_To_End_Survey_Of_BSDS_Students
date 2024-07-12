import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_scores = pd.to_numeric(data_frame_of_features.iloc[0][2:])
score_counts = series_of_scores.value_counts().sort_index()
probabilities = score_counts / score_counts.sum()
plt.bar(probabilities.index, probabilities.values, width = 1.0, edgecolor = "black", alpha = 0.6, label = "Probability Distribution")
sns.kdeplot(series_of_scores, bw_adjust = 0.5, fill = True, label = "KDE", color = "blue")
plt.title("Probability Distribution of Scores for \"The BSDS program was satisfying overall.\"")
plt.xlabel("Scores")
plt.ylabel("Probability")
plt.xticks(probabilities.index)
plt.grid()
plt.legend()
plt.show()