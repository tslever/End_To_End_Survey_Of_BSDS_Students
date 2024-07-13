import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_scores = pd.to_numeric(data_frame_of_features.iloc[0][2:])
hist_data = sns.histplot(series_of_scores, bins = 10, kde = True)
plt.title("Probability Distributions for \"The BSDS program was satisfying overall.\"")
plt.xlabel("Scores")
plt.ylabel("Probability Density")
bin_edges = np.histogram_bin_edges(series_of_scores, bins = 10)
bin_centers = 0.5 * (bin_edges[:-1] + bin_edges[1:])
plt.xticks(bin_centers, labels = range(1, 11))
plt.grid()
plt.legend()
plt.show()