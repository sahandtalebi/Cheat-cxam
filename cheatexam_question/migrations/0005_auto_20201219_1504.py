# Generated by Django 3.1.4 on 2020-12-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheatexam_question', '0004_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='status',
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='iknow',
            field=models.BooleanField(default=True, null=True, verbose_name='جواب سوال رو بلدم'),
        ),
    ]
