import pandas as pd
import numpy as np

# a = pd.Series([10, 20, 30, 40, 50])


# a = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])

# a = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

# a = pd.Series(5.0, index=['a', 'b', 'c', 'd', 'e'])
# print(a.dtype)
# print(a.index)
# print(a.values)
# print(a.get('a'))


###################################   Data Frame    ############################################


# data = {
#     'name': ['soma', 'bharat', 'varun', 'suresh'],
#     'age': [10, 20, 30, 40]
# }
# df = pd.DataFrame(data)
# print(df)


# data = {
#     'name': ['soma', 'bharat', 'varun', 'suresh'],
#     'age': [10, 20, 30, 40]
# }
# df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])
# print(df)
# print(df.index)
# print(df.name)
# print(df.age)
# print(df.name.get('a'))
# print(df.name.get('b'))
# print(df.name.get('c'))
# print(df.age.get('a'))
# print(df.age.get('b'))
# print(df.age.get('c'))


# data = {
#     "weight": pd.Series([10, 20, 30]),
#     "price": pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
# }
# df = pd.DataFrame(data)
# print(df)


# data = {
#     "weight": pd.Series([10, 20, 30], index=['a', 'b', 'c']),
#     "price": pd.Series([1.0, 2.0, 3.0, 4.0, 5.0], index=['a', 'b', 'c', 'd', 'e'])
# }
# df = pd.DataFrame(data)
# print(df)


# data = [{'a': 1, 'b': 2}, {'a': 1, 'b': 2, 'c': 3}]
# df = pd.DataFrame(data, index=[1, 0])
# print(df)


################################## INSPECTING DATA #####################################
# data = {

#     'name': [

#         'Sonam', 'Raj', 'Rohit', np.nan, 'Amit', 'Neha', 'Vikas', 'Pooja', 'Ajay', 'Raj', 'Suresh', 'Kiran', 'Anil', np.nan, 'Rahul', 'Sneha', 'Vivek', 'Raj', 'Arjun', 'Jyoti'

#     ],

#     'age': [

#         28, 24, 35, 32, 27, 26, np.nan, 29, 31, 22, 33, 21, np.nan, 23, 25, 20, 36, 19, np.nan, 18
#     ]

# }


# df = pd.DataFrame(data)
# print(df)
# print(df.info())
# print(df.isnull())
# print(df.isnull().sum())
# print(df.describe())
# print(df.head())
# print()
# print(df.head(10))
# print()
# print(df.tail())
# print()
# print(df.tail(10))
# print()
# print(df["name"].duplicated())
# print(df["name"].duplicated().sum())
# print(df.sort_index())
# print(df.sort_values('age'))
# print(df.sort_values('name'))


#############################          column selection or Indexing              #######################
# data = {

#     'name': [

#         'Sonam', 'Raj', 'Rohit', np.nan, 'Amit', 'Neha', 'Vikas', 'Pooja', 'Ajay', 'Raj', 'Suresh', 'Kiran', 'Anil', np.nan, 'Rahul', 'Sneha', 'Vivek', 'Raj', 'Arjun', 'Jyoti'

#     ],

#     'age': [

#         28, 24, 35, 32, 27, 26, np.nan, 29, 31, 22, 33, 21, np.nan, 23, 25, 20, 36, 19, np.nan, 18
#     ],
#     'roll': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
#     'city': [
#         'Bokaro', 'Ranchi', 'Dhanbad', 'Deoghar', 'Giridih', 'Jamshedpur', 'Dumka', 'Delhi', 'Kolkata', 'Mumbai', 'Hazaribagh', 'Ramgarh', 'Gumla', 'Patna', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 'Ahmedabad', 'Lucknow']

# }

# df = pd.DataFrame(data)
# print("single column data :")
# print(df['name'])
# print()

# print(df['age'])
# print()

# print('multiple column')
# print(df[['name', 'city', 'roll', 'age']])

# print('select row by integer location :')
# print(df.iloc[2])


# print('select row by label :')
# print(df.loc[2])


