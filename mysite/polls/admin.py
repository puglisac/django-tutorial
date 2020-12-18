from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# include question and choice models on admin page
admin.site.register(Question)
admin.site.register(Choice)