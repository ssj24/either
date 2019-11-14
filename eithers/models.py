from django.db import models

# Create your models here.
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail  

class Question(models.Model):
    title = models.CharField(max_length=50)
    issue_a = models.TextField()
    issue_b = models.TextField()
    image_a = ProcessedImageField(
        processors = [Thumbnail(200, 300)],
        format = 'JPEG',
        options = {'quaility' : 90},
        upload_to = 'eithers/images',
        blank = True,
    )

    image_b = ProcessedImageField(
        processors = [Thumbnail(200, 300)],
        format = 'JPEG',
        options = {'quaility' : 90},
        upload_to = 'eithers/images',
        blank = True,
    )


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pick = models.IntegerField()
    comment = models.TextField()
# Create your models here.