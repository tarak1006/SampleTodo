from django.core.management import BaseCommand

    #The class must be named Command, and subclass BaseCommand

from todoapp.models import *


class Command(BaseCommand):
    # Show this when the user types help
    help = "My test command"

    # A command must define handle()
    def handle(self, *args, **options):
        c=Todolists.objects.all()
        for i in c:
            print i
            d=list(Todoitems.objects.filter(todolist__name=i))
            for j in range(len(d)):
                print "\t",d[j]

