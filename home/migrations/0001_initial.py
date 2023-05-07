# Generated by Django 4.2 on 2023-05-02 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productsdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users_id', models.CharField(max_length=300)),
                ('product_name', models.CharField(max_length=250, unique=True)),
                ('organization_name', models.CharField(max_length=250)),
                ('vendors_name', models.CharField(max_length=1000)),
                ('p_type', models.CharField(max_length=50)),
                ('issue_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Productstatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(unique=True)),
                ('status', models.CharField(max_length=50)),
                ('update_user', models.CharField(max_length=250)),
                ('update_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True)),
                ('phone', models.IntegerField(default=0, unique=True)),
                ('designation', models.CharField(max_length=150)),
                ('organization', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
    ]
