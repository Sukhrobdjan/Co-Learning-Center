# Generated by Django 4.0.6 on 2022-07-27 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_option'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='option',
        ),
        migrations.AddField(
            model_name='product',
            name='option',
            field=models.ManyToManyField(to='product.optionvalue'),
        ),
    ]