
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20220923_0724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Athletes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('athlete_name', models.CharField(max_length=255)),
                ('athlete_image', models.ImageField(blank=True, upload_to='athlete_image')),
                ('athlete_game', models.CharField(max_length=255)),
                ('athlete_country', models.CharField(max_length=255)),
            ],
        ),
    ]
