from django.db import models
from imagekit.models import ProcessedImageField


# Create your models here.
class Illustrations(models.Model):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        null=True,
        blank=True,
        )
    id = models.CharField(primary_key=True,max_length=200)
    title = models.CharField(max_length=200,null=True)
    Comments = models.CharField(max_length=1000,null=True)
    priority=models.IntegerField(default=0)

    class Meta:
            managed = True
            db_table = 'illustrations'
            ordering = ['-priority']

    def __str__(self):
        return self.title
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Photographies(models.Model):
    profile_pic = ProcessedImageField(
        upload_to='static/images/profiles',
        format='JPEG',
        null=True,
        blank=True,
        )
    id = models.CharField(primary_key=True,max_length=200)
    # post=models.ManyToManyField(Post,related_name='post')
    
    # priority=models.IntegerField(default=0)

    class Meta:
            managed = True
            db_table = 'photographies'

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(max_length=200, unique=True)
    # author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    photos=models.ManyToManyField(Photographies,related_name='photos')

    class Meta:
        managed = True
        db_table = 'post'
        ordering = ['-created_on']

    def __str__(self):
        return self.title
