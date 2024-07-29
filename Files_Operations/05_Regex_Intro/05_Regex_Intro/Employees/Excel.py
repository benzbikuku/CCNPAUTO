import openpyxl
import re
workbook=openpyxl.load_workbook(r"/home/benz/ENTAUTO/CCNPAUTO/Files_Operations/05_Regex_Intro/05_Regex_Intro/Employees/Employees.xlsx")
print(workbook.sheetnames)
sheet1=workbook["EmployeeData"]
print(sheet1.dimensions)
#### creating a list of string from the tuples
data = list()
for row in sheet1.values:
    a,b,c,d,e,f,g=row
    data.append(f"{a};{b};{c};{d};{e};{f};{g}")
# print(data)
#### Creating a string from the tuple
string_data="\n".join(data)
# print(string_data)

### Find all the employee Names with salary between 24k and less than 30k
# result1=re.findall(r"\w+;\w+;(\w+);\w+;\d+;.+;(2[4-9]\d\d\d)",string_data)
# print(result1)
# for row in result1:
#     a,b = row
#     print(f"{a} has a salary of:  {b}")

# sheet2=workbook["Skills"]

### Find all the employee names working in IT| Marketing Dept with Last Names less than 5 caracters. 

# result1=re.findall(r"\d+;\w+;(\w{1,5});(IT|Marketing);\d+;.+;\d+",string_data)
# print(result1)
# for row in result1:
#     a,b = row
#     print(f"{a} is from :  {b} Department")

#### Find all the employees who First name start either with [p-z] and phone number starts with even digit and ends with odd digit

# result1=re.findall(r"\d+;([P-Z]\w+);\w{1,5};\w+;([2468]\d+[13579]);.+;\d+",string_data)
# print(result1)
# for row in result1:
#     a,b = row
#     print(f"{a} Phone number is :  {b}")

#### List of employees(First Name, Last Name, and Phone Number ) working in Sales department and living in New York

# result1=re.findall(r"\d{1,}?;(\w+);(\w+);Sales;(\d{1,});.+\, New York;\d{1,}",string_data)
# print(result1)
# for row in result1:
#     a,b,c = row
#     print(f"{a}  {b} Phone number is :  {c}")
    
#### First Name of employees not living in Miami

result1=re.findall(r"\d{1,};\w+;(\w+);\w+;\d{1,};.+, (?!Miami)",string_data)
print(result1)
# for row in result1:
#     a,b,c = row
#     print(f"{a}  {b} Phone number is :  {c}")