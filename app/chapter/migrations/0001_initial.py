# Generated by Django 3.2.6 on 2021-08-20 09:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('chapter_type', models.CharField(choices=[('T', 'Text'), ('H', 'Heading'), ('V', 'Videos'), ('L', 'Link')], max_length=150)),
                ('index', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='course.course')),
                ('parent_chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_chapters', to='chapter.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='VideoChapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('video_id', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('video_platform', models.CharField(choices=[('Y', 'Youtube'), ('V', 'Vimeo')], max_length=2)),
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
            name='LinkChapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('url', models.URLField(max_length=150, verbose_name='URL')),
                ('chapter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='link_chapter', to='chapter.chapter')),
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