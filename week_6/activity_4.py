# Create a short presentation informing us of the average internet speed of the cohort.
# How does this compare to the national average?

import pandas as pd
import matplotlib.pyplot as plt

speed_data_df = pd.read_excel("group_results.xlsx")
# print(speed_data_df.info())
print("\nDropped the unnecesary column")
speed_data_df = speed_data_df.drop(columns=["Package (if known)"])

print(f"\nFastest Download = {speed_data_df['Fastest Download'].max():.2f}")
print(f"Slowest Download = {speed_data_df['Slowest Download'].min():.2f}")
print(f"\nMean Download Speed = {speed_data_df['Mean Download'].mean():.2f}")
print(f"Median Download Speed = {speed_data_df['Median Download'].median():.2f}")
print(f"\nFastest Upload = {speed_data_df['Fastest Upload'].max():.2f}")
print(f"Slowest Upload = {speed_data_df['Slowest Upload'].min():.2f}")
print(f"\nMean Upload Speed = {speed_data_df['Mean Upload'].mean():.2f}")
print(f"Median Upload Speed = {speed_data_df['Median Upload'].median():.2f}")

# 1. Sort your data by fastest upload speed.
print("\n1. Sort your data by fastest upload speed.")
print(speed_data_df.sort_values(by=['Fastest Upload'], ascending=False))
# 2. Re-sort it by slowest upload speed.
print("\n2. Re-sort it by slowest upload speed.")
print(speed_data_df.sort_values(by=['Fastest Upload'], ascending=True))
# 3. Return download speeds which are faster than the mean.
print(f"\nMean Download Speed = {speed_data_df['Mean Download'].mean():.2f}")
print("\n3. Return download speeds which are faster than the mean.")
print(speed_data_df[speed_data_df['Mean Download'] > speed_data_df['Mean Download'].mean()])
# 4. Return download speeds which are slower than the mean.
print(f"\nMean Download Speed = {speed_data_df['Mean Download'].mean():.2f}")
print("\n3. Return download speeds which are slower than the mean.")
print(speed_data_df[speed_data_df['Mean Download'] < speed_data_df['Mean Download'].mean()])

national_median_average_download_speed = 69.4
national_median_average_upload_speed = 18.4

# 5. Return download speeds which are faster than the national_median_average_download_speed .
print(f"\nThe latest UK broadband statistics from Ofcom found that the median average download speed in the UK was 69.4Mbps, as of March 2023. The Cohort's Mean Download Speed is {speed_data_df['Mean Download'].mean():.2f}Mbps")
print("5. Table showing download speeds which are faster than the national median average download speed.")
print(speed_data_df[speed_data_df['Mean Download'] > national_median_average_download_speed])
print("\n  Table showing download speeds which are slower than the national median average download speed.")
print(speed_data_df[speed_data_df['Mean Download'] < national_median_average_download_speed])

# 6. Return upload speeds which are faster than the national_median_average_upload_speed.
print(f"\nThe median average upload speed in the UK over this period was 18.4Mbps. The cohorts Mean Upload Speed is {speed_data_df['Mean Upload'].mean():.2f}Mbps")
print("6. Table showing upload speeds which are faster than the national median average upload speed.")
print(speed_data_df[speed_data_df['Mean Upload'] > national_median_average_upload_speed])
print("\n Table showing upload speeds which are slower than the national median average upload speed.")
print(speed_data_df[speed_data_df['Mean Upload'] < national_median_average_upload_speed])

fastest_speed_data_df = speed_data_df.sort_values(by="Fastest Download", ascending=True)
fastest_speed_data_df.plot(kind='scatter',
        x='Fastest Download',
        y='Internet Service Provider',
        color='red')

# set the title
plt.title('ScatterPlot')

# show the plot
plt.show()