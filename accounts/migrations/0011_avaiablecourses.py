# Generated by Django 3.0.8 on 2020-10-23 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20201002_0135'),
    ]

    operations = [
        migrations.CreateModel(
            name='avaiableCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=250)),
                ('courseid', models.CharField(max_length=250)),
                ('courseblock', models.CharField(max_length=250)),
            ],
        ),
    ]
