
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_rename_ip_ipmodel_hit_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipmodel',
            name='broadcast_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
