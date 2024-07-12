import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_scores = pd.to_numeric(data_frame_of_features.iloc[0][2:])
series_of_ages = pd.to_numeric(data_frame_of_features.iloc[520][2:])
series_of_genders = data_frame_of_features.iloc[521][2:]
data_frame = pd.DataFrame({
    "Score": series_of_scores,
    "Age": series_of_ages,
    "Gender": series_of_genders
})
sns.boxplot(x = "Age", y = "Score", hue = "Gender", data = data_frame)
plt.title("Box Plot of Scores for \"The BSDS program was satisfying overall.\" by Age and Gender")
plt.xlabel("Age")
plt.ylabel("Score")
plt.grid()
plt.show()