# print("slice row :")
# print(df[1:4])


# print('select row by condition :')
# print(df['age'] > 25)
# print()
# print(df[df['age'] > 25])


####################################  columb insertion ##############################################

# data = {

#     'name': [

#         'Sonam', 'Raj', 'Rohit', np.nan, 'Amit', 'Neha', 'Vikas', 'Pooja', 'Ajay', 'Raj', 'Suresh', 'Kiran', 'Anil', np.nan, 'Rahul', 'Sneha', 'Vivek', 'Raj', 'Arjun', 'Jyoti'

#     ],

#     'age': [

#         28, 24, 35, 32, 27, 26, np.nan, 29, 31, 22, 33, 21, np.nan, 23, 25, 20, 36, 19, np.nan, 18
#     ],
#     'roll': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120],
#     'city': [
#         'Bokaro', 'Ranchi', 'Dhanbad', 'Deoghar', 'Giridih', 'Jamshedpur', 'Dumka', 'Delhi', 'Kolkata', 'Mumbai', 'Hazaribagh', 'Ramgarh', 'Gumla', 'Patna', 'Bangalore', 'Hyderabad', 'Chennai', 'Pune', 'Ahmedabad', 'Lucknow']

# }

# df = pd.DataFrame(data)

# insert or add scaler value
# df['result'] = "Pass"
# print(df)


# Insert ndarrays - length must be same - columns get inserted at the end

# df["marks"] = [234, 453, 556, 676, 676, 453, 232, 234, 234,
#                123, 124, 567, 231, 867, 234, 566, 756, 678, 453, 354]
# print(df)


# inset()  -  it used for inserting columns at a particular position
# hobbies = ["cricket", "vgame", "reading", "singing", "chatting", "computer", "fighting", "cricket", "vgame", "reading", "singing", "chatting", "computer", "fighting",
#            "cricket", "vgame", "reading", "singing", "chatting", "computer"]

# df.insert(2, "hobbies", hobbies)
# print(df)

# df['fees'] = df['marks']*12
# print(df)


########################################    column  updation    ########################################

# data = {
#     'name': ['deoghar', 'Raj', 'Rohit', 'Rani'],
#     'age': [28, 24, 35, 32],
#     'roll': [101, 102, 103, 104],
#     'marks': [111, 222, 333, 444],
#     'city': ['bokaro', 'ranchi', 'dhanbad', 'deoghar']
# }


# df = pd.DataFrame(data)
# print("Display All Data:\n", df)


# update all fields of a column
# df['gender'] = 'F'
# print(df)


# update specific field of a column
# df.loc[df['roll'] == 102, 'marks'] = 999
# print(df)

# replace values
# print(df.replace('deoghar', 'dumk'))


#################################    column deletion         #########################


# data = {
#     'name': ['deoghar', 'Raj', 'Rohit', 'Rani'],
#     'age': [28, 24, 35, 32],
#     'roll': [101, 102, 103, 104],
#     'marks': [111, 222, 333, 444],
#     'city': ['bokaro', 'ranchi', 'dhanbad', 'deoghar'],
#     'gender': ['F', 'M', 'M', 'F']
# }

# df = pd.DataFrame(data)
# print(df)
# print()

# delete single column
# del df['gender']
# print(df)


# pop single column
# p = df.pop('city')
# print(p)
# print()
# print(df)

# DELETE MULTIPLE COLUMNS
# print(df)
# print()
# drop just return the new data frame of included columns and does not show any effect on original column
# print(df.drop(columns=['city', 'gender']))
# print()
# print(df)


#   DELETE DUPLICATE VALUES
# print(df)
# print()
# print(df.drop_duplicates('name'))


#####################################   Filtering     #################################

# data = {
#     'name': ['deoghar', 'Raj', 'Rohit', 'Rani'],
#     'age': [28, 24, 35, 32],
#     'roll': [101, 102, 103, 104],
#     'marks': [111, 222, 333, 444],
#     'city': ['bokaro', 'ranchi', 'dhanbad', 'deoghar'],
#     'gender': ['F', 'M', 'M', 'F']
# }

