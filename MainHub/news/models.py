from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField
class Article(models.Model):
    title=models.CharField(max_length=150,unique=True)
    slug = models.CharField(max_length=150, unique=True)
    image = models.ImageField(upload_to="Slider")
    created_at = models.DateField()
    description=RichTextField()
    status=models.BooleanField(default=0)

#name of object as title
def _str_(self):
	return self.title