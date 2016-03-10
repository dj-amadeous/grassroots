from django.core.management.base import BaseCommand
from grassroots.models import api


class Command(BaseCommand):
    help = 'imports from csv'
    def import_from_csv(self):

class Command(BaseCommand):
    help = 'creates bills'   
    def create_bills(self): 
