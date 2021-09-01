from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage


class Merged(models.Model):
    m_img = models.ImageField(default='d.png', upload_to='merged_pic')
    name = models.CharField(max_length=50, blank=False, default='')
    number = models.CharField(max_length=10, blank=False, default='')

    def __str__(self):
        return f'{self.id} merged'


class Frame(models.Model):
    frame = models.ImageField(default='d.png', upload_to='frames_pic')
    mask = models.ImageField(default='d.png', upload_to='mask_img')
    frame_heading = models.CharField(max_length=150, blank=False, default='')
    frame_desc = models.CharField(max_length=350, blank=False, default='')
    page_title = models.CharField(max_length=150, blank=False, default='')
    page_desc = models.CharField(max_length=350, blank=False, default='')
    def __str__(self):
        return f'{self.id} frame'

class Uimg(models.Model):
    img = models.ImageField(default='d.png', upload_to='user_img')

    def __str__(self):
        return f'{self.id} user pic'
