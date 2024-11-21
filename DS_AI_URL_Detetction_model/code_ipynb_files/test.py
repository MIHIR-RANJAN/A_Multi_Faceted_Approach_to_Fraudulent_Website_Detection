import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
dt = pd.read_csv('cleanedData.csv')

# Filter rows where 'class' equals 1
dt = dt[dt['class'] == 1]

# Select the 30 columns (excluding 'class')
columns_to_plot = dt.columns.difference(['class'])

# Initialize dictionary to hold counts of -1, 0, and 1 for each column
value_counts = {col: dt[col].value_counts().reindex([-1, 0, 1], fill_value=0) for col in columns_to_plot}

# Convert dictionary to DataFrame for plotting
count_dt = pd.DataFrame(value_counts)

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
bar_width = 0.25
index = np.arange(len(columns_to_plot))

# Plot each bar for -1, 0, 1 values with custom colors
colors = {-1: 'orange', 0: 'green', 1: 'blue'}  # Define colors for each value
for i, value in enumerate([-1, 0, 1]):
    ax.bar(index + i * bar_width, count_dt.loc[value], width=bar_width, 
           label=f'{value}', color=colors[value])

# Set labels and title
ax.set_xlabel('Columns')
ax.set_ylabel('Frequency')
ax.set_title('Frequency of values -1, 0, and 1 for each column')
ax.set_xticks(index + bar_width)
ax.set_xticklabels(columns_to_plot, rotation=90)
ax.legend(title='Value')

plt.tight_layout()
plt.show()
