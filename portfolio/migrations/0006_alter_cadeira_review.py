# Generated by Django 4.0.5 on 2022-06-07 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_cadeira_semestre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadeira',
            name='review',
            field=models.CharField(max_length=10),
        ),
    ]
