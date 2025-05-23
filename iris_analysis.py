# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set a professional style for our plots
plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

# Task 1: Load and Explore the Dataset
print("Task 1: Loading and Exploring the Dataset")
print("-" * 50)

# Load the Iris dataset
try:
    iris = load_iris()
    
    # Create a pandas DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    
    # Add the species column
    df['species'] = [iris.target_names[i] for i in iris.target]
    
    print("Dataset loaded successfully!")
except Exception as e:
    print(f"Error loading dataset: {e}")

# Display the first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Explore the structure
print("\nDataset Structure:")
print(df.info())

# Check for missing values
print("\nChecking for missing values:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis
print("\nTask 2: Basic Data Analysis")
print("-" * 50)

# Compute basic statistics
print("Basic statistics of numerical columns:")
print(df.describe())

# Group by species and compute means
print("\nGrouping by species and computing means:")
species_means = df.groupby('species').mean()
print(species_means)

# Task 3: Data Visualization
print("\nTask 3: Data Visualization")
print("-" * 50)

# Create a figure with subplots
fig, axes = plt.subplots(2, 2, figsize=(20, 14))

# 1. Line chart showing trends
# We'll sort data to create a "trend" since Iris doesn't have time data
print("\n1. Line Chart - Sepal Length Trends by Species")
for species in iris.target_names:
    # Sort by sepal length to create a visual trend
    species_data = df[df['species'] == species].sort_values('sepal length (cm)')
    axes[0, 0].plot(range(len(species_data)), species_data['sepal length (cm)'], 
                   label=species, linewidth=2, marker='o', markersize=4)

axes[0, 0].set_title('Sepal Length Trends by Species (Sorted)', fontsize=16)
axes[0, 0].set_xlabel('Sample Index (Sorted)', fontsize=14)
axes[0, 0].set_ylabel('Sepal Length (cm)', fontsize=14)
axes[0, 0].grid(True)
axes[0, 0].legend(fontsize=12)

# 2. Bar chart showing comparison across categories
print("\n2. Bar Chart - Average Measurements by Species")
species_means.plot(kind='bar', ax=axes[0, 1], rot=0)
axes[0, 1].set_title('Average Measurements by Species', fontsize=16)
axes[0, 1].set_xlabel('Species', fontsize=14)
axes[0, 1].set_ylabel('Measurement (cm)', fontsize=14)
axes[0, 1].grid(axis='y')

# 3. Histogram of a numerical column
print("\n3. Histogram - Distribution of Petal Length")
for i, species in enumerate(iris.target_names):
    axes[1, 0].hist(df[df['species'] == species]['petal length (cm)'], 
                   bins=10, alpha=0.7, label=species)
axes[1, 0].set_title('Distribution of Petal Length by Species', fontsize=16)
axes[1, 0].set_xlabel('Petal Length (cm)', fontsize=14)
axes[1, 0].set_ylabel('Frequency', fontsize=14)
axes[1, 0].legend(fontsize=12)
axes[1, 0].grid(True)

# 4. Scatter plot to visualize relationship
print("\n4. Scatter Plot - Sepal Length vs Petal Length")
colors = ['red', 'green', 'blue']
for i, species in enumerate(iris.target_names):
    axes[1, 1].scatter(df[df['species'] == species]['sepal length (cm)'], 
                      df[df['species'] == species]['petal length (cm)'],
                      label=species, c=colors[i], alpha=0.7, s=60, edgecolor='k')
axes[1, 1].set_title('Sepal Length vs Petal Length', fontsize=16)
axes[1, 1].set_xlabel('Sepal Length (cm)', fontsize=14)
axes[1, 1].set_ylabel('Petal Length (cm)', fontsize=14)
axes[1, 1].legend(fontsize=12)
axes[1, 1].grid(True)

plt.tight_layout(pad=3.0)
plt.savefig('iris_visualizations.png', dpi=300, bbox_inches='tight')
plt.show()

# Additional visualization: Pair plot for more comprehensive view
print("\nAdditional Visualization: Pair Plot of Iris Dataset Features")
pair_plot = sns.pairplot(df, hue='species', height=2.5)
pair_plot.fig.suptitle('Pair Plot of Iris Dataset Features', y=1.02, fontsize=16)
plt.savefig('iris_pairplot.png', dpi=300, bbox_inches='tight')
plt.show()

# Findings and Observations
print("\nFindings and Observations")
print("-" * 50)
print("1. The scatter plot shows that there is a strong positive correlation between sepal length and petal length.")
print("2. From the bar chart, we can observe that Iris Setosa has the smallest average measurements for petal length and width.")
print("3. Iris Virginica generally has the largest measurements across most features.")
print("4. The histograms reveal distinct distributions for petal length, making it a good feature for species classification.")
print("5. The pair plot demonstrates that Iris Setosa is clearly separable from the other two species.")
print("6. Versicolor and Virginica show some overlap in their measurements, which might make classification challenging between these two species.")
print("7. Sepal width shows the least variation among all the features and is less useful for distinguishing between species.")