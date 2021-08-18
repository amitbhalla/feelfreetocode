# Generated by Django 3.2.6 on 2021-08-18 04:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0005_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('chapter_type', models.CharField(choices=[('T', 'Text'), ('H', 'Heading'), ('V', 'Videos'), ('L', 'Link')], max_length=150)),
                ('index', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='course.course')),
                ('parent_chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_chapters', to='chapter.chapter')),
            ],
        ),
    ]
