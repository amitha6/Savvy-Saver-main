# Generated by Django 2.2.6 on 2019-11-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20191101_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, default='default-product.png', upload_to=''),
        ),
    ]