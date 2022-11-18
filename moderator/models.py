from django.db import models

# Create your models here.
class Moderator(models.Model):
    moderator_id = models.AutoField(db_column='Moderator_id', primary_key=True)  # Field name made lowercase.
    moderator_name = models.CharField(db_column='Moderator_name', max_length=15)  # Field name made lowercase.
    age = models.CharField(db_column='Age', max_length=5)  # Field name made lowercase.
    qualification = models.CharField(db_column='Qualification', max_length=10)  # Field name made lowercase.
    email_id = models.CharField(db_column='Email_id', max_length=20)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=20)  # Field name made lowercase.
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'moderator'





