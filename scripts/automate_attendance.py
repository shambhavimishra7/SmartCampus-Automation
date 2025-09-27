import pandas as pd

# Load sample data
data = pd.read_csv('../data/sample_student_data.csv')

# Mark attendance
data['AttendanceStatus'] = data['Attendance'].apply(lambda x: 'Present' if x==1 else 'Absent')

# Simulate notifications
for idx, row in data.iterrows():
    if row['AttendanceStatus'] == 'Absent':
        print(f"Notification: Reminder sent to {row['Name']} for attendance/homework.")

# Save updated data
data.to_csv('../data/attendance_updated.csv', index=False)
print("Attendance update complete!")
