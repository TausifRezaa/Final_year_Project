# Generated by Django 4.1.1 on 2022-09-20 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(choices=[('JPN', 'Japan'), ('USA', 'USA'), ('UK', 'England'), ('NP', 'Nepal')], max_length=25),
        ),
    ]
