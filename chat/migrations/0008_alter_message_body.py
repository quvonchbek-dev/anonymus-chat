# Generated by Django 4.1.5 on 2023-01-23 13:38

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_message_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=django_quill.fields.QuillField(default='ici'),
        ),
    ]