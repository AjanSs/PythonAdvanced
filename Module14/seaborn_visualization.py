import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('avgIQpercountry.csv', thousands=',')

print(df.info())

plt.figure(figsize=(10, 6))
sns.histplot(df['Average IQ'], bins=20, kde=True)
plt.title('Histogram of Average IQ')
plt.xlabel('Average IQ')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

numeric_data = df.select_dtypes(include=['number'])

plt.figure(figsize=(10, 6))
sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.set_style('darkgrid')
sns.boxplot(data=df, x='Continent', y='Average IQ')
plt.title('Boxplot of Average IQ by Continent')
plt.xlabel('Continent')
plt.ylabel('Average IQ')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()