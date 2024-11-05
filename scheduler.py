import os  
import django  
import schedule  
import time  
from datetime import datetime
from django.core.management import call_command  

# Set the environment variable for Django settings  
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'propertyvaluation.settings')  

# Initialize Django  
django.setup()  

def archive_records():  
    call_command('archive_records')  # Your management command here  
def job():  
    # Check if today is the first day of the month  
    if datetime.now().day == 10:  # Change to your desired day  
        archive_records()  

# Schedule the job to run every day  
schedule.every().day.at("00:00").do(job)  


# Schedule the task for the 1st day of each month  
# schedule.every().month.at("00:00").do(archive_records)  

while True:  
    schedule.run_pending()  
    time.sleep(1)