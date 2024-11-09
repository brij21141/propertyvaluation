from django.core.management.base import BaseCommand  
from reception.models import ReceptionReport ,ArchieveReceptionReport
from site_engineer.models import EngineerReport, ArchieveEngineerReport
from reporter.models import ReporterReport, ArchieveReporterReport
from django.utils import timezone  
from django.forms.models import model_to_dict  
from django.db import transaction
  

class Command(BaseCommand):  
    help = "Archive old orders at the start of each month"  

    def handle(self, *args, **kwargs):  
        # Get the first day of the current month  
        with transaction.atomic():  # Start the transaction  if transactions fails it will rollback data
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
                record_dict['id'] = record.id  # Retaining the existing ID
                # Create a new instance of DestinationModel using the record dictionary  
                destination_record = ArchieveReceptionReport(**record_dict)  
                
                # Append to the list (to bulk create later)  
                dest_records.append(destination_record)  
                # record.delete()
            # Bulk create all objects at once  
            ArchieveReceptionReport.objects.bulk_create(dest_records) 
            
            dest_engrecords = []
            old_engineerrecords = EngineerReport.objects.filter(  
            datecreated__lt=first_day_of_month, reportersubmitdate__lt=first_day_of_month, 
            reporter='Submitted')
            for record in old_engineerrecords: 
                print(record) 
                print(record.receptionid) 
                record.archieved=True
                record.save()
                record_dict = model_to_dict(record)  
                # record_dict.pop('id') 
                # record_dict.pop('receptiontempid') 
                # record_dict['id'] = record.id  # Retaining the existing ID 
                record_dict['userdetailsid'] = record.userdetailsid  #  'userdetailsid'  ForeignKey   
                # record_dict['receptiontempid'] = record.receptionid_id # 'receptionid is foreign key
                record_dict['receptionid'] = ArchieveReceptionReport.objects.get(pk=record.receptionid.id) # 'receptionid is foreign key
                destination_record = ArchieveEngineerReport(**record_dict)  
                
                dest_engrecords.append(destination_record)  
                record.delete()
            ArchieveEngineerReport.objects.bulk_create(dest_engrecords)  
            dest_reprecords = []
            
            old_reporterrecords = ReporterReport.objects.filter(datecreated__lt=first_day_of_month)  

            for record in old_reporterrecords:  
                
                record.archieved=True
                record.save()
                record_dict = model_to_dict(record)  
                # record_dict.pop('id')  
                # record_dict['id'] = record.id  # Retaining the existing ID
                # record_dict.pop('receptiontempid') 
                record_dict['userdetailsid'] = record.userdetailsid  #  'userdetailsid' is  ForeignKey   
                # record_dict['receptiontempid'] = record.receptionid_id #  'receptionid
                record_dict['receptionid'] = ArchieveReceptionReport.objects.get(pk=record.receptionid.id) # 'receptionid is foreign key
                record_dict['bankid'] = record.bankid #  'bankid' is ForeignKey
                destination_record = ArchieveReporterReport(**record_dict)  
                
                # Append to the list (to bulk create later)  
                dest_reprecords.append(destination_record)  
                record.delete()
            # Bulk create all objects at once  
            ArchieveReporterReport.objects.bulk_create(dest_reprecords) 

            old_receptionrecords = ReceptionReport.objects.filter(archieved=True)   

            for record in old_receptionrecords:  
                record.delete()
            
            self.stdout.write(self.style.SUCCESS('Archived old records successfully'))

        