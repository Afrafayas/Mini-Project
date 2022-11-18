# Generated by Django 3.2.9 on 2022-11-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(db_column='Question_id', primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'question',
                'managed': False,
            },
        ),
    ]
