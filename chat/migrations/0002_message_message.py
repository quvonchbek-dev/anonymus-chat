# Generated by Django 4.1.5 on 2023-01-20 13:47

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
