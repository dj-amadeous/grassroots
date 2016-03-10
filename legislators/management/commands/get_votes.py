from django.core.management.base import BaseCommand
from api import create_bills
   
class Command(BaseCommand):
    help = 'creates bills'
    def add_arguments(self, parser):
        parser.add_argument(input)
    def handle(self, *args, **options):
        for i in range(input):
            create_bills(i)
        self.stdout.write(self.style.SUCCESS('Successfully created bills.'))
