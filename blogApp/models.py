from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300)
    date = models.DateTimeField()
    text = models.TextField(max_length=700)
    image = models.ImageField(upload_to='event_images/')

    def get_summery(self):
        if len(self.text) > 70:
            return self.text[:70] + '...'
        else:
            return self.text[:70]

    def __str__(self):
        return self.title
