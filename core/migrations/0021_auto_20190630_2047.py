# Generated by Django 2.2.2 on 2019-07-01 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20190630_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksuggestion',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]