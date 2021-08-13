from PIL import Image, ImageDraw

im1 = Image.open('lena.jpg')
im2 = Image.open('ABHAY2.png')

# Transparency
newImage = []
for item in im2.getdata():
    if item[3] == 0:
        newImage.append((0, 0, 0, 1))
    else:
        newImage.append((255, 255, 255, 1))
n_image = Image.new('RGB',im2.size, (250,250,250))  
n_image.putdata(newImage)
n_image = n_image.convert('L').resize(im2.size)

im = Image.composite(im1, im2, n_image)
im.save('ball.png')

#im1.paste(image,(0,0))
#resize, first image
#im1 = im1.resize(im2.size)
#im2.putalpha(255)
#image2_size = image2.size
#new_image = Image.new('RGB',image2.size, (250,250,250))
#new_image.paste(image1,(0,0))
#image2.paste(image1, (0, 0), mask_im)
#im = Image.composite(im1, im2, mask)
#im1.paste(im2,(0,0))
#im_invert = ImageOps.invert(mask)
#im.save("merged_image.png","PNG")