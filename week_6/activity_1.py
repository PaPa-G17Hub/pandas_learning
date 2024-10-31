# MegaBytes menu is as follows:

###########
# Drinks: #
###########
# Tea: £1.00
# Americano: £1.70
# Latte: £1.90
# Cappuccino: £1.90
# Mocha: £2.00
# Hot Chocolate: £2.20

#########
# Food: #
#########
# Croissant: £1.50
# Muffin: £2.10
# Toast: £1.00
# Panini: £2.90
# Buttered Roll: 0.70p
# Stroopwafel: 0.50p

# We have been asked to find:

# 1. The average price of an item
# 2· The average basket price
# 3. The maximum spend in one transaction
# 4. The minimum spend in one transaction
# 5. The most common spend amount
# 6. The most common payment type

import pandas as pd

# read the excel file into a panda dataframe
df = pd.read_excel("first_hour_sales.xlsx")

print("\nReplace the index with the Transaction ID")
df = df.set_index("Transaction ID")

print("\nDrop the unnecesary column")
df = df.drop(columns=["Till ID"])

print("\nDrop the rows with nonsence data")
df = df.dropna(how="any")

print("\nDrop duplicate rows")
df = df.drop_duplicates()

print("\nFix any obvious outlier data")
df.at[15.0,"Cost"] = 6.00

# Custom function to convert our time from float to object
def float_to_time(float_time_record):
    # cast float to string
    str_time_record = str(float_time_record)
    # split this string on the decimal point value
    time_record_hours, time_record_minutes = str_time_record.split(".")
    #format the time with leading zeros where necessary into the HH:MM format
    #using f strings we cast the string to an int and use :02 to provide any leading zeros
    timestamp = f"{int(time_record_hours):02}:{int(time_record_minutes):02}"
    return timestamp

# function to split a string into a list of objects
def split_basket(basket_items):
    items = basket_items.split(",")
    stripped_items = [item.strip() for item in items]
    return stripped_items

df["Basket"] = df["Basket"].apply(split_basket)

# The data is now cleaned
print(df)

# 1. The average price of an item
products = {'Tea' : 1.00,
            'Americano' : 1.70,
            'Latte' : 1.90,
            'Cappuccino' : 1.90,
            'Mocha' : 2.00,
            'Hot Chocolate' : 2.20,
            'Croissant' : 1.50,
            'Muffin' : 2.10,
            'Toast' : 1.00,
            'Panini' : 2.90,
            'Buttered Roll' : 0.70,
            'Stroopwafel' : 0.50}

# load products into a dataframe
products_df = pd.DataFrame(products.items(), columns=['Product', 'Price'])
print(f"\nThe average price of an item from the menu is £{products_df["Price"].mean():.2f}")
#print(products_df)

# 2· The average basket price
print(f"\nTotal cost of all the baskets is £{df["Cost"].sum():.2f}")
print(f"The average cost of these baskets is £{df["Cost"].mean():.2f}")

# 3. The maximum spend in one transaction
print(f"\nThe maximum spent in any single transaction was £{df["Cost"].max():.2f}")

# 4. The minimum spend in one transaction
print(f"\nThe minimum spent in any single transaction was £{df["Cost"].min():.2f}")

# 5. The most common spend amount
print(f"\nThe most frequent transaction amount was £{df["Cost"].mode()}")

# 6. The most common payment type
print(f"\nThe most common payment type was {df["Payment Method"].mode()}")