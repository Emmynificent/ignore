# Generated by Django 4.0.2 on 2023-06-14 13:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_noteuserprofile_created_alter_noteuserprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noteuserprofile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
