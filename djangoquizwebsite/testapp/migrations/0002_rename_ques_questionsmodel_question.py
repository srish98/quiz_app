# Generated by Django 3.2.4 on 2021-07-21 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionsmodel',
            old_name='ques',
            new_name='question',
        ),
    ]
