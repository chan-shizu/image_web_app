# Generated by Django 2.1.2 on 2019-02-25 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20190225_1412'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Touroku',
        ),
        migrations.RemoveField(
            model_name='document',
            name='gray_photo',
        ),
        migrations.AddField(
            model_name='document',
            name='output',
            field=models.ImageField(default='output/output.jpg', upload_to=''),
        ),
    ]
