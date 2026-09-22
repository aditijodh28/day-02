import json
import os


FILE_NAME = "employees.json"


# Load Employees

def load_employees():

    try:

        if not os.path.exists(FILE_NAME):
            return []

        with open(FILE_NAME, "r") as file:

            return json.load(file)

    except json.JSONDecodeError:

        print("Invalid JSON file.")

        return []


# Save Employees

def save_employees(employees):

    with open(FILE_NAME, "w") as file:

        json.dump(
            employees,
            file,
            indent=4
        )


# Add Employee

def add_employee(employees):

    try:

        employee_id = int(
            input("Enter employee ID: ")
        )

        # Check duplicate ID
        for employee in employees:

            if employee["id"] == employee_id:

                print("Employee ID already exists.")

                return

        name = input("Enter employee name: ")

        salary = float(
            input("Enter salary: ")
        )

        if salary <= 0:

            print("Salary must be greater than 0.")

            return

        department = input(
            "Enter department: "
        )

        employee = {

            "id": employee_id,

            "name": name,

            "salary": salary,

            "department": department
        }

        employees.append(employee)

        save_employees(employees)

        print(
            "Employee added successfully."
        )

    except ValueError:

        print(
            "Please enter valid numeric values."
        )


# Update Employee

def update_employee(employees):

    try:

        employee_id = int(
            input(
                "Enter employee ID to update: "
            )
        )

        for employee in employees:

            if employee["id"] == employee_id:

                name = input(
                    "Enter new name: "
                )

                salary = float(
                    input(
                        "Enter new salary: "
                    )
                )

                if salary <= 0:

                    print(
                        "Salary must be greater than 0."
                    )

                    return

                department = input(
                    "Enter new department: "
                )

                employee["name"] = name

                employee["salary"] = salary

                employee["department"] = department

                save_employees(employees)

                print(
                    "Employee updated successfully."
                )

                return

        print("Employee not found.")

    except ValueError:

        print("Invalid input.")


# Delete Employee

def delete_employee(employees):

    try:

        employee_id = int(
            input(
                "Enter employee ID to delete: "
            )
        )

        for employee in employees:

            if employee["id"] == employee_id:

                employees.remove(employee)

                save_employees(employees)

                print(
                    "Employee deleted successfully."
                )

                return

        print("Employee not found.")

    except ValueError:

        print("Invalid employee ID.")


# Search Employee

def search_employee(employees):

    keyword = input(
        "Enter employee name: "
    ).lower()

    found = False

    for employee in employees:

        if keyword in employee["name"].lower():

            print_employee(employee)

            found = True

    if not found:

        print("Employee not found.")


# Filter by Department

def filter_department(employees):

    department = input(
        "Enter department: "
    ).lower()

    results = [

        employee

        for employee in employees

        if employee["department"].lower()
        == department
    ]

    if not results:

        print(
            "No employees found."
        )

        return

    for employee in results:

        print_employee(employee)


# Sort Employees

def sort_employees(employees):

    print("\nSort Options")

    print("1. Salary Low to High")
    print("2. Salary High to Low")
    print("3. Name A-Z")

    choice = input(
        "Enter choice: "
    )

    if choice == "1":

        results = sorted(
            employees,
            key=lambda employee:
            employee["salary"]
        )

    elif choice == "2":

        results = sorted(
            employees,
            key=lambda employee:
            employee["salary"],
            reverse=True
        )

    elif choice == "3":

        results = sorted(
            employees,
            key=lambda employee:
            employee["name"].lower()
        )

    else:

        print("Invalid choice.")

        return

    for employee in results:

        print_employee(employee)


# Statistics

def statistics(employees):

    if not employees:

        print("No employees available.")

        return

    total_employees = len(employees)

    total_salary = sum(
        employee["salary"]
        for employee in employees
    )

    average_salary = (
        total_salary / total_employees
    )

    highest = max(
        employees,
        key=lambda employee:
        employee["salary"]
    )

    lowest = min(
        employees,
        key=lambda employee:
        employee["salary"]
    )

    departments = {}

    for employee in employees:

        department = employee["department"]

        departments[department] = (
            departments.get(department, 0) + 1
        )

    print("\n========== STATISTICS ==========")

    print(
        "Total Employees:",
        total_employees
    )

    print(
        "Total Salary:",
        total_salary
    )

    print(
        "Average Salary:",
        round(average_salary, 2)
    )

    print("\nHighest Salary:")

    print_employee(highest)

    print("\nLowest Salary:")

    print_employee(lowest)

    print("\nEmployees by Department:")

    for department, count in departments.items():

        print(
            department,
            ":",
            count
        )


# List Employees

def list_employees(employees):

    if not employees:

        print("No employees available.")

        return

    for employee in employees:

        print_employee(employee)


# Display Employee

def print_employee(employee):

    print("--------------------------------")

    print(
        "ID:",
        employee["id"]
    )

    print(
        "Name:",
        employee["name"]
    )

    print(
        "Salary:",
        employee["salary"]
    )

    print(
        "Department:",
        employee["department"]
    )

    print("--------------------------------")


# Main Menu

def main():

    employees = load_employees()

    while True:

        print("\n====================================")

        print(
            "      EMPLOYEE MANAGEMENT SYSTEM"
        )

        print("====================================")

        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. Filter by Department")
        print("6. Sort Employees")
        print("7. Statistics")
        print("8. List Employees")
        print("9. Exit")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            add_employee(employees)

        elif choice == "2":

            update_employee(employees)

        elif choice == "3":

            delete_employee(employees)

        elif choice == "4":

            search_employee(employees)

        elif choice == "5":

            filter_department(employees)

        elif choice == "6":

            sort_employees(employees)

        elif choice == "7":

            statistics(employees)

        elif choice == "8":

            list_employees(employees)

        elif choice == "9":

            print(
                "Thank you for using the system!"
            )

            break

        else:

            print(
                "Invalid choice."
            )


if __name__ == "__main__":

    main()