# Generated by Django 3.2.4 on 2023-09-03 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table1_models',
            name='user_id',
            field=models.CharField(default='null', max_length=50),
            preserve_default=False,
        ),
    ]