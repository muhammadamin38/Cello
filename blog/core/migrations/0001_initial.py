# Generated by Django 3.1 on 2022-12-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('data', models.TextField()),
                ('malumot', models.TextField()),
                ('tanlov', models.CharField(max_length=20)),
                ('imgs', models.CharField(max_length=255)),
                ('imge', models.CharField(max_length=255)),
                ('img', models.CharField(max_length=255)),
            ],
        ),
    ]
