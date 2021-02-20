from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="media/")
    body = models.TextField()

    def __str__(self):
        return self.title+"-"+self.human_readable_date()

    def human_readable_date(self):
        date = str(self.publish_date)
        return date[:date.index("+")]
    
    def publish_date_visual(self):
        return self.publish_date.strftime("%d %b %Y %H:%M")

    def summery(self):

        return self.body if len(self.body) <= 100 else self.body[:100]+"..."