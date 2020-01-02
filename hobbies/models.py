from django.db import models
from imagekit.models import ProcessedImageField


# Create your models here.
class illustrations(models.Model):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        null=True,
        blank=True,
        )
    id = models.CharField(primary_key=True,max_length=200)
    title = models.CharField(max_length=200,null=True)
    Comments = models.CharField(max_length=1000,null=True)

    class Meta:
            managed = True
            db_table = 'illstrations'

    def __str__(self):
        return self.title