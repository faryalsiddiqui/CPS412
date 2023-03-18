import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file
responses = pd.read_csv('formResponses.csv')

# Append the fields into a variables array
variables = ['What is your age', 
             'What is your role in academia?',
             'What is your gender?', 
             'Education (Highest level of education you have achieved/ are pursuing)', 
             'What is your Ethnicity', 
             'What is your academic field?', 
             'Have you used ChatGPT before?', 
             'I have found ChatGPT to be useful in my personal or professional life.', 
             'ChatGPT should be used in school', 
             'ChatGPT is a reliable resource for information',
             'Students should be allowed to use ChatGPT for school-related purposes', 
             'There should be restrictions or guidelines for the use of ChatGPT in schools and universities', 
             'Do you believe that the usage of ChatGPT could put potential harm in the learning ability of students in the future?', 
             'Would you recommend/ Have you recommended ChatGPT to others?']

# Loop over each variable and create a pie chart
for var in variables:
    # selects the column with the name var from the DataFrame.
    pie_counts = responses[var]

    # count the frequency of UNIQUE values in an object called pie_counts
    pie_counts = pie_counts.value_counts()  

    # create a pie chart
    plt.pie(pie_counts, labels=pie_counts.index, autopct='%1.1f%%', radius=1.0, pctdistance=0.85)

    # set the title of the piechart to the variable name
    plt.title(var)

    # displays the pie chart
    plt.show() 
