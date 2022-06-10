# Generated by Django 4.0.5 on 2022-06-10 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0003_credential_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=100)),
                ('members', models.CharField(max_length=300)),
                ('contact', models.EmailField(max_length=254)),
            ],
        ),
    ]