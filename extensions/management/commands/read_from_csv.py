from django.core.management.base import BaseCommand 
from api import read_from_csv


class Command(BaseCommand, change_file_path):
    help = 'reads from csv'
    def handle(self, **options):
        read_from_csv()

