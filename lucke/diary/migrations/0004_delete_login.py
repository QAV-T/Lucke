# Generated by Django 5.0.6 on 2024-07-01 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_rename_post_diary_alter_login_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login',
        ),
    ]