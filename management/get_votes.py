from django.core.management.base import BaseCommand
from api import create_bills

    
class Command(BaseCommand):
    help = 'creates bills'

    def create_bills(self, parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        create_bills(options['path'])
        for i in range(20):
            create_bills(i)
        self.stdout.write(self.style.SUCCESS('Successfully created bills.'))

