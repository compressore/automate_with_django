import csv
import datetime
from django.core.management import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = 'Export data from student model to a CSV file'

    def handle(self, *args, **kwargs):
        try:
            # fetch data from the DB
            students = Student.objects.all()
            # generate the timestamp of current date and time
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            # define the file name/path
            file_path = f'exported_students_data-{timestamp}.csv'

            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                # write CSV header
                writer.writerow(['Roll No', 'Name', 'Age'])

                for data in students:
                    writer.writerow([data.roll_no, data.name, data.age])

            self.stdout.write(self.style.SUCCESS("Data exported successfully!"))

        except Student.DoesNotExist:
            self.stdout.write(self.style.ERROR("No students found in the database."))

        except IOError as e:
            self.stdout.write(self.style.ERROR(f"IO error occurred: {e}"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
