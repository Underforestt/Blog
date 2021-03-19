from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    text = models.TextField(max_length=300)
    image = models.ImageField(upload_to='event_images/')

    def get_summery(self):
        return self.text[:70]
