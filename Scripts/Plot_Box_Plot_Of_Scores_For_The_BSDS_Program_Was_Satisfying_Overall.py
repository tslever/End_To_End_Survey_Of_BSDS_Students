import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_scores = pd.to_numeric(data_frame_of_features.iloc[0][2:])
plt.figure(figsize = (10, 6))
sns.boxplot(x = series_of_scores)
plt.title("Box Plot of Scores for \"The BSDS program was satisfying overall.\"")
plt.xlabel("Scores")
plt.grid()
plt.show()