import csv
from django.core.management.base import BaseCommand
from api.models import Profile
from django.contrib.auth.models import User
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Import dataset into Profile model'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'api', 'management', 'commands', 'data', 'ACCOUNTS.csv')

        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    try:
                        user = User.objects.create_user(
                            username=row['Username'],
                            password=row['Password'],  
                            email=row.get('Email', '') 
                        )

                        Profile.objects.create(
                            user=user,

                            role=row['Role'],
                            first_name=row.get('First_Name', ''),
                            last_name=row.get('Last_Name', ''),
                            middle_name=row.get('Middle_Name', ''),
                            phone_number=row.get('Phone_Number', ''),
                            address=row.get('Address', '')
                        )

                        self.stdout.write(self.style.SUCCESS(f"Successfully imported profile for: {row['Username']}"))

                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f"An error occurred for row {row.get('Username', 'unknown')}: {e}"))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"File '{file_path}' not found."))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {e}")) 