import csv
import os

def start_employee_file():
#Create the csv file if it does not exist

    if not os.path.exists('employees.csv'):
        with open('employees.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['employee_id', 'full_name', 'position', 'area', 'contract_start_date'])
            
def register_employee():
 