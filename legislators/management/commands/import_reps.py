from api import read_from_csv, create_bills
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Imports legislators into the database'

    def add_arguments(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        read_from_csv(options['path'])
        self.stdout.write(self.style.SUCCESS('Successfully imported representatives.'))



class Command(BaseCommand):
    help = 'creates bills'

    def create_bills(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        create_bills(options['path'])
        for i in range(20):
            create_bills(i)
        self.stdout.write(self.style.SUCCESS('Successfully created bills.'))

