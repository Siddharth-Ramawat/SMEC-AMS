# Generated by Django 2.2.1 on 2020-03-10 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20200310_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='user_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]