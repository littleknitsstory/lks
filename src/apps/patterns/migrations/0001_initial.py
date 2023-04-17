# Generated by Django 4.1.2 on 2023-04-15 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern_number', django_extensions.db.fields.ShortUUIDField(blank=True, editable=False, verbose_name='Pattern number')),
                ('prompt', models.TextField(verbose_name='Users text')),
                ('created_up', models.DateTimeField(auto_now_add=True, verbose_name='request time')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pattern_user', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
        ),
    ]
