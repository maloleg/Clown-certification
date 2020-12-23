from django.db import models
import time
# Create your models here.

class Data(models.Model):
    Who_is_clown = 'No one'
    Amound_of_times = dict()
    time = time.time()
    clownUrl = 'https://vk.com/jumoreski'
    # print(Who_is_clown("None"))

    def __str__(self):
        return self.title