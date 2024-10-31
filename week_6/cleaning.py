import pandas as pd

df = pd.read_excel("first_hour_sales.xlsx")

# print the entire dataframe
print(df)

print("Printing df.describe")
print(df.describe)

print("Printing df.info()")
print(df.info())

print("\nSet the index to the Transaction ID")
df = df.set_index("Transaction ID")

print('''\nThe Till ID column does not change and therefore cannot be used for analysis.
We can remove unnecessary columns using the follwing methods\n
df = df.drop("Till ID", axis=1)
# or
df = df.drop(columns=["Till ID"])''')
df = df.drop(columns=["Till ID"])
print(df)

print("\nWe can drop a row by targetting specific row with the TRANSACTION ID value")
df = df.drop([6.0])
print(df)

print('''\nRemoving rows with NAN values is performed by the dropna() method. 
      \nThe how argument specifies how strict we want to be.
 "all" - all the values need to be NAN
 "any" - any of the values can be NAN''')
df = df.dropna(how="any")
print(df)

print('''\nFinding duplicates using the df.duplicated() method ''')
print(df[df.duplicated()])

print('''\nDropping duplicates using the drop_duplicates() method ''')
df = df.drop_duplicates()
print(df)

print('''\nOutliers
      
Using the df.at[] property we can change specific values
      \ndf.at[15.0,"Cost"] = 6.00
      ''')

df.at[15.0,"Cost"] = 6.00
print(df)


print('''\nColumn wide cleaning
\nOur data has a Time column stored as a float.
We can make better use of this column when stored as a datetime type   
Use the apply method with a float_to_time function to accomplish this
''')
def float_to_time(float_time_record):
    # cast float to string
    str_time_record = str(float_time_record)
    # split this string on the decimal point value
    time_record_hours, time_record_minutes = str_time_record.split(".")
    #format the time with leading zeros where necessary into the HH:MM format
    #using f strings we cast the string to an int and use :02 to provide any leading zeros
    timestamp = f"{int(time_record_hours):02}:{int(time_record_minutes):02}"
    return timestamp

df["Time"] = df["Time"].apply(float_to_time)
print("Show the output of the float_to_time function, as an object datatype")
print(df["Time"])
print("To convert to a datetime type we use the to_datetime() method")
df["Time"] = pd.to_datetime(df["Time"])
print(df["Time"])
print(df)

def split_basket(basket_items):
    items = basket_items.split(",")
    stripped_items = [item.strip() for item in items]
    return stripped_items

df["Basket"] = df["Basket"].apply(split_basket)
print(df["Basket"])

print("\nTo view all the items ordered we will create a new dataframe and use the explode method on the Basket column")
exploded_data = df.explode("Basket", ignore_index=False)
print(exploded_data["Basket"])