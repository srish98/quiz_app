# Generated by Django 3.2.4 on 2021-07-23 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_rename_coursename_course_course_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionsmodel',
            name='course',
        ),
        migrations.AlterField(
            model_name='studentscores',
            name='StudentName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]