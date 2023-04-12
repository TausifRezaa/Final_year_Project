
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_highlightsvideo_hv'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='broadcastvideo',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='broadcast_views', to='games.ipmodel'),
        ),
    ]
