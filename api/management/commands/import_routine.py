import csv
from django.core.management.base import BaseCommand
from api.models import RoutineInterview, IndividualRecordForm
from django.conf import settings
import os
from datetime import datetime

class Command(BaseCommand):
    help = 'Import dataset into RoutineInterview model'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'api', 'management', 'commands', 'data', 'ROUTINE_INTERVIEW.csv')

        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    if not any(row.values()):
                        continue
                        

                    try:
                        date = datetime.strptime(row['Date'], '%Y-%m-%d').date() if row['Date'] else None


                        sr_code = row['Student Number'] if row['Student Number'] else None
                        
                        RoutineInterview.objects.create(
                            sr_code=sr_code,  
                            name=row['Name'],
                            section=row['Section'],
                            grade=row['Grade'],
                            date=date,
                            family_problem=row['Family'],

                            family_details=row['FD'],
                            friends_problem=row['Friends'],
                            friends_details=row['FFD'],
                            health_problem=row['Personal &  Health'],
                            health_details=row['PD'],
                            academic_problem=row['Academic / School'],
                            academic_details=row['AD'],
                            career_problem=row['Career'],
                            career_details=row['CD'],
                            remarks=row['Remarks'],
                            recommendation=row['Recommendations'],
                            other_recommendation=row['Others']
                        )

                        self.stdout.write(
                            self.style.SUCCESS(f"Successfully imported data for: {row['Name']}")
                        )

                    except Exception as e:
                        self.stderr.write(
                            self.style.ERROR(f"An error occurred for row {row.get('Name', 'Unknown')}: {e}")
                        )

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File '{file_path}' not found."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {e}")) 