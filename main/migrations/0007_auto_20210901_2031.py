# Generated by Django 3.1.6 on 2021-09-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_frame_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='button',
            field=models.CharField(default='', max_length=350),
        ),
        migrations.AddField(
            model_name='campaign',
            name='sub_desc',
            field=models.CharField(default='', max_length=350),
        ),
        migrations.AddField(
            model_name='campaign',
            name='sub_title',
            field=models.CharField(default='', max_length=150),
        ),
    ]