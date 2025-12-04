# PeopleOps Vacation Console

Holiday management system for RIWI's People Operations area.

## Student Information
- **Full name:** [Your name here]
- **ID Document:** [Your ID here]
- **Clan/Group:** [Your clan here]

## General Description
Python console application that manages employees and their vacations, automatically calculating available days based on seniority, validating requirements, and generating CSV reports.

## How to Run the Program

### Requirements
- Python 3.7 or higher

### Execution
1. Open terminal in the project folder
2. Run: `python Main.py`
3. Default credentials:
   - User: `admin`
   - Password: `admin123`

### Required CSV Files
Create these 3 CSV files manually:

**users.csv**
```csv
user,password,rol
admin,admin123,administrator
```

**employees.csv** (can start empty)
```csv
employee_id,full_name,position,area,contract_start_date
```

**holidays.csv** (must start empty)
```csv
employee_id,employee_name,start_date,end_date,calculated_days,status,month,year
```

## Project Structure

```
├── Main.py           # Main program and menu
├── Users.py          # Credential validation
├── Employees.py      # Employee management (register, list, search)
├── Holidays.py       # Vacation calculations and requests
├── Reports.py        # CSV report export
└── README.md         # Documentation
```

### File Description

- **Main.py**: Entry point, handles login and main menu
- **Users.py**: Validates credentials against CSV file
- **Employees.py**: Employee CRUD (create, read, search)
- **Holidays.py**: Business logic for vacations (calculations, validations, approvals)
- **Reports.py**: Generates CSV reports filtered by month/year

## Calculation Rules

### Vacation Accumulation
- **1.5 days per month worked**
- Calculation: complete months × 1.5 - already approved days

### Requirements to Request
- **Minimum 6 months worked**
- Automatic validation when registering request

### Day Calculation
- Counts all days between start and end date
- **Excludes Sundays** from count
- Validates availability before registering

## Main Features

### Employee Management
1. Register new employee
2. List all employees
3. Search specific employee

### Vacation Management
1. Register request (validates 6 months and available days)
2. Approve/Reject pending requests
3. View complete history by employee

### Reports
- Export approved vacations by month/year
- Includes complete data: employee, position, area, dates, days

## Limitations and Future Improvements

### Current Limitations
- Does not allow editing registered employees
- Does not handle multiple admin users
- Fixed date format (DD/MM/YYYY)
- Does not validate future dates for requests

### Proposed Improvements
- Employee editing and deletion
- User roles (admin, employee)
- Dashboard with statistics
- More robust date validation
- Graphical interface (GUI)
- SQL database instead of CSV
- Email notifications
- Export reports to PDF/Excel

## Usage Example

1. Login with admin/admin123
2. Register employee (contract date: 01/01/2024)
3. Wait 6 months to request vacation
4. Register vacation request
5. Approve request from menu
6. Generate monthly report

## License
Academic project - RIWI 2025
