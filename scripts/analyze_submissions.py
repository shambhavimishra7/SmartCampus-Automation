import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../data/attendance_updated.csv')

# Homework submission rate
submission_rate = data['HomeworkSubmitted'].mean() * 100
print(f"Homework Submission Rate: {submission_rate:.2f}%")

# Plot homework submission status
data['HomeworkSubmitted'].value_counts().plot(kind='bar', title='Homework Submission Status')
plt.savefig('../visuals/report_sample.png')
plt.show()
 
