#from PIL import Image, ExifTags, ImageOps
# Importing Image and ImageFont, ImageDraw module from PIL package  
from PIL import Image, ImageFont, ImageDraw  
      
# creating a image object  
image = Image.new('RGB', (922, 557), color = (255, 255, 255))
text = 'तपःस्वाध्यायनिरतं तपस्वी वाग्विदां वरम् અમને તેની BEST MEDICINE'
draw = ImageDraw.Draw(image)  
fontsize = 20  # starting font size

font = ImageFont.truetype('Lohit-Devanagari.ttf',fontsize)  
#font = ImageFont.truetype("arial.ttf", fontsize)
while font.getsize(text)[0] < 344:
    # iterate until the text size is just larger than the criteria
    fontsize += 1
    font = ImageFont.truetype('NotoSans-Regular.ttf',fontsize)

# drawing text size 
draw.text((509, 487), text, fill ="red", font = font, align ="center")  
image.save('ball.png')

#img = Image.open('c.JPG')
#img = img.resize((344, 344))
#fixed_image = ImageOps.exif_transpose(img)
#fixed_image.save("ball.png", format="png")
#n_img = Image.new('RGB', (922, 557), color = (255, 255, 255))
#n_img.paste(img,(509,119))
#n_img.save("merged_image.png","PNG")
#img_exif_dict = dict(img_exif)
    # { ... 42035: 'FUJIFILM', 42036: 'XF23mmF2 R WR', 42037: '75A14188' ... }
#for key, val in img_exif_dict.items():
#    if key in ExifTags.TAGS:
#        print(f"{ExifTags.TAGS[key]}:{repr(val)}")

#print(img._getexif())
#exif=dict((ExifTags.TAGS[k], v) for k, v in img._getexif().items() if k in ExifTags.TAGS)
#if not exif['Orientation']:
#    img=img.rotate(90, expand=True)
#img.thumbnail((1000,1000), Image.ANTIALIAS)
#img.save(output_fname, "JPEG")

#from PIL import Image, ImageDraw, ImageFilter

#im1 = Image.open('1.jpeg')
#im2 = Image.open('ABHAY2.png')
#im1 = Image.open('lena.jpg')
#im1 = im1.resize(im2.size)

#mask = Image.open('mask.png').convert('L').resize(im2.size)
#im = Image.composite(im1, im2, mask)
#im.save('ball.png')

#ironman = im1
#bg = im2
#text_img = Image.new('RGBA', (600,320), (0, 0, 0, 0))
#text_img.paste(bg, (0,0))
#text_img.paste(ironman, (0,0), mask=ironman.split()[1])
#text_img.save("ball.png", format="png")