import pandas as pd

## Reading

# df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
# df = pd.read_json("data.json")
# df = pd.read_excel("data.xlsx")

# print(df.columns)
# print(df.info())
# print(df.describe())
# print(df.head())
# print(df.tail())
# print(df.shape)



## Writing

# data = {
#     "Name": ["alice", "bob", "tom"],
#     "Age": [34, 24, 14],
#     "Marks": [89, 99, 54]
# }

# df = pd.DataFrame(data)

# df.to_excel("data.xlsx", index=False)


##Adding columns

df = pd.read_csv("python_practice/data.csv")
# print(df)

# df['Salary'] = [20000, 30000]
# # print(df)

# df.insert(2, "City", ["US", "UK"])
# # print(df)

# df.to_csv("python_practice/data.csv", index=False)

## Updating values using .loc[]
# df.loc[1, "Age"] = 26
# print(df)

##Removing columns

# df.drop(columns=["City", "Salary"], inplace=True)
# print(df)

##Handling Missing Data

# print(df.isnull().sum())

# df.dropna(inplace=True)  #axis=0  (default, 0-row, 1-columns)
# print(df)

# df.fillna(0, inplace=True)   ##fill all null values-0
# df['Name'].fillna("Unknown", inplace=True)
# df['Age'].fillna(df['Age'].mean(), inplace=True)
# print(df)

#Interpolation -- for numeric only
# #linear, polynomial, time
# df["Salary"] = df["Salary"].interpolate(method="linear")
# print(df)

#sort_values
# df.sort_values(by="Age", ascending=True, inplace=True)    ##multi  by=["Age", "Column"]
# print(df)

#groupby
# print(df.groupby("Age")["Salary"].sum())
# print(df.groupby(["Age", "Name"])["Salary"].sum())


# Group by Department and calculate multiple stats
# agg_stats = df.groupby('Department').agg({
#     'Salary': ['mean', 'max', 'min'],
#     'Experience': 'sum'
# })
# print(agg_stats)


#Merge and Join

# df_customers = pd.DataFrame({
#     "CustID": [1, 2, 3, 4],
#     "Name": ["Alice", "Bob", "Cherry", "Russ"]
# })

# df_orders = pd.DataFrame({
#     "CustID": [1, 2, 5, 6],
#     "Orders": [10, 9, 14, 5]
# })

# df_payment = pd.DataFrame({
#     "CustID": [1, 2, 3, 4, 5, 6],
#     "Orders": [100, 900, 1400, 50, 1500, 800]
# })

# df_merged = pd.merge(df_customers, df_orders, on="CustID", how="inner")
# print(df_merged)


# Check for duplicates
# print(df.duplicated())

# # Remove duplicates
# df_no_duplicates = df.drop_duplicates()
# print(df_no_duplicates)



# Convert column to integer
# df['Salary'] = df['Salary'].astype(int)

# renaming Columns
# df.rename(columns={'Employee': 'Emp_Name'}, inplace=True)

