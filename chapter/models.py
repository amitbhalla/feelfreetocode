import uuid


from django.db import models


from course.models import Course


chapter_choices = (
    ("T", "Text"),
    ("H", "Heading"),
    ("V", "Videos"),
    ("L", "Link"),
)
chapter_choises_description = (
    (
        "T",
        "Create your textual lessons in the course. It can also be used to embed iFrame, add HTML code through the Source option",
    ),
    ("H", "Define your chapter or section headings."),
    (
        "V",
        "All uploaded videos are completely secure and non downloadable. It can also be used to embed youtube and Vimeo videos.",
    ),
    ("L", "Add Link which will be embedded in iFrame"),
)
video_platform_choises = (
    ("Y", "Youtube"),
    ("V", "Vimeo"),
)


# Holds the chapter object
class Chapter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="chapters"
    )
    chapter_type = models.CharField(choices=chapter_choices, max_length=150)
    index = models.IntegerField(null=False)
    parent_chapter = models.ForeignKey(
        "Chapter",
        on_delete=models.CASCADE,
        related_name="child_chapters",
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.course)


# Object inside a chapter
class TextChapter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    chapter = models.OneToOneField(
        Chapter, on_delete=models.CASCADE, related_name="text_chapter"
    )
    title = models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.title


# Object inside a chapter
class HeadingChapter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    chapter = models.OneToOneField(
        Chapter, on_delete=models.CASCADE, related_name="heading_chapter"
    )
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


# Object inside a chapter
class VideoChapter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    chapter = models.OneToOneField(
        Chapter, on_delete=models.CASCADE, related_name="video_chapter"
    )
    title = models.CharField(max_length=150)
    video_id = models.CharField(max_length=150, unique=False)
    description = models.TextField()
    video_platform = models.CharField(
        choices=video_platform_choises, max_length=2
    )

    def __str__(self):
        return self.title


# Object inside a chapter
class LinkChapter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    chapter = models.OneToOneField(
        Chapter, on_delete=models.CASCADE, related_name="link_chapter"
    )
    title = models.CharField(max_length=150)
    url = models.URLField("URL", max_length=150)

    def __str__(self):
        return self.title
