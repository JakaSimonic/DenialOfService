# Generated by Django 3.2.9 on 2021-11-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosdata',
            name='id',
        ),
        migrations.AlterField(
            model_name='dosdata',
            name='client_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dosdata',
            name='timeframe_start',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
