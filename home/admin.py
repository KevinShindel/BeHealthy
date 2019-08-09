from django.contrib import admin
from home.models import Questions as Question


class QuestionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, QuestionAdmin)
