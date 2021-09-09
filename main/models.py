from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class Campaign(models.Model):
    country_code = models.CharField(max_length=10, blank=False, default='in')
    language_code = models.CharField(max_length=10, blank=False, default='en')
    title = models.CharField(max_length=150, blank=False, default='')
    description = models.CharField(max_length=350, blank=False, default='')
    sub_title = models.CharField(max_length=150, blank=False, default='')
    sub_description = models.CharField(max_length=350, blank=False, default='')
    button = models.CharField(max_length=350, blank=False, default='')

    def __str__(self):
        return f'{self.title}'


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
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} frame'

class Uimg(models.Model):
    img = models.ImageField(default='d.png', upload_to='user_img')

    def __str__(self):
        return f'{self.id} user pic'


class Question(models.Model):
    campaign = models.ForeignKey(
                Campaign, 
                related_name="questions", 
                on_delete = models.CASCADE)

    question = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(
                Question, 
                related_name="choices", 
                on_delete = models.CASCADE)

    choice = models.CharField(max_length=50, blank=True)
    percentage = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.choice + str(self.percentage)