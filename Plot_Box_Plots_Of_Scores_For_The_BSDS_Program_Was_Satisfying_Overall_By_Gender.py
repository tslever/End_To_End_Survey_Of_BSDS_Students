import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_scores = pd.to_numeric(data_frame_of_features.iloc[0][2:])
series_of_genders = data_frame_of_features.iloc[521][2:]
data_frame_of_scores_and_genders = pd.DataFrame({"Score": series_of_scores, "Gender": series_of_genders})
sns.boxplot(x = "Gender", y = "Score", data = data_frame_of_scores_and_genders)
plt.title("Box Plot of Scores for \"The BSDS program was satisfying overall.\" by Gender")
plt.xlabel("Gender")
plt.ylabel("Score")
plt.grid()
plt.show()