from django.db import models
from django.forms import model_to_dict


class Questions(models.Model):
    ask_question = models.CharField(max_length=150)

    def tojson(self):
        return model_to_dict(self, exclude=['id'])
