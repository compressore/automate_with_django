import csv
import datetime
from django.core.management import BaseCommand
from django.apps import apps

# proposed command python manage.py exportdata model_name
class Command(BaseCommand):
    help = 'Export data from the DB to a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model name')

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name'].capitalize()
        #search through all installed apps for the model
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label,model_name)
                break #Stop searching once the model is found
            except LookupError:
                pass # model not found in this app, so continue searching in the next app

        if not model:
            self.stderr.write(f'Model {model_name} not found')
            return
        # fetch data from the DB
        data = model.objects.all()
        # generate the timestamp of current date and time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        # define the file name/path
        file_path = f'exported_{model_name}_data-{timestamp}.csv'

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            # write CSV header
            # retrieve all field names of the model that we are exporting
            writer.writerow([field.name for field in model._meta.fields])

            for info in data:
                writer.writerow([getattr(info, field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS("Data exported successfully!"))


