
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_athletes'),
    ]

    operations = [
        migrations.AddField(
            model_name='athletes',
            name='athlete_description',
            field=models.TextField(blank=True, max_length=120),
        ),
    ]
