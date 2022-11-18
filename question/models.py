from django.db import models
from moderator.models import Moderator

# Create your models here.
class Question(models.Model):
    question_id = models.AutoField(db_column='Question_id', primary_key=True)  # Field name made lowercase.
    question = models.CharField(max_length=500)
    moderator_id = models.IntegerField(db_column='Moderator_id')  # Field name made lowercase.
    status = models.CharField(max_length=10)
    category = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'question'


