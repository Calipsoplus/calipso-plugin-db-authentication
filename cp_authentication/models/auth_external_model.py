from django.db import models

from django.conf import settings


# Create your models here.
class AuthDatabaseUser(models.Model):
    login = models.CharField(db_column=settings.EXTERNAL_DB_USERNAME_FIELD, max_length=100)
    password = models.CharField(db_column=settings.EXTERNAL_DB_PASSWORD_FIELD, max_length=100)

    def __str__(self):
        return self.login

    class Meta:
        db_table = settings.EXTERNAL_DB_TABLE
        managed = False
