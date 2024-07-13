import pandas as pd
from scipy.stats import t, sem

# Load the data
data_frame_of_features = pd.read_csv("Feature_Matrix.csv", header=0, index_col=0)

# Extract the series of scores
series_of_scores = pd.to_numeric(data_frame_of_features.iloc[0][2:])

# Calculate the sample mean and sample size
sample_mean = series_of_scores.mean()
sample_size = len(series_of_scores)
sample_standard_error = sem(series_of_scores)

# Define the population mean under the null hypothesis
population_mean = 5

# Calculate the t-statistic
t_statistic = (sample_mean - population_mean) / sample_standard_error

# Degrees of freedom
df = sample_size - 1

# Calculate the critical t-value for a one-tailed test at a 95% confidence level
alpha = 0.05
critical_t_value = t.ppf(1 - alpha, df)

# Calculate the p-value
p_value = 1 - t.cdf(t_statistic, df)

# Print the results
print(f"Sample Mean: {sample_mean}")
print(f"T-Statistic: {t_statistic}")
print(f"Critical T-Value: {critical_t_value}")
print(f"P-Value: {p_value}")

# Conclusion
if t_statistic > critical_t_value:
    print("Reject the null hypothesis: The true population mean is greater than 5.")
else:
    print("Fail to reject the null hypothesis: There is not enough evidence to conclude the true population mean is greater than 5.")