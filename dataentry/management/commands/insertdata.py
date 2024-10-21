from django.core.management import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
  help = "Insert data into database"

  def handle(self, *args, **kwargs):
    dataset = [
      { 'roll_no': 5, 'name': 'Drake', 'age': 44},
      { 'roll_no': 3, 'name': 'James', 'age': 15},
    ]
    for data in dataset:
      roll_no = data['roll_no']
      check_exist = Student.objects.filter(roll_no=roll_no).exists()
      if not check_exist:
        pass
        Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
      else:
        self.stdout.write(self.style.WARNING(f"Student with roll number {data['roll_no']} already exist"))
    self.stdout.write(self.style.SUCCESS("Data inserted successfully"))