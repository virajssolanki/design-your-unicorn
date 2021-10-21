from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class HomePage(models.Model):
    country_code = models.CharField(max_length=10, blank=False, default='in')
    language_code = models.CharField(max_length=10, blank=False, default='en')
    title = models.CharField(max_length=150, 
                                blank=True, default='',
                                verbose_name="HomePage Title", 
                                help_text="Bold text on first page user land -hero-section")

    description = models.TextField(max_length=350, 
                                blank=False, default='',
                                verbose_name="HomePage Description", 
                                help_text="description will display on home page below Title -hero-section")

    background = models.ImageField(default='d.png', 
                                upload_to='home',
                                verbose_name="Home page main banner",
                                help_text="Background Image for home page hero-section")

    def __str__(self):
        return f'{self.title}'

class Campaign(models.Model):
    homepage = models.ForeignKey(HomePage, on_delete = models.CASCADE, 
                                    blank=True,
                                    related_name="campaign", 
                                    verbose_name="homepage",
                                    help_text="select the home page within wich these campaign will be displayed.")

    title = models.CharField(max_length=150, 
                                blank=False, default='',
                                verbose_name="Campaign Title", 
                                help_text="eg. Entrepreneurs, Mentors")

    description = models.TextField(max_length=350, 
                                blank=False, default='',
                                verbose_name="Campaign Description", 
                                help_text="description will display on home page")

    commitment_section_title = models.CharField(max_length=150, 
                                blank=False, default='',
                                verbose_name="Campaign Sub Title", 
                                help_text="eg. make a commitment to yourself")

    commitment_section_description = models.TextField(max_length=350, 
                                blank=False, default='',
                                verbose_name="Campaign Sub Description", 
                                help_text="eg. Select the frame and create your custom image to share with the world.")

    icon = models.ImageField(default='d.png', 
                                upload_to='Campaign',
                                verbose_name="choose icon for Campaign",
                                help_text="icon will display on home page")
    
    background = models.ImageField(default='d.png', 
                                upload_to='Campaign',
                                verbose_name="background banner image for Campaign",
                                help_text="icon will display on home page")

    cta = models.CharField(max_length=150, 
                                blank=False, default='',
                                verbose_name="Call to action button name", 
                                help_text="This will be the button name on home page")

    def __str__(self):
        return f'{self.title}'


class Merged(models.Model):
    m_img = models.ImageField(default='d.png', upload_to='merged_pic')
    name = models.CharField(max_length=50, blank=False, default='')
    number = models.CharField(max_length=10, blank=False, default='')

    def __str__(self):
        return f'{self.id} merged'

class PrintName(models.Model):
    font_size = models.IntegerField(blank=False, default=25, 
                                        verbose_name='font size',
                                        help_text='font size to print name on image')

    x = models.IntegerField(blank=False, default=47, 
                                        verbose_name='x coordinate',
                                        help_text='x coordinate to print name on image, it helps to decide position')

    y = models.IntegerField(blank=False, default=634, 
                                        verbose_name='y coordinate',
                                        help_text='y coordinate to print name on image, it helps to decide position')

    def __str__(self):
        return  f"font size-{str(self.font_size)} x-{str(self.x)} y-{str(self.y)}"

class PrintDesignation(models.Model):
    font_size = models.IntegerField(blank=False, default=20, 
                                        verbose_name='font size',
                                        help_text='font size to print designation on image')

    x = models.IntegerField(blank=False, default=47, 
                                        verbose_name='x coordinate',
                                        help_text='x coordinate to print designation on image, it helps to decide position')

    y = models.IntegerField(blank=False, default=677, 
                                        verbose_name='y coordinate',
                                        help_text='y coordinate to print designation on image, it helps to decide position')

    def __str__(self):
        return  f"font size-{str(self.font_size)} x-{str(self.x)} y-{str(self.y)}"

class PrintCommitment(models.Model):
    font_size = models.IntegerField(blank=False, default=27, 
                                        verbose_name='font size',
                                        help_text='font size to print commitment on image')

    x = models.IntegerField(blank=False, default=714, 
                                        verbose_name='x coordinate',
                                        help_text='x coordinate to print commitment on image, it helps to decide position')

    y = models.IntegerField(blank=False, default=634, 
                                        verbose_name='y coordinate',
                                        help_text='y coordinate to print commitment on image, it helps to decide position')

    def __str__(self):
        return  f"font size-{str(self.font_size)} x-{str(self.x)} y-{str(self.y)}"

class PrintImage(models.Model):
    x = models.IntegerField(blank=False, default=369, 
                                        verbose_name='x coordinate',
                                        help_text='x coordinate to print photo on image, it helps to decide position')

    y = models.IntegerField(blank=False, default=669, 
                                        verbose_name='y coordinate',
                                        help_text='y coordinate to print photo on image, it helps to decide position')

    def __str__(self):
        return  f"x-{str(self.x)} y-{str(self.y)}"

class Userinfo(models.Model):
    name = models.CharField(max_length=40, blank=False, default='Name',
                                verbose_name="Form name field")
    email = models.EmailField(blank=True, 
                                verbose_name="Form email field")
    designation = models.CharField(max_length=40, blank=False, default=' ',
                                verbose_name="Form designation field")
    company_name = models.CharField(max_length=40, blank=False, default=' ',
                                verbose_name="Form Company name field")
    commitment = models.CharField(max_length=40, blank=False, default='Name',
                                verbose_name="Form Company name field")

class Frame(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    # user_info = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    frame = models.ImageField(default='d.png', upload_to='frames_pic')
    mask = models.ImageField(default='d.png', upload_to='mask_img')
    frame_heading = models.CharField(max_length=150, blank=False, default='')
    frame_desc = models.CharField(max_length=350, blank=False, default='')
    page_title = models.CharField(max_length=150, blank=False, default='')
    page_desc = models.CharField(max_length=350, blank=False, default='')
    cta = models.CharField(max_length=150, blank=False, default='',
                                verbose_name="Call to action button name", 
                                help_text="This will display under frame image")
    print_name = models.ForeignKey(PrintName, on_delete=models.CASCADE)
    print_designation = models.ForeignKey(PrintDesignation, on_delete=models.CASCADE)
    print_commitment = models.ForeignKey(PrintCommitment, on_delete=models.CASCADE)
    print_image = models.ForeignKey(PrintImage, on_delete=models.CASCADE)

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