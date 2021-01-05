from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# class to add choices to question inline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# format how question admin page looks
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # how questions are desplayed on main question page
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # adds filter by pub_date
    list_filter = ['pub_date']
    # adds search capability by question text
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

