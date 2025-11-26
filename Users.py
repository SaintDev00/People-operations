import csv

import os

def validate_credentials(user, password):
        #Validates credentials against the csv file
           
        if not os.path.exists('users.csv'):
        #Create file with default admin user
            
            with open ('users.csv', 'w', newline='', encoding='utf_8') as f:
                
                writer = csv.writer(f)
                
                writer.writerow(['user', 'password', 'rol'])
                
                writer.writerow(['admin', 'admin123', 'administrator'])
                
                
        with open('usuarios.csv', 'r', encoding='utf_8') as f:
            
            reader = csv.DictReader(f)
            
            for row in reader:
                
                if row['user'] == user and row['password'] == password:
                    
                    
                    return False