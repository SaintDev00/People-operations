import csv
import os
from datetime import datetime, timedelta

def start_holidays_file():
    """Create the csv file if it does not exist"""
    if not os.path.exists('holidays.csv'):
        with open('holidays.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['employee_id', 'employee_name', 'start_date', 
                           'end_date', 'calculated_days', 'status', 'month', 'year'])

def get_employee(employee_id):
    """Get employee information"""
    if not os.path.exists('employees.csv'):
        return None
    
    with open('employees.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for emp in reader:
            if emp['employee_id'] == employee_id:
                return emp
    return None

def calculate_months_worked(start_date):
    """Calculate complete months worked since start date"""
    start_date_dt = datetime.strptime(start_date, '%d/%m/%Y')
    current_date = datetime.now()
    
    months = (current_date.year - start_date_dt.year) * 12
    months += current_date.month - start_date_dt.month
    
    if current_date.day < start_date_dt.day:
        months -= 1
    
    return max(0, months)

def calculate_available_days(employee_id, months_worked):
    """Calculate available vacation days"""
    accumulated_days = months_worked * 1.5
    
    # Subtract already approved days
    used_days = 0
    if os.path.exists('holidays.csv'):
        with open('holidays.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['employee_id'] == employee_id and row['status'] == 'APPROVED':
                    used_days += float(row['calculated_days'])
    
    return accumulated_days - used_days

def calculate_requested_days(start_date, end_date):
    """Calculate days between two dates excluding Sundays"""
    start = datetime.strptime(start_date, '%d/%m/%Y')
    end = datetime.strptime(end_date, '%d/%m/%Y')
    
    days = 0
    current_date = start
    
    while current_date <= end:
        if current_date.weekday() != 6:  # 6 = Sunday
            days += 1
        current_date += timedelta(days=1)
    
    return days

def register_request():
    """Register a new vacation request"""
    start_holidays_file()
    
    print("\n--- REGISTER VACATION REQUEST ---")
    employee_id = input("Employee ID: ")
    
    employee = get_employee(employee_id)
    if not employee:
        print(f"\n✗ Employee with ID {employee_id} not found")
        input("Press Enter to continue...")
        return
    
    # Validate minimum time
    months_worked = calculate_months_worked(employee['contract_start_date'])
    if months_worked < 6:
        print(f"\n✗ Employee must have at least 6 months working")
        print(f"  Months worked: {months_worked}")
        input("Press Enter to continue...")
        return
    
    # Calculate available days
    available_days = calculate_available_days(employee_id, months_worked)
    print(f"\nAvailable days: {available_days:.1f}")
    
    start_date = input("Start date (DD/MM/YYYY): ")
    end_date = input("End date (DD/MM/YYYY): ")
    
    # Calculate requested days
    requested_days = calculate_requested_days(start_date, end_date)
    print(f"Requested days (without Sundays): {requested_days}")
    
    if requested_days > available_days:
        print(f"\n✗ Not enough available days")
        input("Press Enter to continue...")
        return
    
    # Register request
    date_obj = datetime.strptime(start_date, '%d/%m/%Y')
    month = date_obj.month
    year = date_obj.year
    
    with open('holidays.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([employee_id, employee['full_name'], start_date, 
                        end_date, requested_days, 'PENDING', month, year])
    
    print(f"\n✓ Request registered successfully")
    input("Press Enter to continue...")

def approve_reject_request():
    """Approve or reject pending requests"""
    start_holidays_file()
    
    print("\n--- PENDING REQUESTS ---")
    
    requests = []
    with open('holidays.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if row['status'] == 'PENDING':
                requests.append(row)
                print(f"\n[{i}] ID: {row['employee_id']} - {row['employee_name']}")
                print(f"    Dates: {row['start_date']} to {row['end_date']}")
                print(f"    Days: {row['calculated_days']}")
    
    if not requests:
        print("No pending requests")
        input("\nPress Enter to continue...")
        return
    
    try:
        index = int(input("\nEnter request number: "))
        if index < 0 or index >= len(requests):
            print("✗ Invalid index")
            input("Press Enter to continue...")
            return
    except:
        print("✗ Invalid input")
        input("Press Enter to continue...")
        return
    
    action = input("Approve or Reject? (A/R): ").upper()
    new_status = 'APPROVED' if action == 'A' else 'REJECTED'
    
    # Update status
    all_requests = []
    with open('holidays.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        all_requests = list(reader)
    
    counter = 0
    for row in all_requests:
        if row['status'] == 'PENDING':
            if counter == index:
                row['status'] = new_status
                break
            counter += 1
    
    with open('holidays.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['employee_id', 'employee_name', 
                                               'start_date', 'end_date',
                                               'calculated_days', 'status', 'month', 'year'])
        writer.writeheader()
        writer.writerows(all_requests)
    
    print(f"\n✓ Request {new_status.lower()}")
    input("Press Enter to continue...")

def view_history():
    """Show vacation history of an employee"""
    start_holidays_file()
    
    print("\n--- VACATION HISTORY ---")
    employee_id = input("Employee ID: ")
    
    with open('holidays.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        found = False
        
        for row in reader:
            if row['employee_id'] == employee_id:
                print(f"\n{row['employee_name']}")
                print(f"Dates: {row['start_date']} to {row['end_date']}")
                print(f"Days: {row['calculated_days']}")
                print(f"Status: {row['status']}")
                print("-" * 40)
                found = True
        
        if not found:
            print(f"\n✗ No records found for employee {employee_id}")
    
    input("\nPress Enter to continue...")

def main_holidays():
    """Vacation management menu"""
    while True:
        print("\n" + "="*50)
        print("   VACATION MANAGEMENT")
        print("="*50)
        print("1. Register request")
        print("2. Approve/Reject request")
        print("3. View employee history")
        print("4. Return to main menu")
        print("="*50)
        
        option = input("\nSelect an option: ")
        
        if option == "1":
            register_request()
        elif option == "2":
            approve_reject_request()
        elif option == "3":
            view_history()
        elif option == "4":
            break
        else:
            print("\n✗ Invalid option")
            input("Press Enter to continue...")
