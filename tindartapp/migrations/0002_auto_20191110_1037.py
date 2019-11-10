# Generated by Django 2.2.7 on 2019-11-10 10:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tindartapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='likes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='art',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
