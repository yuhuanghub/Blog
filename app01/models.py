from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    caption = models.CharField(max_length=16)

    def __str__(self):
        return self.caption

class Category_img(models.Model):
    name = models.CharField(max_length=20,null=True)
    image = models.URLField(max_length=100,null=True)

    def __str__(self):
        return self.name
class Article(models.Model):
    title = models.CharField(max_length=100)
    #title_image =models.URLField(max_length=200,null=True,default='http://i2.bvimg.com/620816/a0cc009306821447.jpg')
    title_image = models.ForeignKey(Category_img)
    data_time = models.DateTimeField(auto_now_add=True)
    content = RichTextField(blank=True,verbose_name='内容')

    category = models.ForeignKey(Category)

    class Meta:
        ordering = ['-data_time']

