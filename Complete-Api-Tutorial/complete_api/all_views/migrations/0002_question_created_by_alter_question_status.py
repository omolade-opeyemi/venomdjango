# Generated by Django 4.2.3 on 2023-07-11 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('all_views', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.CharField(default='inactive', max_length=10),
        ),
    ]
