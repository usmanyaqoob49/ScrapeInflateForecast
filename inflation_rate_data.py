from bs4 import BeautifulSoup
import requests
import pandas as pd

#url of the website 
url= "https://www.usinflationcalculator.com/inflation/historical-inflation-rates/"
#getting html page by requesting
html_page= requests.get(url)

print("Response Status Code: ", html_page.status_code)
#storing content of page
html_page= html_page.content

# #parsing the html page with lxml
soup= BeautifulSoup(html_page, 'lxml')

#Now we need to extract rows of the table--> we do it by giving 'tr' that mean row and class of the row specified in html code of page
trs=  soup.find_all('tr')

#print(trs)

# #to store the data
data_list= []

#now lets iterate over trs to get data and headers from each row
for tr in trs:
    #extracting headers th and data td from each row 
    row_data= [td.text.strip() for td in tr.find_all(['td', 'th'])]
    # Create a dictionary for the row
    row_dict = {f'Column{i}': value for i, value in enumerate(row_data)}
    
    # Append the dictionary to the list
    data_list.append(row_dict)

#making the dataframe from the list that have our dictionary
df= pd.DataFrame(data_list)
# df.to_csv('Inflation_rate.csv')
print(df.head())
