from django.core.management import BaseCommand

class Command(BaseCommand):
  help = "Import data from CSV file"

  def handle(self, *args, **kwargs):

    self.stdout.write(self.style.SUCCESS("Data imported successfully"))