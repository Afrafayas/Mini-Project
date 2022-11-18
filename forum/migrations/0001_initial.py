# Generated by Django 3.2.9 on 2022-11-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('forum_id', models.AutoField(db_column='Forum_id', primary_key=True, serialize=False)),
                ('forum_name', models.CharField(db_column='Forum_Name', max_length=11)),
            ],
            options={
                'db_table': 'forum',
                'managed': False,
            },
        ),
    ]
