
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_ipmodel_broadcastvideo_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ipmodel',
            old_name='ip',
            new_name='hit_count',
        ),
        migrations.RemoveField(
            model_name='broadcastvideo',
            name='views',
        ),
        migrations.AddField(
            model_name='ipmodel',
            name='broadcast',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
