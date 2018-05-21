from django.db import models
from datetime import datetime
from django.db import models
from embed_video.fields import EmbedVideoField
from  django.utils.text import slugify

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.



class Posts(models.Model):

    title = models.CharField(max_length=255, blank=True, null=True)
    #description = RichTextField(blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    description2 = RichTextUploadingField(  blank=True, 
                                            null=True,
                                            config_name='special',
                                            external_plugin_resources=[(
                                                'youtube',
                                                '/static/base/vendor/ckeditor_plugins/youtube/youtube/',
                                                'plugin.js',
                                            )],         
                                            )
    body = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    
    slug = models.SlugField(default='', blank=True)

    created_at = models.DateTimeField(default=datetime.now, blank=True)
   # def save(self):
   #     self.slug = slugify(self.title)
   #     super(Posts, self).save

    def __str__(self):
        return '%s' % self.title
      #  return self.title

    class Meta:
        verbose_name_plural = "Posts"
       

"""
#OLD SIMPLE CLASS
class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at=models.DateTimeField(default=datetime.now, blank=True)
    def __str__ (self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"

""" 

               
