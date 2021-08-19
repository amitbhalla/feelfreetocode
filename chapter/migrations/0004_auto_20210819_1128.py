# Generated by Django 3.2.6 on 2021-08-19 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0003_auto_20210818_0507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videochapter',
            old_name='video_plateform',
            new_name='video_platform',
        ),
        migrations.AlterField(
            model_name='chapter',
            name='parent_chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_chapters', to='chapter.chapter'),
        ),
    ]