# Generated by Django 3.0.8 on 2021-06-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('lectureVideoID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('lectureVideo', models.CharField(max_length=20)),
                ('lectureName', models.CharField(max_length=20)),
                ('fileName', models.CharField(max_length=20)),
            ],
        ),
    ]