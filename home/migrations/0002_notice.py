# Generated by Django 4.2 on 2023-05-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice_name', models.CharField(max_length=500)),
                ('upload_date', models.DateField()),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]