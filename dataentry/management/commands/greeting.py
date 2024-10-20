from django.core.management import BaseCommand


class Command(BaseCommand):
  help = "Greet the user"

  def add_arguments(self, parser):
    parser.add_argument('name', type=str, help='Specifies user name')

  def handle(self, *args, **kwargs):
    name = kwargs['name']
    gretting = f'hi {name} good morning'
    self.stdout.write(gretting)