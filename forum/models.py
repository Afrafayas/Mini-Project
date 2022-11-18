from django.db import models
from moderator.models import Moderator

# Create your models here.
class Forum(models.Model):
    forum_id = models.AutoField(db_column='Forum_id', primary_key=True)  # Field name made lowercase.
    forum_name = models.CharField(db_column='Forum_Name', max_length=11)  # Field name made lowercase.
    # moderator_id = models.IntegerField(db_column='Moderator_id')  # Field name made lowercase.
    moderator=models.ForeignKey(Moderator,to_field='moderator_id',on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'forum'

