'''
Parsing data to be visualized in tableau
'''

# import necessary libraries
import pandas as pd

df = pd.read_csv("./data/EmploymentRateCanada.csv")

result_df = df.drop_duplicates(subset=['month'], keep='first')
result_df.drop('variable', axis=1, inplace=True)
result_df.drop('sex', axis=1, inplace=True)
result_df['month'] = result_df['month'].str.slice(start=0, stop=4)
result_df.rename(columns={'month': 'year'}, inplace=True)
aggregation_functions = {'Alberta': 'sum', 'British Columbia': 'sum', 
                         'Manitoba': 'sum', 'New Brunswick': 'sum',
                         'Newfoundland and Labrador': 'sum', 'Nova Scotia': 'sum', 
                         'Ontario': 'sum', 'Prince Edward Island': 'sum',
                         'Quebec': 'sum', 'Saskatchewan': 'sum'}
result_df = result_df.groupby(result_df['year']).aggregate(aggregation_functions)
result_df.to_csv("./data/TimeToEmployment.csv")



recent_employment = result_df.iloc[-1]
recent_employment.to_csv("test")