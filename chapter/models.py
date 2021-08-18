import uuid


from django.db import models


from course.models import Course


chapter_choices = (
    ('T', 'Text'),
    ('H', 'Heading'),
    ('V', 'Videos'),
    ('L', 'Link'),
)


class Chapter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    chapter_type = models.CharField(choices=chapter_choices, max_length=150)
    index = models.IntegerField(null=False)
    parent_chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, related_name='child_chapters')
