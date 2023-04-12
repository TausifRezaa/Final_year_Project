
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_highlightsvideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='highlightsvideo',
            name='hv',
            field=models.FileField(blank=True, upload_to='highlights_video'),
        ),
    ]
