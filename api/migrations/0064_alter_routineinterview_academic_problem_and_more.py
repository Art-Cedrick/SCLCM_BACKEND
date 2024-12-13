# Generated by Django 5.0.3 on 2024-12-13 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0063_alter_individualrecordform_living_with_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routineinterview',
            name='academic_problem',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='routineinterview',
            name='career_problem',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='routineinterview',
            name='family_problem',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='routineinterview',
            name='friends_problem',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='routineinterview',
            name='health_problem',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='routineinterview',
            name='recommendation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
