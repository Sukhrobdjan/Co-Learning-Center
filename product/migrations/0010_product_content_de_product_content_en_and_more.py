# Generated by Django 4.0.6 on 2022-07-27 11:51

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_remove_product_option_product_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content_de',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='content_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_de',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=256, null=True),
        ),
    ]