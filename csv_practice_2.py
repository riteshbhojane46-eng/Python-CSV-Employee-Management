import csv

with open("employee.csv", "w", newline="") as file:

    fieldnames = ["Name","Salary","Dept"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()

    
    writer.writerow({
        "Name" : "Rahul",
        "Salary" : 25000,
        "Dept" : "IT"
    })

    writer.writerow({
            "Name" : "Priya",
            "Salary" : 30000,
            "Dept" : "HR"
        })

    writer.writerow({
                "Name" : "Amit",
                "Salary" : 30000,
                "Dept" : "Finance"
            })


print("Data Saved Successfully !")

with open ("employee.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)