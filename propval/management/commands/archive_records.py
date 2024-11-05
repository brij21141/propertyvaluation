from django.core.management.base import BaseCommand  
from reception.models import ReceptionReport ,ArchieveReceptionReport
from site_engineer.models import EngineerReport, ArchieveEngineerReport
from reporter.models import ReporterReport, ArchieveReporterReport
from django.utils import timezone  
from django.forms.models import model_to_dict  
from django.db.models import Exists, OuterRef  
  

class Command(BaseCommand):  
    help = "Archive old orders at the start of each month"  

    def handle(self, *args, **kwargs):  
        # Get the first day of the current month  
        first_day_of_month = timezone.now().replace(day=1)  
        dest_records = [] 
        # Archive Orders that were created before the first day of this month  
        old_receptionrecords = ReceptionReport.objects.filter(datecreated__lt=first_day_of_month,reporterreport__datecreated__lt=first_day_of_month,reporter='Submitted')   

        for record in old_receptionrecords:  
             
            record.archieved=True
            record.save()
            # Convert record to dictionary and remove 'id' or any other fields you need to exclude  
            record_dict = model_to_dict(record)  
            record_dict.pop('id')  # Exclude the id field if it exists  

            # Create a new instance of DestinationModel using the record dictionary  
            destination_record = ArchieveReceptionReport(**record_dict)  
            
            # Append to the list (to bulk create later)  
            dest_records.append(destination_record)  
            record.delete()
        # Bulk create all objects at once  
        ArchieveReceptionReport.objects.bulk_create(dest_records)  
        
        dest_records = []
        old_engineerrecords = EngineerReport.objects.filter(  
        datecreated__lt=first_day_of_month, reportersubmitdate__lt=first_day_of_month, 
        reporter='Submitted')
        for record in old_engineerrecords:  
             
            record.archieved=True
            record.save()
            record_dict = model_to_dict(record)  
            record_dict.pop('id') 
            record_dict['userdetailsid'] = record.userdetailsid  # Assuming 'userdetailsid' is your ForeignKey   
            record_dict['receptionid'] = record.receptionid # Assuming 'receptionid
            destination_record = ArchieveEngineerReport(**record_dict)  
            
            dest_records.append(destination_record)  
            record.delete()
        ArchieveEngineerReport.objects.bulk_create(dest_records)  
        dest_records = []
        
        old_reporterrecords = ReporterReport.objects.filter(datecreated__lt=first_day_of_month)  

        for record in old_reporterrecords:  
             
            record.archieved=True
            record.save()
            record_dict = model_to_dict(record)  
            record_dict.pop('id')  
            record_dict['userdetailsid'] = record.userdetailsid  #  'userdetailsid' is  ForeignKey   
            record_dict['receptionid'] = record.receptionid #  'receptionid
            record_dict['bankid'] = record.bankid #  'bankid' is ForeignKey
            destination_record = ArchieveReporterReport(**record_dict)  
            
            # Append to the list (to bulk create later)  
            dest_records.append(destination_record)  
            record.delete()
        # Bulk create all objects at once  
        ArchieveReporterReport.objects.bulk_create(dest_records)  
        
        self.stdout.write(self.style.SUCCESS('Archived old records successfully'))