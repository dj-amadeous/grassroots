from django.core.management.base import BaseCommand
from api import read_from_csv
from api import create_bills

class Command(BaseCommand):
    help = 'imports from csv'
    

class Command(BaseCommand):
    help = 'creates bills'   
    def create_bills(self): 
