# Generated by Django 3.1.6 on 2021-02-21 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
