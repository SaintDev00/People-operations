import csv
import os

def get_employee_data(employee_id):
    """Get employee information from CSV"""
    if not os.path.exists('employees.csv'):
        return None
    
    with open('employees.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for emp in reader:
            if emp['employee_id'] == employee_id:
                return emp
    return None

def generate_report():
    """Generate a CSV report of vacations by month and year"""
    print("\n--- GENERATE VACATION REPORT ---")
    
    month = input("Month (1-12): ")
    year = input("Year (YYYY): ")
    
    filename = f"report_vacations_{year}_{month.zfill(2)}.csv"
    
    # Read approved vacations for the period
    filtered_vacations = []
    
    if os.path.exists('holidays.csv'):
        with open('holidays.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['status'] == 'APPROVED' and row['month'] == month and row['year'] == year:
                    # Get additional employee data
                    employee = get_employee_data(row['employee_id'])
                    if employee:
                        filtered_vacations.append({
                            'employee_id': row['employee_id'],
                            'employee_name': row['employee_name'],
                            'position': employee.get('position', 'N/A'),
                            'area': employee.get('area', 'N/A'),
                            'start_date': row['start_date'],
                            'end_date': row['end_date'],
                            'calculated_days': row['calculated_days'],
                            'month': row['month'],
                            'year': row['year']
                        })
    
    if not filtered_vacations:
        print(f"\n✗ No approved vacations for {month}/{year}")
        input("Press Enter to continue...")
        return
    
    # Generate CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['employee_id', 'employee_name', 'position', 'area', 
                     'start_date', 'end_date', 'calculated_days', 'month', 'year']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_vacations)
    
    print(f"\n✓ Report generated successfully: {filename}")
    print(f"  Total records: {len(filtered_vacations)}")
    input("\nPress Enter to continue...")
