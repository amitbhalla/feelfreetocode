# Generated by Django 3.2.6 on 2021-08-18 05:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chapter', '0002_linkchapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkchapter',
            name='url',
            field=models.URLField(max_length=150, verbose_name='URL'),
        ),
        migrations.CreateModel(
            name='VideoChapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('video_id', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('video_plateform', models.CharField(choices=[('Y', 'Youtube'), ('V', 'Vimeo')], max_length=2)),
                ('chapter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='video_chapter', to='chapter.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='TextChapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('chapter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='text_chapter', to='chapter.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='HeadingChapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('chapter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='heading_chapter', to='chapter.chapter')),
            ],
        ),
    ]