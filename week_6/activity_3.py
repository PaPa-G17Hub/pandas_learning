# Download the script internet_speed_test.py and install the speedtest-cli library.
###############################################
#         pip install speedtest-cli
###############################################
# Run internet_speed_test.py
# This will repeatedly check your download and upload speeds for around 20 minutes and create a dataframe.

# Find out:
# Internet Service Provider
# Package (if known)
# Fastest Download
# Slowest Download
# Mean Download
# Median Download
# Fastest Upload
# Slowest Upload
# Mean Upload
# Median Upload

import pandas as pd

speed_data_df = pd.read_excel("results2024-10-24-1553.xlsx")
# print(speed_data_df.info())

print(f"\nFastest Download = {speed_data_df['Download (Mb/s)'].max():.2f}")
print(f"\nSlowest Download = {speed_data_df['Download (Mb/s)'].min():.2f}")
print(f"\nMean Download Speed = {speed_data_df['Download (Mb/s)'].mean():.2f}")
print(f"\nMedian Download Speed = {speed_data_df['Download (Mb/s)'].median():.2f}")
print(f"\nFastest Upload = {speed_data_df['Upload (Mb/s)'].max():.2f}")
print(f"\nSlowest Upload = {speed_data_df['Upload (Mb/s)'].min():.2f}")
print(f"\nMean Upload Speed = {speed_data_df['Upload (Mb/s)'].mean():.2f}")
print(f"\nMedian Upload Speed = {speed_data_df['Upload (Mb/s)'].median():.2f}")

# 1. Sort your data by fastest upload speed.
print("\n1. Sort your data by fastest upload speed.")
print(speed_data_df.sort_values(by=['Upload (Mb/s)'], ascending=False))
# 2. Re-sort it by slowest upload speed.
print("\n2. Re-sort it by slowest upload speed.")
print(speed_data_df.sort_values(by=['Upload (Mb/s)'], ascending=True))
# 3. Return download speeds which are faster than the mean.
print(f"\nMean Download Speed = {speed_data_df['Download (Mb/s)'].mean():.2f}")
print("\n3. Return download speeds which are faster than the mean.")
print(speed_data_df[speed_data_df['Download (Mb/s)'] > speed_data_df['Download (Mb/s)'].mean()])
# 3. Return download speeds which are slower than the mean.
print(f"\nMean Download Speed = {speed_data_df['Download (Mb/s)'].mean():.2f}")
print("\n3. Return download speeds which are slower than the mean.")
print(speed_data_df[speed_data_df['Download (Mb/s)'] < speed_data_df['Download (Mb/s)'].mean()])