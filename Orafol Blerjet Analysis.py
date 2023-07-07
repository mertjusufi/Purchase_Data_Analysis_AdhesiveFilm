import pandas as pd

# Load the data
df_sales = pd.read_excel('C:\\Users\\Lenovo\\Downloads\\Documents\\blerjet orafol.xlsx')
df_purchases = pd.read_excel('C:\\Users\\Lenovo\\Downloads\\Documents\\blerjet orafol.xlsx')

# Take a look at the first few rows of the data
print(df_sales.head())
print(df_purchases.head())

print("---------------------------------------------------------")
#################################################################################################################


print ("TOP AND BOTTOM PRODUCTS ")
# Top 10 products in terms of purchase
top_purchases = df_sales.groupby('Emërtimi')['Sasia'].sum().sort_values(ascending=False).head(11)
print(top_purchases)

# Bottom 10 products in terms of purchases
bottom_purchases = df_sales.groupby('Emërtimi')['Sasia'].sum().sort_values().head(11)
print(bottom_purchases)

print("---------------------------------------------------------")


############################################################################################################################

"""

print("Quantiles")
# Quantiles of the data
print(df_sales['Sasia'].quantile([0.25, 0.5, 0.75]))
 

print("Statistics")
# Mean sales
mean_sales = df_sales['Sasia'].mean()
print(f"Mean Purchases: {mean_sales}")

# Median sales
median_sales = df_sales['Sasia'].median()
print(f"Median Purchases: {median_sales}")

# Mode sales
mode_sales = df_sales['Sasia'].mode()
print(f"Mode Purchases: {mode_sales}")

# Standard deviation of sales
std_sales = df_sales['Sasia'].std()
print(f"Standard Deviation of Purchases: {std_sales}")

# Variance of sales
var_sales = df_sales['Sasia'].var()
print(f"Variance of Purchases: {var_sales}")

# Minimum sales
min_sales = df_sales['Sasia'].min()
print(f"Minimum Purchases: {min_sales}")

# Maximum sales
max_sales = df_sales['Sasia'].max()
print(f"Maximum Purchases: {max_sales}")

"""
#######################################################################################################################################

# Descriptive statistics
print(df_sales['Sasia'].describe())
print("---------------------------------------------------------")

#######################################################################################################################################

print("Sales Concetration")
# Sales Concetration 
total_sales = df_sales['Sasia'].sum()
top_10_sales = df_sales.groupby('Emërtimi')['Sasia'].sum().sort_values(ascending=False).head(10).sum()
sales_concentration = (top_10_sales / total_sales) * 100
print(f"Top 10 products account for {sales_concentration}% of total purchases.")

print("---------------------------------------------------------")
#######################################################################################################################################
"""
import matplotlib.pyplot as plt

plt.boxplot(df_sales['Sasia'])
plt.show()





# Calculating standard deviation for each product
product_variability = df_sales.groupby('Emërtimi')['Sasia'].std().reset_index()

# Sorting by variability
product_variability.sort_values(by='Sasia', ascending=False, inplace=True)
print(product_variability)


"""
#######################################################################################################################################



# Sort products by their total order quantity
df_sorted = df_sales.sort_values('Sasia', ascending=False)

# Calculate cumulative sum
df_sorted['Cumulative Sum'] = df_sorted['Sasia'].cumsum()

# Calculate cumulative percentage
df_sorted['Cumulative Percentage'] = 100 * df_sorted['Cumulative Sum'] / df_sorted['Sasia'].sum()

# Classify into ABC
df_sorted['ABC'] = pd.cut(df_sorted['Cumulative Percentage'], bins=[0, 80, 95, 100], labels=['A', 'B', 'C'])

print(df_sorted)

print("---------------------------------------------------------")

#######################################################################################################################################

# Calculate the z-score for each product's order quantity
df_sales['z_score'] = (df_sales['Sasia'] - df_sales['Sasia'].mean()) / df_sales['Sasia'].std()

# Define outliers as products with a z-score greater than 3 or less than -3
df_outliers = df_sales[(df_sales['z_score'] > 2) | (df_sales['z_score'] < -2)]
print(df_outliers)

print("---------------------------------------------------------")

#######################################################################################################################################


# Define thresholds for fast and slow moving items
threshold_fast = df_sales['Sasia'].quantile(0.75)
threshold_slow = df_sales['Sasia'].quantile(0.25)

# Identify fast moving items
df_fast = df_sales[df_sales['Sasia'] >= threshold_fast]

# Identify slow moving items
df_slow = df_sales[df_sales['Sasia'] <= threshold_slow]

print(df_fast)
print(df_slow)

print("---------------------------------------------------------")

#######################################################################################################################

import matplotlib.pyplot as plt
import seaborn as sns

# sort dataframe based on 'Sasia' column
df_sorted = df_sales.sort_values('Sasia', ascending=False)

# take top 10 fast moving and slow moving items
fast_moving = df_sorted.head(10)
slow_moving = df_sorted.tail(10)

# plot
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.barplot(x = fast_moving['Emërtimi'], y = fast_moving['Sasia'])
plt.title('Fast Moving Items')
plt.xticks(rotation=90)

plt.subplot(1, 2, 2)
sns.barplot(x = slow_moving['Emërtimi'], y = slow_moving['Sasia'])
plt.title('Slow Moving Items')
plt.xticks(rotation=90)

plt.tight_layout()
plt.show()



