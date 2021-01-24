from django.db import models

class Password(models.Model):
    title = models.CharField(max_length=122)
    website = models.CharField(max_length=12)
    user = models.CharField(max_length=122)
    myRange=models.CharField(max_length=7)

    def __str__(self):
        return self.title