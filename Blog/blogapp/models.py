from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    images = models.ImageField(null=True,blank=True,upload_to="user_images")
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title