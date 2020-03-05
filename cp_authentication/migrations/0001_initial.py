# Generated by Django 2.1.5 on 2020-03-03 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthDatabaseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(db_column='Login', max_length=100)),
                ('password', models.CharField(db_column='Password', max_length=100)),
            ],
            options={
                'db_table': 'User',
                'managed': False,
            },
        ),
    ]
