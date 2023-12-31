# Generated by Django 4.2.5 on 2023-10-10 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={},
        ),
        migrations.AddField(
            model_name='tasks',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='task',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
