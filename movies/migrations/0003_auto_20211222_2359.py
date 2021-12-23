# Generated by Django 3.0.3 on 2021-12-22 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20211222_1755'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service',
            new_name='Movie',
        ),
        migrations.RenameModel(
            old_name='ServiceShots',
            new_name='MovieShots',
        ),
        migrations.RenameField(
            model_name='movieshots',
            old_name='service',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='service',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='service',
            new_name='movie',
        ),
    ]
