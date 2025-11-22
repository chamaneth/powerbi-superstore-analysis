import pandas as pd
import kagglehub
import os

# Download dataset from Kaggle
path = kagglehub.dataset_download("apoorvaappz/global-super-store-dataset")
print("Path to dataset files:", path)

# Show files
print(os.listdir(path))

# Load the CSV file
df = pd.read_csv(f"{path}/Global_Superstore2.csv", encoding='latin1')

# ---------- DATA CLEANING ----------

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Convert number columns
df['Quantity'] = df['Quantity'].astype(int)
df['Sales'] = df['Sales'].astype(float)
df['Profit'] = df['Profit'].astype(float)
df['Discount'] = df['Discount'].astype(float)

# Create Total Sales (Quantity × Sales per unit)
df['TotalSales'] = df['Quantity'] * df['Sales']

# Save cleaned dataset
df.to_csv("cleaned_superstore.csv", index=False)

print("Cleaned dataset saved as cleaned_superstore.csv")
