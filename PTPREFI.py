import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Medicaldataset.csv')

# Create a histogram for 'age'
plt.figure(figsize=(8, 6))
plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
plt.title('Heart Attack Patients Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.grid(True)
plt.show()

