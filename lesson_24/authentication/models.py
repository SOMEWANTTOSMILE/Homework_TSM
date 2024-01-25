from django.db import models


class Users(models.Model):
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=255)

    def __str__(self):
        return self.user_email


