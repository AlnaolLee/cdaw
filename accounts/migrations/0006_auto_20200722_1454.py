# Generated by Django 3.0.8 on 2020-07-22 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_fmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='another',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(max_length=10)),
                ('grade', models.TextField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='fmodel',
        ),
    ]
