import os
# Import pandas — a Python tool that helps us work with tables (like Excel)
import pandas as pd
print("Current working directory:", os.getcwd())
# Load the survey CSV file
data = pd.read_csv('C:\\Users\\ankus\\Microsoft VS Code\\survey.csv')

# Print the first 5 rows so we can see what the data looks like
print(data.head())

# Remove rows with missing values
clean_data = data.dropna()

# Show how many rows are left after cleaning
print("Rows after cleaning:", clean_data.shape[0])

# Save the clean data to a new CSV for Power BI
clean_data.to_csv('clean_survey.csv', index=False)

import matplotlib.pyplot as plt

# Count how many people answered 'Yes' or 'No' to getting treatment
treatment_counts = clean_data['treatment'].value_counts()

# Plot it
treatment_counts.plot(kind='bar')
plt.title('Mental Health Treatment: Yes vs No')
plt.xlabel('Treatment')
plt.ylabel('Number of People')
plt.show()

