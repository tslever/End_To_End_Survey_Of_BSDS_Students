import pandas as pd
import matplotlib.pyplot as plt

data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header = 0, index_col = 0)
series_of_scores = pd.to_numeric(data_frame_of_features.iloc[0][2:])
series_of_ages = pd.to_numeric(data_frame_of_features.iloc[520][2:])
series_of_genders = data_frame_of_features.iloc[521][2:]
data_frame = pd.DataFrame({
    "Age": series_of_ages,
    "Gender": series_of_genders,
    "Score": series_of_scores
})
unique_scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
unique_genders = data_frame["Gender"].unique()
n_rows, n_cols = 5, 2
fig, axes = plt.subplots(n_rows, n_cols, figsize = (15, 10))
axes = axes.flatten()
for ax, score in zip(axes, unique_scores):
    score_data = data_frame[data_frame["Score"] == score]
    if not score_data.empty:
        proportions = []
        for gender in unique_genders:
            gender_data = score_data[score_data["Gender"] == gender]
            age_counts = gender_data["Age"].value_counts(normalize = True).sort_index()
            proportions.append(age_counts)
        proportions_df = pd.DataFrame(proportions, index = unique_genders).fillna(0)
        proportions_df.plot(kind = "bar", stacked = True, ax = ax, colormap = "viridis")
        ax.set_xticklabels(ax.get_xticklabels(), rotation = 0)
    else:
        list_of_genders = ["Man", "Woman", "Transgender Man", "Transgender Woman"]
        ax.set_xticks(range(len(list_of_genders)))
        ax.set_xticklabels(list_of_genders)
    ax.set_title(f"Score: {score}")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Proportion of Ages")
    legend = ax.legend(title = "Age", bbox_to_anchor = (1.05, 1), loc = "upper left", fontsize = "small")
    ax.grid()
fig.suptitle("Bar Charts of Ages, Genders, and Scores")
plt.tight_layout()
plt.show()