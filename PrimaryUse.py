import pandas as pd
import matplotlib.pyplot as plt

# Read in the CSV file
df = pd.read_csv('formResponses.csv')

# Split the multi-select column into dummy variables
dummies = df['What has been your primary use for ChatGPT?'].str.get_dummies(sep=',')

# Sum the dummy variables across rows to get the count for each option
primary_counts = dummies.sum()

# Plot a bar chart of the counts
primary_counts.plot(kind='bar', edgecolor='black')
plt.xlabel('What has been your primary use for ChatGPT?')
plt.ylabel('Count')
plt.title('Primary Use Count')
plt.show()
