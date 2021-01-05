import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# Question model
class Question(models.Model):
    def __str__(self):
        return self.question_text

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# returns true if pub_date is less than 1 day old
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    # change how the published recently column in admin page displays/acts
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

# Choice model
class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    