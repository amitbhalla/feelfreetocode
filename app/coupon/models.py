import uuid
import shortuuid

from django.db import models

from course.models import Course


def random_code():
    return shortuuid.ShortUUID().random(length=6).upper()


class Coupon(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    discount = models.IntegerField()
    active = models.BooleanField(default=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="coupans"
    )
    code = models.CharField(
        max_length=6, null=False, unique=True, default=random_code
    )

    def __str__(self):
        name = str(self.code) + " - " + str(self.course)
        return name
