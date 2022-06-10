"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should display the title 'COVID-19 (January) Data'.
    The welcome message should contain dashes above and below the title.
    The number of dashes should be equivalent to the number of characters in the title.

    :return: Does not return anything.
    """
    # TODO: Your code here
    def welcome (name):
    welcome ('COVID-19_January_ Data')





def error(msg):
    """
    Task 2: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter 'msg' passed to this function

    :param msg: a string containing an error message
    :return: does not return anything
    """
    # TODO: Your code here
    def error(error_msg):
    error ('syntax error')





def progress(operation, value):
    """
    Task 3: Display a message to indicate the progress of an operation.

    The function should display a message in the following format:
    '{operation} {status}.'

    Where {operation} is the value of the parameter passed to this function
    and
    {status} is 'has started' if the value of the parameter 'value' is 0
    {status} is 'is in progress ({value}% completed)' if the value of the parameter 'value' is between,
    but not including, 0 and 100
    {status} is 'has completed' if the value of the parameter 'value' is 100

    :param operation: a string indicating the operation being started
    :param value: an integer indicating the amount of progress made
    :return: does not return anything
    """
    # TODO: Your code here
    pass


def menu(variant=0):
    """
    Task 4: Display a menu of options and read the user's response.

    If no value or a zero is supplied for the parameter 'variant' then a menu with the following options
    should be displayed:

    '[1] Process Data', '[2] Visualise Data', '[3] Export Data' and '[4] Exit'

    If the value of the parameter 'variant' is 1 then a menu with the following options should be displayed:

    '[1] Record by Serial Number', '[2] Records by Observation Date', '[3] Group Records by Country/Region,
    '[4] Summarise Records'

    If the value of the parameter 'variant' is 2 then a menu with the following options should be displayed:

    '[1] Country/Region Pie Chart', '[2] Observations Chart', '[3] Animated Summary'

    If the value of the parameter 'variant' is 3 then a menu with the following options should be displayed:

    '[1] All Data', '[2] Data for Specific Country/Region'

    In each of the above cases, the user's response should be read in and returned as an integer
    corresponding to the selected option.
    E.g. 1 for 'Process Data', 2 for 'Visualise Data' and so on.

    If the user enters a invalid option then a suitable error message should be displayed

    :return: nothing if invalid selection otherwise an integer for a valid selection
    """
    # TODO: Your code here
   import sys
def main():
    menu()


def menu():
    print("************Menu**************")
    print()

    choice = input("""
                      1: Process Data
                      2: Visualize Data
                      3: Export Data
                      4: Exit

                      Please enter your choice: """)

    if choice == "1" or choice =="1":
        processdata()
    elif choice == "2" or choice =="2":
        visualizedata()
    elif choice=="3" or choice=="3":
        exportdata()
    elif choice=="4" or choice=="4":
        sys.exit
    else:
        print("You must only select either 1, 2, 3, 4")
        print("Please try again")
        menu()
def processdata():
    print("************Menu**************")
    print()

    choice = input("""
                      1: Record by Serial Number
                      2: Records by Observation Date
                      3: Group Records by Country/Region
                      4: Summarise Records

                      Please enter your choice: """)

    if choice == "1" or choice =="1":
        menu()
    elif choice == "2" or choice =="2":
        data()
    elif choice=="3" or choice=="3":
        data1()
    elif choice=="4" or choice=="4":
        menu()
    else:
        print("You must only select either 1, 2, 3, 4")
        print("Please try again")
        menu()
def data():
    print("************Menu**************")
    print()

    choice = input("""
                      1: Country/Region Pie Chart
                      2: Observations Chart
                      3: Animated Summary

                      Please enter your choice: """)

    if choice == "1" or choice =="1":
        menu()
    elif choice == "2" or choice =="2":
        menu()
    elif choice=="3" or choice=="3":
        sys.exit
    else:
        print("You must only select either 1,2 or 3")
        print("Please try again")
        menu()
def data1():
    print("************Menu**************")
    print()

    choice = input("""
                      1: All Data
                      2: Data for Specific Country/Region

                      Please enter your choice: """)

    if choice == "1" or choice =="1":
        menu()
    elif choice == "2" or choice =="2":
        menu()
    else:
        print("You must only select either 1 or 2")
        print("Please try again")
        menu()
main()










def total_records(num_records):
    f"""
    Task 5: Display the total number of records in the data set.
    
    The function should display a message in the following format:

    "There are {num_records} records in the data set."

    Where {num_records} is the value of the parameter passed to this function
    
    :param num_records: the total number of records in the data set
    :return: Does not return anything
    """
    # TODO: Your code here
df.shape
    def total_records(num_records):
    num_records= df.shape
total_records(0)
print("The shape of the dataset", df.shape)



def serial_number():
    """
    Task 6: Read in the serial number of a record and return the serial number.

    The function should ask the user to enter a serial number for a record e.g. 189
    The function should then read in and return the user's response as an integer.

    :return: the serial number for a record
    """
    # TODO: Your code here
 def serial_number(serial):
    serial=df['SNo']
    serial_number(0)

print (serial)




def observation_dates():
    """
    Task 7: Read in and return a list of observation dates.

    The function should ask the user to enter some observation dates
    This should be entered in the format dd/mm/yyyy where dd is two-digit day, mm is two digit month and yyyy is
    a four digit year e.g. 01/22/2020
    The function should return a list containing the specified observation dates.

    :return: a list of observation dates
    """
    # TODO: Your code here
   y= input("enter date")
def observation_dates(x):
    import datetime
    x = datetime.datetime('y').date()
    print (x)
    df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
    df['ObservationDate']
    mask = df[(df['ObservationDate'] >= x) & (df['ObservationDate'] <= x)]
    print(mask)








def display_record(record, cols=None):
    """
    Task 8: Display a record. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the record will be displayed.

    The parameter record is a list of values e.g. [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    The parameter cols is a list of column indexes e.g. [0,3,5]
    The function should display a list of values.
    The displayed list should only consist of those values whose column index is in cols.

    E.g. if cols is [1,3] then for the record [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    the following should be displayed:
    ['01/22/2020','Mainland China']

    E.g. if cols is [0,1,4] then for the record [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]
    the following should be displayed:
    [1,'01/22/2020','1/22/2020 17:00']

    E.g. if cols is an empty list or None then all the values will be displayed
    [1,'01/22/2020','Anhui','Mainland China','1/22/2020 17:00',1,0,0]

    :param record: A list of data values for a record
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here
  result = df.loc[:0]

def display_record(record, cols=None):
    record = df.loc[:0]






def display_records():
    """
    Task 9: Display each record in the specified list of records.
    Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for a record will be displayed.

    The function should have two parameters as follows:

    records     which is a list of records where each record itself is a list of data values.
    cols        this is a list of integer values that represent column indexes.
                the default value for this is None.

    You will need to add these parameters to the function definition.

    The function should iterate through each record in records and display the record.

    Each record should be displayed as a list of values e.g. [1,01/22/2020,Anhui,Mainland China,1/22/2020 17:00,1,0,0]
    Only the columns whose indexes are included in cols should be displayed for each record.

    If cols is an empty list or None then all values for the record should be displayed.

    :param records: A list of records
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here

x=df.loc[2:3]
def display_records(x):
    x=df.loc[2:3]


