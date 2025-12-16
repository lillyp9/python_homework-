import csv
employees = []

with open("../csv/employees.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        employees.append(row)
        
employees = employees[1:]
full_names = [ row[0] + " " + row[1] for row in employees]
print(full_names)

names_with_e = [name for name in full_names if "e" in name.lower()]
print(names_with_e)
        
        