import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data Loading (Pandas)
df = pd.read_csv("Fashion Dataset.csv")


# Data Inspection (Pandas)

# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.shape)
# print(df.columns)


# Data Cleaning (Pandas)

df.drop("Unnamed: 0", axis=1,inplace=True)
df.dropna(subset=["p_id", "name", "price", "brand"],inplace=True)
df["colour"] = df["colour"].fillna("Unknown")
df["ratingCount"] = df["ratingCount"].fillna(0)
df["avg_rating"] = df["avg_rating"].fillna(0)

# print(df.isnull().sum())
# print(df.shape)


# Statistical Analysis (Numpy Operation)

print("Here are the some Information about Myntra Dataset :- \n ")
avg_price = np.mean(df["price"])
print(f"Average Price of Products :- {avg_price:.2f} Rs \n ")
max_price = np.max(df["price"])
print(f"Maximum Price of Products :- {max_price:.2f} Rs \n ")
min_price = np.min(df["price"])
print(f"Minimum Price of Products :- {min_price:.2f} Rs \n ")
median_price = np.median(df["price"])
print(f"Median Price of Products :- {median_price:.2f} Rs \n ")
std_price = np.std(df["price"])
print(f"Standard Deviation Price of Products :- {std_price:.2f} Rs \n ")



# Creating New Features (Numpy + Pandas)

# Price Category :-
price_category = df["price_category"] = np.where(df["price"] > avg_price, "Premium", "Budget")
# print(df["price_category"])

# Rating Category :-
rating_category = df["rating_category"] = np.where(df["avg_rating"] >= 4, "High Rated", "Low Rated")
# print(df["rating_category"])





# Graphs :- 


# plt.figure(figsize=(13,10))

# Brand Analysis (Pandas + Matplotlib)
top_brands = df["brand"].value_counts().head(10)

plt.figure(figsize=(10,5))
# plt.subplot(3,2,1)
plt.bar(top_brands.index, top_brands.values)
plt.title("Top 10 Brands on Myntra")
plt.xlabel('Brands')
plt.ylabel("Number of Products")
plt.xticks(rotation=15)

# plt.savefig("top_brands.jpg")



# Top 10 Colors 
top_colors = df["colour"].value_counts().head(10)

plt.figure(figsize=(10,5))
# plt.subplot(3,2,2)
plt.bar(top_colors.index, top_colors.values, color="aqua")
plt.title("Top 10 Product Colors")
plt.xlabel("Colors")
plt.ylabel("Count")
plt.xticks(rotation=15)

# plt.savefig("top_color_Graph.jpg")



# Price Distribution
plt.figure(figsize=(8,5))
# plt.subplot(3,2,3)
plt.hist(df["price"], bins=20)
plt.title("Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Products")

# plt.savefig("Price_Distribution_Graph.jpg")



# Rating Distribution 
plt.figure(figsize=(8,5))
# plt.subplot(3,2,4)
plt.hist(df["avg_rating"], bins=10, color="lime")
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Products")

# plt.savefig("Rating_Distribution_Graph.jpg")



# Price vs Rating 
plt.figure(figsize=(8,5))
# plt.subplot(3,2,5)
plt.scatter(df["price"], df["avg_rating"], color="red")
plt.title("Price vs Rating")
plt.xlabel("Price")
plt.ylabel("Average Rating")

# plt.savefig("Scatter_Graph.jpg")



# Premium vs Budget Product Distribution
plt.figure(figsize=(6,6))
# plt.subplot(3,2,6)
price_count = df["price_category"].value_counts()

plt.pie(price_count.values, labels=price_count.index, autopct="%1.1f%%")
plt.title("Premium vs Budget Products")

# plt.savefig("pie_chart_graph.jpg")



plt.tight_layout()
# plt.savefig("Myntra_Dashboard.jpg")
# plt.show()