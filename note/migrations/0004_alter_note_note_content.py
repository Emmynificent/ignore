# Generated by Django 4.0.2 on 2023-01-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_note_note_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note_content',
            field=models.TextField(blank=True),
        ),
    ]
