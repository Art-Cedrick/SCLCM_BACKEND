import csv
from django.core.management.base import BaseCommand
from api.models import CareerTracking, IndividualRecordForm, Profile
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Import dataset into IndividualRecordForm model'

    def handle(self, *args, **kwargs):
        #file_path = r'C:\Users\ACER\Documents\GitHub\SCLCM_BACKEND\api\management\commands\data\CAREER-TRACKING.csv'  # Adjust the file path
        #file_path = '/root/SCLCM_BACKEND/api/management/commands/data/INDIVIDUAL-RECORD-FORM.csv'

        #file_path = '/root/SCLCM_BACKEND/api/management/commands/data/ACCOUNTS.csv'

        file_path = os.path.join(settings.BASE_DIR, 'api', 'management', 'commands', 'data', 'INDIVIDUAL-RECORD-FORM.csv')

        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    try:
                        default_profile = Profile.objects.get(id=1)

                        IndividualRecordForm.objects.create(
                            profile=default_profile,  
                            sr_code=row['sr_code'],  
                            lastname=row['lastname'],
                            firstname=row['firstname'],
                            middlename=row['middlename'],
                            year=row['year'],

                            section=row['section'],
                            completeAddress=row['completeAddress'],
                            fatherName=row['fatherName'],
                            fatherOccupation=row['fatherOccupation'],
                            fatherContactNumber=row['fatherContactNumber'],
                            fatherEmailAddress=row['fatherEmailAddress'],
                            motherName=row['motherName'],
                            motherOccupation=row['motherOccupation'],
                            motherContactNumber=row['motherContactNumber'],
                            motherEmailAddress=row['motherEmailAddress'],
                            parents=row['parents'],
                            living_with=row['living_with'],
                            relationship=row['relationship'],
                            club=row['club']
                        )

                        self.stdout.write(self.style.SUCCESS(f"Successfully imported data for: {row['firstname']} {row['lastname']}"))

                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f"An error occurred for row {row.get('firstname', '')} {row.get('lastname', '')}: {e}"))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File '{file_path}' not found."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {e}"))
