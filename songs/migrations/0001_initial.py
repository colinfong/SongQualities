# Generated by Django 5.0.4 on 2024-04-26 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('artist', models.CharField(max_length=20)),
                ('quality', models.CharField(max_length=50)),
                ('timestamp', models.CharField(max_length=10)),
            ],
        ),
    ]
