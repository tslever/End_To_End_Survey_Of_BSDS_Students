import pandas as pd
import matplotlib.pyplot as plt

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_scores_for_Loreto_Alonzi_performed_satisfactory_overall = pd.to_numeric(data_frame_of_features.iloc[176][2:])
series_of_scores_for_Loreto_Alonzi_was_hardworking = pd.to_numeric(data_frame_of_features.iloc[186][2:])
series_of_ages = pd.to_numeric(data_frame_of_features.iloc[520][2:])
normalized_series_of_ages = (series_of_ages - series_of_ages.min()) / (series_of_ages.max() - series_of_ages.min())
plt.scatter(
    series_of_scores_for_Loreto_Alonzi_performed_satisfactory_overall, 
    series_of_scores_for_Loreto_Alonzi_was_hardworking,
    c = normalized_series_of_ages,
    cmap = "viridis"
)
plt.colorbar(label = "Age")
plt.title("Scores for \"Loreto Alonzi Performed Satisfactorily Overall.\" vs. Scores for \"Loreto Alonzi was Hardworking.\" and Age")
plt.xlabel("Scores for \"Loreto Alonzi performed satisfactorily overall.\"")
plt.ylabel("Scores for \"Loreto Alonzi was hardworking.\"")
plt.grid()
plt.show()