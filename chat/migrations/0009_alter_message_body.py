# Generated by Django 4.1.5 on 2023-01-26 03:34

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_message_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=django_quill.fields.QuillField(null=True),
        ),
    ]