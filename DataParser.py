'''
Parsing data to be visualized in tableau
'''

# import necessary libraries
import pandas as pd

# importing the raw data
df = pd.read_csv("./data/EmploymentRateCanada.csv")

# our new data will not have a column for each province. Instead, each province will be put into one 'province' column
parsed_df = pd.DataFrame(columns=['year', 'typeOfEmployment', 'sex', 'province', 'numEmployed'])

# To avoid overlapping data, will omit rows that group together types of employment, and sex
temp_df = df.loc[(df['variable'] != 'Employment') & (df['sex'] != 'Both sexes')]

provinces:list[str] = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick',
            'Newfoundland and Labrador', 'Nova Scotia', 'Ontario', 'Prince Edward Island',
            'Quebec', 'Saskatchewan']

for _, row in temp_df.iterrows():
    # Could take the average of each year, but for simplicity will just take the first month (January) of each year
    if row['month'][-2:] == "01":
        for province in provinces: 
            parsed_df.loc[len(parsed_df)] = [row['month'][:4], row['variable'], row['sex'], province, row[province]]

print(parsed_df)

# create a new csv with the parsed data to be used in tableau
parsed_df.to_csv('./data/EmploymentRateCanadaParsed.csv')