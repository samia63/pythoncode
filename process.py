"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

from pandas import *
data = read_csv('C:/covid_19_data.csv')
SNo = data['SNo'].tolist()
od = data['ObservationDate'].tolist()
ps = data['Province/State'].tolist()
cr = data['Country/Region'].tolist()
ld = data['Last Update'].tolist()
cd = data['Confirmed'].tolist()
dt = data['Deaths'].tolist()
rc = data['Recovered'].tolist()




The required functions are as follows:
- Retrieve the total number of records that have been loaded.

integers_list1 = [SNo]
integers_list2 = [od]
integers_list3 = [ps]
integers_list4 = [cr]
integers_list5 = [ld]
integers_list6 = [cd]
integers_list7 = [dt]
integers_list8 = [rc]
newlist = []
newlist.extend(integers_list1)
newlist.extend(integers_list2)
newlist.extend(integers_list3)
newlist.extend(integers_list4)
newlist.extend(integers_list5)
newlist.extend(integers_list6)
newlist.extend(integers_list7)
newlist.extend(integers_list8)
joinedlist = integers_list1 + integers_list2 + integers_list3 + integers_list4 +  integers_list5 +  integers_list6 +  integers_list7 +  integers_list8 

print(newlist)



- Retrieve a record with the serial number as specified by the user.

 (df.loc[df['SNo'] == int(input("Enter the Serial number : ", ))])



- Retrieve the records for the observation dates as specified by the user.


(df.loc[df['ObservationDate'] == str(input("Enter the Observation Date : "))])


- Retrieve all of the records grouped by the country/region.

import pandas as pd
df = pd.read_csv('C:/covid_19_data.csv')
df
gk = df.groupby('Country/Region')
gk.first()


- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 df_new = df[['Country/Region', 'Confirmed','Deaths','Recovered']]
df_new

"""

# TODO: Your code here
