import pandas as pd

data = pd.read_csv('../data/attendance_updated.csv')

summary = f"""
Weekly Module Summary:
Total Students: {len(data)}
Homework Submission Rate: {data['HomeworkSubmitted'].mean()*100:.2f}%
Students Absent This Week: {len(data[data['Attendance']==0])}
"""
print(summary)
 
