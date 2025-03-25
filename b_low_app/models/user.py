from django.db import models

class User(models.Model):
    name_user = models.CharField(max_length=50)
    email_user = models.EmailField(max_length=100)
    password_user = models.CharField(max_length=100)
    ROL_USER = {
        'u': 'user'
    }
    rol_user = models.CharField(max_length=1, choices=ROL_USER)
    token_user = models.TextField()