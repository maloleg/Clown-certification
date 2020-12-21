from django.db import models

# Create your models here.

class Data(models.Model):
    Who_is_clown = 'None'
    Amound_of_times = dict()
    # print(Who_is_clown("None"))

    def __str__(self):
        return self.title