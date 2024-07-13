import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_scores = pd.to_numeric(data_frame_of_features.iloc[0][2:])
series_of_genders = data_frame_of_features.iloc[521][2:]
data = pd.DataFrame({
    "Score": series_of_scores,
    "Gender": series_of_genders
})
sns.histplot(data = data, x = "Score", hue = "Gender", kde = True)
plt.title("Probability Density Distributions of Scores by Gender")
plt.xlabel("Score")
plt.ylabel("Probability Density")
plt.grid()
plt.show()