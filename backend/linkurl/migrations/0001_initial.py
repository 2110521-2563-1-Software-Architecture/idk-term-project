# Generated by Django 3.1.2 on 2020-10-08 16:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('link_shorten', models.CharField(max_length=5, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(5)])),
                ('link_original', models.CharField(max_length=200)),
                ('link_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='links_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
