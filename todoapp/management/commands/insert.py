from django.core.management import BaseCommand

    #The class must be named Command, and subclass BaseCommand

from todoapp.models import *


class Command(BaseCommand):
    # Show this when the user types help
    help = "My test command"


    # A command must define handle()
    def handle(self, *args, **options):
        todo_lists = [("harsha", "2017-06-13"), ("chandu", "2017-06-13"), ("ramesh", "2017-06-13"),
                      ("sriram", "2017-06-13"), ("subhash", "2017-06-13")]
        todo_items = [("sleep well", True, "2017-06-13"), ("eat well", True, "2017-06-13"),
                      ("enjoy well", True, "2017-06-13"),
                      ("be passionate", True, "2017-06-13")]
        for i in range(5):
             c = Todolists(name=todo_lists[i][0], creation_date=todo_lists[i][1])
             c.save()
        for i in range(5):
            for j in range(4):
                d = Todoitems(description=todo_items[j][0], completed=todo_items[j][1], due_by=todo_items[j][2],
                              todolist=Todolists.objects.get(name=todo_lists[i][0]))
                d.save()

