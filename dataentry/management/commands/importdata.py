from django.core.management import BaseCommand, CommandError
from django.apps import apps
import csv

class Command(BaseCommand):
  help = "Import data from CSV file"

  def add_arguments(self, parser):
    parser.add_argument('file_path', type=str, help="CSV file path")
    parser.add_argument('model_name', type=str, help="Model name")

    
  def handle(self, *args, **kwargs):
    file_path = kwargs['file_path']
    model_name = kwargs['model_name'].capitalize()

    model = None
    for app_confing in apps.get_app_configs():
      try:
        model = apps.get_model(app_confing.label,model_name)
        break #Stop searching once model is found
      except LookupError:
        continue # model not found in this app, so continue searching in the next app

    if not model:
        raise CommandError(f"Model {model_name} not found in any app")

    # search for the model across the project apps
    with open(file_path , 'r') as file:
      reader =  csv.DictReader(file)

      for row in reader:
          model.objects.create(**row)

    self.stdout.write(self.style.SUCCESS("Data imported successfully!"))