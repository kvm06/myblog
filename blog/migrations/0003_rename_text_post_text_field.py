# Generated by Django 3.2.6 on 2021-08-19 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='text_field',
        ),
    ]