# df = pd.DataFrame(data)

# print(df)
# print()

# dt1 = df['age'].isin([28, 35])
# print(dt1)
# print()

# dt2 = df[df['age'].isin([28, 35])]
# print(dt2)


####################################   MISSING DATA    ###########################


# data = {
#     'name': ['deoghar', 'Raj', 'Rohit', 'Rani'],
#     'age': [28, 24, np.nan, 32],
#     'roll': [101, 102, 103, 104],
#     'marks': [111, 222, 333, np.nan],
#     'city': ['bokaro', 'ranchi', 'dhanbad', 'deoghar'],
#     'gender': ['F', 'M', 'M', 'F']
# }


# df = pd.DataFrame(data)
# print(df)
# print()


# Boolean mask where values are nan
# print(df.isna())
# print()
# print(df.isna().sum())
# print()

# Fill some value in missing data
# print(df.fillna(value=123))
# print()

# remove missing data
# print(df.dropna())

# Backward Filling
# print(df.bfill())

# Forward Filling
# print(df.ffill())


########################    STATS      ###########################
# data = {
#     'name': ['deoghar', 'Raj', 'Rohit', 'Rani'],
#     'age': [28, 24, np.nan, 32],
#     'roll': [101, 102, 103, 104],
#     'marks': [111, 222, 333, np.nan],
#     'city': ['bokaro', 'ranchi', 'dhanbad', 'deoghar'],
#     'gender': ['F', 'M', 'M', 'F']
# }


# df = pd.DataFrame(data)
# print(df)
# print()

# CALCULATING THE MEAN OF 'AGE' COLUMN
# print(df['age'].mean())
# print()

# CALCULATE THE MEAN OF 'AGE' COLUMN INCLUDING NAN VALUES
# print(df['age'].mean(skipna=False))


# CALCULATE THE MEAN OF 'AGE' AND 'MARKS' COLUMN
# print(df[['age', 'marks']].mean())

# apply a single aggregate function
# age_mean = df['age'].agg(['mean'])
# print(age_mean)

# apply multiple aggregate functions
# stats = df['age'].agg(['mean', 'min', 'max'])
# print(stats)


# apply different aggregate functions to different columns
# custom_agg = df.agg({
#     'age': ['mean', 'min', 'max'],
#     'marks': 'sum',
#     'roll': 'count'
# })

# print(custom_agg)


########################    TRANSFORMATION      ###########################
# data = {
#     'name': ['deoghar', 'Raj', 'Rohit', 'Rani'],
#     'age': [28, 24, np.nan, 32],
#     'roll': [101, 102, 103, 104],
#     'marks': [111, 222, 333, np.nan],
#     'city': ['bokaro', 'ranchi', 'dhanbad', 'deoghar'],
#     'gender': ['F', 'M', 'M', 'F']
# }


# df = pd.DataFrame(data)
# apply a single transform function
# print(df['age'].transform(lambda x: x+1))


# apply transform function to multiple columns
# print(df[['age', 'marks']].transform(lambda x: x**2))


# apply different transform function to different columns
# print(df.transform({
#     'age': lambda x: x+1,
#     'marks': lambda x: x**2
# }))


########################    value counts      ###########################

# data = {
#     'name': ['deoghar', 'Raj', 'Rohit', 'Rani'],
#     'age': [28, 24, np.nan, 32],
#     'roll': [101, 102, 103, 104],
#     'marks': [111, 222, 333, np.nan],
#     'city': ['bokaro', 'ranchi', 'dhanbad', 'deoghar'],
#     'gender': ['F', 'M', 'M', 'F']
# }
# df = pd.DataFrame(data)

# use value_counts to count unique values in city column
# print(df['city'].value_counts())


# use value_counts to cout unique values in marks column including nan value
# print(df['marks'].value_counts(dropna=False))

########################    String Methods      ###########################

