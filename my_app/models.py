from django.db import models

# Create your models here.


class AccountInfo(models.Model):
    username = models.CharField(max_length=40)
    passwd = models.CharField(max_length=150)
    phone_num = models.CharField(max_length=11)

    def __str__(self):
        return self.username
