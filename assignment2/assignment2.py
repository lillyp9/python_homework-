import csv
import traceback
import os
import custom_module
from datetime import datetime

def read_employees():
    dict = {}
    rows =[]
    try:
        with open('../csv/employees.csv', 'r') as file:
             reader = csv.reader(file)
             first_row = True
             for row in reader:
                if first_row ==True:
                  dict["fields"] = row
                  first_row = False
                else:
                  rows.append(row)
        dict["rows"] = rows
        return dict  
    except Exception as e:
        print(e)
        return{}
employees = read_employees()
print(employees)

#Task 3
def column_index (name):
    
        fields = employees["fields"]
        index = fields.index(name)
        return index
  
employee_id_column = column_index("employee_id")
print(employee_id_column)
     

#Task 4 
def first_name(row_number):
        index = column_index("first_name")
        row = employees["rows"][row_number]
        value = row[index]
        return value
print(first_name(3))    
        
        
#Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

#Task 6

def employee_find_2(employee_id):
     matches = list(filter(lambda row: int(row[employee_id_column])== employee_id , employees["rows"]))
     return matches
print(employee_find_2(3))

#Task 7 
def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])
    return employees["rows"]
print(sort_by_last_name())

#Task 8 
def employee_dict(row):
   
    fields = employees["fields"][1:]
    values = row[1:]
    return dict(zip(fields, values))
print(employee_dict)

#Task 9
def all_employees_dict():
   all_dict = {}
   for row in employees["rows"]:
    employee_id = row[0]
    info = employee_dict(row)
    all_dict[employee_id] = info
   return all_dict
print(all_employees_dict)

#Task 10
def get_this_value():
    return os.getenv("THISVALUE")

#Task 11
def set_that_secret(chocolate):
    custom_module.set_secret(chocolate)
    
print(custom_module.secret)

#Task 12
def read_minutes():
    minutes1_box={}
    rows1_list= []
    with open('../csv/minutes1.csv', 'r') as file:
         reader = csv.reader(file)
         first_row = True
         for row in reader:
             if first_row == True:
              minutes1_box["fields"] = row 
              first_row = False
             else:
                row_tuple = tuple(row)
                rows1_list.append(row_tuple)
    minutes1_box["rows"] = rows1_list
  
    minutes2_box={}
    rows2_list= []
    
    with open('../csv/minutes2.csv', 'r') as file:
         reader = csv.reader(file)
         first_row = True
         for row in reader:
             if first_row == True:
              minutes2_box["fields"] = row 
              first_row = False
             else:
               row_tuple = tuple(row)
               rows2_list.append(row_tuple)
    minutes2_box["rows"] = rows2_list
    
    return minutes1_box , minutes2_box

minutes1, minutes2 = read_minutes()

#Task 13
def create_minutes_set ():
    set1 = ()
    set2 = ()
    minutes1_row = minutes1["rows"]
    set1 = set(minutes1_row)
    minutes2_row = minutes2["rows"]
    set2 = set(minutes2_row)
    union = set1 | set2
    return union
minutes_set = create_minutes_set()

#Task 14 
def create_minutes_list():
    
    converted_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
    return converted_list
minutes_list= create_minutes_list()

#Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1]) 
    converted_data =  [(x[0], x[1].strftime("%B %d, %Y")) for x in minutes_list]
    with open('./minutes.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(minutes1["fields"])
      for row in converted_data:
       writer.writerow(row) 
    return converted_data
     
                          
 

    
   
    
    
                  
          
       
    

