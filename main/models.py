from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=30)
    content = models.TextField()
    pub_date = models.DateTimeField()
    category = models.CharField(max_length=20)

    def summary(self):
        return self.content[:20]