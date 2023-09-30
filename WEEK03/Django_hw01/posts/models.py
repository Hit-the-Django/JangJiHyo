from django.db import models

# Create your models here.

class Profile (models.Model):
        
        name = models.CharField('이름', max_length=200)
        profile_image=models.ImageField(height_field=None, width_field=None)
        age = models.IntegerField('나이',default=20)
        contents = models.TextField('내용')
        email=models.EmailField(blank=True)
        website=models.URLField(max_length=250)

class Post (models.Model):
    
    image= models.ImageField(verbose_name='이미지')
    contents = models.TextField('내용')
    created_at= models.DateTimeField('작성일')
    view_count= models.IntegerField('조회수')
   




    