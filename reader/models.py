from django.db import models

# Create your models here.
class Book(models.Model):

    name = models.CharField(max_length=255, null=True, blank=True)

    short_description = models.TextField(max_length=500, null=True, blank=True)

    expire_date = models.DateField(blank=True, null=True)

    attachment_file = models.FileField(upload_to='reader/book/', max_length=500, null=True, blank=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name   