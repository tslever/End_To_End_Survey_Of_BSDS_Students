import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_scores = pd.to_numeric(data_frame_of_features.iloc[0][2:])
df_for_plotting = pd.DataFrame({"Scores": series_of_scores})
sns.violinplot(y = "Scores", data = df_for_plotting)
plt.title("Violin Plot of Scores for \"The BSDS program was satisfying overall\"")
plt.ylabel("Scores")
plt.grid()
plt.show()