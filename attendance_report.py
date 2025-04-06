import csv  # using csv module to work with csv files

# making a dictionary to keep track of how many times each student was present or absent
attendance = {}

# opening the attendance file
with open("attendance.csv", "r") as file:
    reader = csv.DictReader(file)  # this reads the file with column names

    # looping through each row to count attendance
    for row in reader:
        name = row["Student Name"]
        status = row["Status"]

        # if student not already added, we create a slot for them
        if name not in attendance:
            attendance[name] = {"Present": 0, "Absent": 0}

        # now we check status and add to the right count
        if status == "Present":
            attendance[name]["Present"] += 1
        elif status == "Absent":
            attendance[name]["Absent"] += 1

# now we write the result into a new file
with open("attendance_summary.csv", "w", newline="") as file:
    fieldnames = ["Student Name", "Present", "Absent"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    # writing each student's summary
    for name, data in attendance.items():
        writer.writerow({
            "Student Name": name,
            "Present": data["Present"],
            "Absent": data["Absent"]
        })

# also print the summary so I can see it quickly in terminal
print("Here’s the final attendance count:")
for name, data in attendance.items():
    print(f"{name} => Present: {data['Present']} | Absent: {data['Absent']}")
