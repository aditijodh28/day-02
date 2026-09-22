import csv

FILE_NAME = r"C:\Users\Yashraj\Downloads\PugArch-Internship\day-02\csv-analysis\employees.csv"

employees = []

# Read CSV
with open(FILE_NAME, "r", encoding="utf-8-sig", newline="") as file:

    reader = csv.DictReader(file)

    for row in reader:

        row["id"] = int(row["id"])
        row["salary"] = float(row["salary"])

        employees.append(row)


# Record Count
print("Record Count:", len(employees))


# Salaries
salaries = [
    employee["salary"]
    for employee in employees
]

print("Average Salary:", sum(salaries) / len(salaries))
print("Minimum Salary:", min(salaries))
print("Maximum Salary:", max(salaries))


# Department Statistics
department_count = {}

for employee in employees:

    department = employee["department"]

    department_count[department] = (
        department_count.get(department, 0) + 1
    )


print("\nEmployees by Department:")

for department, count in department_count.items():

    print(department, ":", count)


# Duplicate IDs
ids = [
    employee["id"]
    for employee in employees
]

duplicates = []

for employee_id in ids:

    if ids.count(employee_id) > 1:

        if employee_id not in duplicates:

            duplicates.append(employee_id)


print("\nDuplicate IDs:", duplicates)