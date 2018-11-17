from django.db import models


class EmailRegis(models.Model):
    FirstNameField = models.CharField(max_length=50, verbose_name = 'First Name')
    lastNameField = models.CharField(max_length = 50, verbose_name = 'Last Name')
    emailField = models.CharField(max_length=50, verbose_name = 'E-mail')

    def __str__(self):
        return self.emailField




