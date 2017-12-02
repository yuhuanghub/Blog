from django.db import models

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
    title_image = models.ForeignKey(Category_img)
    data_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    category = models.ForeignKey(Category)
    views = models.PositiveIntegerField(default=0)

    def increat_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        ordering = ['-data_time']

