# Generated by Django 2.2.4 on 2019-08-15 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule', models.CharField(default=None, max_length=150)),
                ('ask_question', models.CharField(max_length=150)),
            ],
        ),
    ]
