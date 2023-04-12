
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_ipmodel_broadcast_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hitcount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hit_count', models.CharField(max_length=100)),
                ('broadcast', models.CharField(max_length=255)),
                ('broadcast_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='IpModel',
        ),
        migrations.AlterField(
            model_name='broadcastvideo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='gamescategory',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='highlightsvideo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='scoreboards',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
