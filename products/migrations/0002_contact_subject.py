# Generated by Django 5.0.4 on 2024-04-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='subiect', max_length=255),
            preserve_default=False,
        ),
    ]