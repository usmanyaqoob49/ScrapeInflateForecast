import pandas as pd

# Reading the CSV file that I made with the scrapt data
df = pd.read_csv('inflation_rate.csv')

#now what i want is to Convert data from yearly to month 
#as i have monthly data in columns so i can melt/transform dataframe to get data in rows

months= ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
       'Sep', 'Oct', 'Nov', 'Dec']

#dataframe to store transformed data
concatenated_df= pd.DataFrame()

#now lets iterate over each column which is month and try to melt data frame with that colum
#simply we will make every column a row 
for month in months:
    melted_df = pd.melt(df, id_vars=['Year'], value_vars=[month])
    concatenated_df= pd.concat([concatenated_df, melted_df])


concatenated_df['Date']= concatenated_df['variable'].astype(str) + '/' + concatenated_df['Year'].astype(str)
del concatenated_df['Year']
del concatenated_df['variable']

#converting to date column
concatenated_df['Date']= pd.to_datetime(concatenated_df['Date'], format= '%b/%Y')
concatenated_df.to_csv('new.csv')
print(concatenated_df.head(60))

