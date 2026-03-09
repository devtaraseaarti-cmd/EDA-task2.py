import pandas as pd
import matplotlib.pyplot as plt

# dataset load
data = pd.read_csv("ultimate_student_productivity_dataset_5000.csv")

# first rows
print(data.head())

# dataset info
print(data.info())

# statistical summary
print(data.describe())

# missing values
print(data.isnull().sum())

# correlation
print(data.corr(numeric_only=True))

# Scatter Plot
plt.scatter(data['study_hours'], data['exam_score'])
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score")
plt.show()

# Bar Graph
sample_data = data.head(15)
sample_data.plot(kind='bar')
plt.show()

# Pie Chart
top_data = data['study_hours'].value_counts().head(6)
plt.pie(top_data, labels=top_data.index, autopct='%1.1f%%')
plt.show()