# data = {
#     'name': ['deoghar', 'Raj', 'Rohit', 'Rani'],
#     'age': [28, 24, np.nan, 32],
#     'roll': [101, 102, 103, 104],
#     'marks': [111, 222, 333, np.nan],
#     'city': ['bokaro', 'ranchi', 'dhanbad', 'deoghar'],
#     'gender': ['F', 'M', 'M', 'F']
# }
# df = pd.DataFrame(data)

# convert to lowercase
# print(df['name'].str.lower())

# convert to uppercase
# print(df['city'].str.upper())

# compute length
# print(df['name'].str.len())

# extract first three characters
# print(df['name'].str[:3])

# string replace method
# print(df['name'].str.replace('a', 'A'))


########################    MERGE      ###########################

# df1 = pd.DataFrame({
#     'id': [1, 2, 3, 4],
#     'name': ['Sonam', 'Raj', 'Sonal', 'Rajeev']
# })
# df2 = pd.DataFrame({
#     'id': [3, 4, 5, 6],
#     'score': [90, 80, 70, 60]
# })

# inner join
# inner_join = pd.merge(df1, df2, on='id')
# print(inner_join)

# left join
# left_join = pd.merge(df1, df2, on='id', how='left')
# print(left_join)


# use left_on and right_on for performing merge on different column from each data frame
# df3 = pd.DataFrame({
#     'id': [1, 2, 3, 4],
#     'name': ['Sonam', 'Raj', 'Sonal', 'Rajeev']
# })
# df4 = pd.DataFrame({
#     'stu_id': [3, 4, 5, 6],
#     'score': [90, 80, 70, 60]
# })

# inner_join = pd.merge(df3, df4, left_on='id', right_on='stu_id')
# print(inner_join)


########################    CONCATENATE      ###########################

# df1 = pd.DataFrame({
#     'Α': ['ΑΘ', 'A1', 'A2', 'A3'],
#     'B': ['BO', 'B1', 'B2', 'B3']
# })
# df2 = pd.DataFrame({
#     'A': ['A4', 'A5', 'A6', 'A7'],
#     'B': ['B4', 'B5', 'B6', 'B7']
# })
# df3 = pd.DataFrame({
#     'C': ['CO', 'C1', 'C2', 'C3'],
#     'D': ['D0', 'D1', 'D2', 'D3']
# })

# vertical concatenation
# vertical_concat = pd.concat([df1, df2])

# print(vertical_concat)


# horizontal concatenation
# horizontal_concat = pd.concat([df1, df2], axis=1)
# print(horizontal_concat)


########################    PIVOT TABLE      ###########################


# data = {
#     'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
#     'City': ['Bokaro', 'Ranchi', 'Dhanbad', 'Dumka'],
#     'Sales': [200, 150, 300, 200],
#     'Expenses': [50, 60, 70, 80]
# }
# df = pd.DataFrame(data)
# print("Original DataFrame:\n", df)


# Basic pivot table
# pivot = pd.pivot_table(df, index='Date', columns='City',
#                        values='Sales', aggfunc='sum')
# print(pivot)


# pivot table with multiple aggregation
# pivot_table = pd.pivot_table(df, index='Date',
#                              values=['Sales', 'Expenses'], columns='City', aggfunc={'Sales': 'sum', 'Expenses': 'mean'}, margins=True)
# print(pivot_table)

# fill 0 for nan values
# pivot_table = pd.pivot_table(df, fill_value=0, index='Date',
#                              values=['Sales', 'Expenses'], columns='City', aggfunc={'Sales': 'sum', 'Expenses': 'mean'}, margins=True)
# print(pivot_table)


########################     EXPORT TO CSV      ###########################


# data = {
#     'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
#     'City': ['Bokaro', 'Ranchi', 'Dhanbad', 'Dumka'],
#     'Sales': [200, 150, 300, 200],
#     'Expenses': [50, 60, 70, 80]
# }

# df = pd.DataFrame(data)
# df.to_csv('sample.csv', index=False)


########################     IMPORTING TO CSV      ###########################


df_read = pd.read_csv(
    'annual-enterprise-survey-2021-financial-year-provisional-csv.csv')
print(df_read)
