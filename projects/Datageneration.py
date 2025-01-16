
# This project demonstrates how to generate and visualize data using Python libraries.
# The program will:
# 1. Generate random data (numerical, categorical).
# 2. Perform basic manipulations on the data.
# 3. Visualize the data using Matplotlib and Seaborn.

import random 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#generate Random Numerical Data
random.seed(42)              #set seed for reproductibility
ages = [random.randint(18,60) for _ in range(100)]             #generate 100 random ages

#gerate Categorical Data into Dataframes
genders = [random.choice(['Male','Female']) for _ in range(100)]
#Combine data into DataFrame
data = pd.DataFrame({
    'Age': ages,
    "Gender": genders
})

#Add a new variable (Height)
data["Height"] =np.random.normal(loc = 170, scale = 10, size = 100).round(1)   # Normal distribution
#Add a new variable (Height)
data["Weight"] = np.random.normal(loc = 70, scale = 15, size = 100).round(1)   # Normal distribution

print("Generated Data")
print(data.head())

# Display basic statistics for the numerical columns in the data.
print("\nData Summary:")
print(data.describe())

#Visualize the data
#Histogram of ages
plt.figure(figsize =(8,5))
plt.hist(data['Age'], bins = 10, color ='skyblue',edgecolor = 'black')
plt.title('Histogram of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

#Scatter Plot of Height vs Weight
plt.figure(figsize=(8,5))
plt.scatter(data['Height'],data['Weight'],c='red',alpha=0.5)
plt.title('Height vs Weight')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()

#Boxplot of Heights by Gender
plt.figure(figsize=(8,5))
sns.boxplot(x="Gender",y="Height",data=data, palette="pastel")
plt.title("Height Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Height (cm)")
plt.show()

#Pairplot of All Numerical Variables
sns.pairplot(data, hue="Gender",palette='husl')
plt.show()

#Bar plot of Gender Counts
plt.figure(figsize=(8,5))
sns.countplot(x='Gender',data=data,palette='muted')
plt.title('Gender Count')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()