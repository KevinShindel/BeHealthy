from django.db import models


class Questions(models.Model):
    rule = models.CharField(max_length=150, default=None)
    ask_question = models.CharField(max_length=150)
