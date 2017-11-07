import pandas as pd
names = ['student1','student2','student3','student4','student5']
marks_percantage = [80, 70, 60, 90, 65]
students_dataset = list(zip(names, marks_percantage))

print(students_dataset)

# loading to the Pandas dataframe
df = pd.DataFrame(
    data= students_dataset,
    columns= ['Names','marks_percentage']
)

print(df)

# Loading CSV Files

path = 'student_dataset.csv'
df1 = pd.read_csv(path)

print(df1)

# Exporting to csv

df.to_csv('student_dataset.csv')

# Finding the top percentage

max_percentage = df['marks_percentage'].max()
print(marks_percantage)

sorted = df.sort_values(['marks_percentage'], ascending= False)
print(sorted)

print(sorted.head(1))

# To store we can use the list function

store = list(df.columns.values)
print(store)

# Generate various statistic excluding null values we can use the describe function

summary = df.describe()
print(summary)

