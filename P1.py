#20mca031-JigarLeuva Assign-1
import requests
import json
import pandas as pd


#Fetch the JSON file programmatically and store the data in the data structure of your choice.

data=requests.get('https://s3.amazonaws.com/open-to-cors/assignment.json').text
res_info=json.loads(data)

#store it into dict
product_info=res_info['products']
print(type(product_info))

sub_cat=list(product_info.values())
print(type(sub_cat))


#convert data into dataframe
dfdata=pd.DataFrame(sub_cat)


dfdata.sort_values('popularity')

#Display the data in the presentation of your choice with Title, Price ordered based on the descending popularity.
print(dfdata[['title','price']])


  
