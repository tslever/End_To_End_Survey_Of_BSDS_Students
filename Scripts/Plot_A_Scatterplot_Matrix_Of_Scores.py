import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_scores_in_row_0 = pd.to_numeric(data_frame_of_features.iloc[0][2:])
series_of_scores_in_row_1 = pd.to_numeric(data_frame_of_features.iloc[1][2:])
series_of_scores_in_row_2 = pd.to_numeric(data_frame_of_features.iloc[2][2:])
scores_df = pd.DataFrame({
    'Scores in Row 0': series_of_scores_in_row_0,
    'Scores in Row 1': series_of_scores_in_row_1,
    'Scores in Row 3': series_of_scores_in_row_2
})
g = sns.pairplot(scores_df)
plt.subplots_adjust(top = 0.95)
g.figure.suptitle("Scatterplot Matrix of Scores", fontsize = 16)
for ax in g.axes.flatten():
    ax.grid(True)
plt.show()