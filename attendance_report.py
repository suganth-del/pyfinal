
import pandas as pd

# Load the attendance CSV file
df = pd.read_csv("attendance.csv")

# Group by student and count status
summary = df.groupby(['Student Name', 'Status']).size().unstack(fill_value=0)

# Fill missing columns if needed
if 'Present' not in summary.columns:
    summary['Present'] = 0
if 'Absent' not in summary.columns:
    summary['Absent'] = 0

# Save the summary to a new CSV
summary_path = "attendance_summary.csv"
summary.to_csv(summary_path)

# Also print the summary in a readable format
print("Attendance Summary:")
print(summary)
