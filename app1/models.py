from django.db import models
import os.path
import datetime

def update_filename(instance, filename):
    path = "documents/"
    now = datetime.datetime.now()
    format = now.strftime('%Y%m%d_%H%M%S') + '.jpg'
    return os.path.join(path, format)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to=update_filename, default='defo')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    output = models.ImageField(default = 'output/output.jpg')
