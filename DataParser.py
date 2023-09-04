'''
Parsing data to be visualized in tableau
'''

# import necessary libraries
import pandas as pd

# importing the raw data
df = pd.read_csv("./data/EmploymentRateCanada.csv")

# NEW IMPLEMENTATION: uses the pandas.melt function for cleaner code

# our new data will not have a column for each province. Instead, each province will be put into one 'province' column
# to avoid overlapping data, will omit rows that group together types of employment, and sex
# could take the average of each year, but for simplicity will just take the first month (January) of each year
df = df[(df['variable'] != 'Employment') & (df['sex'] != 'Both sexes') & (df['month'].str.contains("-01"))].rename(columns={'month': 'year', 'variable': 'typeOfEmployment'})

# only care about year now so can remove the month
df['year'] = df['year'].str.slice(0,4)

provinces:list[str] = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick',
            'Newfoundland and Labrador', 'Nova Scotia', 'Ontario', 'Prince Edward Island',
            'Quebec', 'Saskatchewan']

df = pd.melt(df, id_vars=['year', 'typeOfEmployment', 'sex'], value_vars=provinces, var_name='province', value_name='numEmployed')

# OLD IMPLEMENTATION

# # our new data will not have a column for each province. Instead, each province will be put into one 'province' column
# parsed_df = pd.DataFrame(columns=['year', 'typeOfEmployment', 'sex', 'province', 'numEmployed'])

# # To avoid overlapping data, will omit rows that group together types of employment, and sex
# temp_df = df.loc[(df['variable'] != 'Employment') & (df['sex'] != 'Both sexes')]

# provinces:list[str] = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick',
#             'Newfoundland and Labrador', 'Nova Scotia', 'Ontario', 'Prince Edward Island',
#             'Quebec', 'Saskatchewan']

# for _, row in temp_df.iterrows():
#     # Could take the average of each year, but for simplicity will just take the first month (January) of each year
#     if row['month'][-2:] == "01":
#         for province in provinces: 
#             parsed_df.loc[len(parsed_df)] = [row['month'][:4], row['variable'], row['sex'], province, row[province]]

# print(parsed_df)

# create a new csv with the parsed data to be used in tableau
df.to_csv('./data/test.csv')