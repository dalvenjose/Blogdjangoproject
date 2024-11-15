from django.db import models

class blogmodel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100 , unique= True)
    image =  models.ImageField(upload_to='blogimage', default='default\download.jpg')


    def  __str__(self):
        return self.title
    


