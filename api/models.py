from django.db import models


class Bucketlist(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)


class Comment(models.Model):
    bucketlist = models.ForeignKey(
        Bucketlist,
        related_name='comments',
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=400)
