# Generated by Django 4.0.1 on 2022-05-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220506_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'PENDING'), (2, 'CANCELED'), (3, 'COMPLETED')])),
            ],
            options={
                'verbose_name': 'Request Status',
                'verbose_name_plural': 'Request Statuses',
            },
        ),
    ]