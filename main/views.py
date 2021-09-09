import os
from django.conf import settings
from django.shortcuts import render
from .models import Frame, Uimg, Merged, Campaign
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from PIL import Image, ImageDraw, ImageFont, ImageOps
from .forms import UimgForm
from urllib.request import urlopen
import requests
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import base64
from base64 import b64encode

def home(request):
    frames = Frame.objects.all().order_by('-pk')
    context = locals()
    return render(request, 'main/home.html', context)


def index(request, country_code, language_code):
    campaign = Campaign.objects.filter(country_code=country_code).filter(language_code=language_code).first()
    frames = Frame.objects.filter(campaign=campaign).order_by('-pk')
    context = locals()
    print(context)
    return render(request, 'main/index.html', context)


# def simple_upload(request, pk):
#     if request.method == 'POST':
#         form = UimgForm(request.POST, request.FILES)
#         if form.is_valid():
#             files = request.FILES
#             img = files.get("img")
#             x = form.cleaned_data.get('x')
#             y = form.cleaned_data.get('y')
#             w = form.cleaned_data.get('width')
#             h = form.cleaned_data.get('height')
#             name = form.cleaned_data.get('name')
#             village = form.cleaned_data.get('village')
#             number = form.cleaned_data.get('number')
#             #nl = '\n'
#             #info= f'Name: {name}{nl}Village: {village}'

#             i_rgb = Image.open(img)
#             if i_rgb.mode != "RGB":
#                 i_rgb.convert('RGB')
#             i = ImageOps.exif_transpose(i_rgb)

#             frame_img_obj = Frame.objects.filter(id=pk).first().frame.file
#             mask_img_obj = Frame.objects.filter(id=pk).first().mask.file
#             f = Image.open(frame_img_obj)
#             m = Image.open(mask_img_obj).convert('L').resize(f.size)

#             cropped_image = i.crop((x, y, w+x, h+y))
#             resized_image = cropped_image.resize((f.size), Image.ANTIALIAS)
#             #thumb_io = BytesIO()
#             #resized_image.save(thumb_io, format='PNG', quality=80)
#             #inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, None, 'user_img.png', 
#             #                                 'image/png', thumb_io.tell(), None)
#             #instance = Uimg()
#             #instance.img = inmemory_uploaded_file
#             #instance.save()


#             if f.mode != "RGB":
#                 f.convert('RGB')

#             #draw = ImageDraw.Draw(f)
#             #draw.text((51, 51), info ,(255,255,255))

#             f = Image.composite(resized_image, f, m)

#             #f.paste(resized_image,(322,45))
#             thumb_io = BytesIO()
#             f.save(thumb_io, format='PNG', quality=80)
#             encoded_img = base64.b64encode(thumb_io.getvalue())
#             decoded_img = encoded_img.decode('utf-8')
#             img_data = f"data:image/png;base64,{decoded_img}"
#             #f_inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, None, 'merge.png', 
#             #                                 'image/png', thumb_io.tell(), None)
#             f_instance = Merged()
#             #f_instance.m_img = f_inmemory_uploaded_file
#             f_instance.name = name
#             f_instance.village = village
#             f_instance.number = number
#             f_instance.save()
#     else:
#         form = UimgForm()

#     context = locals()
#     return render(request, 'main/upload.html', context)

def upload(request, pk):
    if request.method == 'POST':
        form = UimgForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES
            img = files.get("img")
            x = form.cleaned_data.get('x')
            y = form.cleaned_data.get('y')
            w = form.cleaned_data.get('width')
            h = form.cleaned_data.get('height')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            designation = form.cleaned_data.get('designation')
            company_name = form.cleaned_data.get('company_name')
            commitment_1 = form.cleaned_data.get('commitment_1')
            commitment_2 = form.cleaned_data.get('commitment_2')

            i_rgb = Image.open(img)
            if i_rgb.mode != "RGB":
                i_rgb.convert('RGB')
            i = ImageOps.exif_transpose(i_rgb)

            frame_img_obj = Frame.objects.filter(id=pk).first().frame.file
            mask_img_obj = Frame.objects.filter(id=pk).first().mask.file
            f = Image.open(frame_img_obj)
            m = Image.open(mask_img_obj).convert('L').resize(f.size)

            cropped_image = i.crop((x, y, w+x, h+y))
            new = cropped_image.resize((215, 215), Image.ANTIALIAS)
            resized_image = Image.new('RGB', (f.size), color = (255, 255, 255))
            resized_image.paste(new, (349, 439))

            if f.mode != "RGB":
                f.convert('RGB')

            f = Image.composite(resized_image, f, m)
            draw = ImageDraw.Draw(f)
            name_f = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'Montserrat-Bold.ttf'), 20)
            designation_f = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'Montserrat-Medium.ttf'), 16)
            company_f = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'Montserrat-Italic.ttf'), 15)
            index_f = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'Montserrat-Bold.ttf'), 26)
            commitment_f = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'Montserrat-Bold.ttf'), 21)
            #while font.getsize(info)[0] < 306:
                #fontsize += 1
                #font = ImageFont.truetype('HindVadodara-Medium.ttf', fontsize)  
            draw.text((56, 713), name, fill =(1, 1, 1), font = name_f, align ="center") 
            draw.text((56, 750), designation, fill =(1, 1, 1), font = designation_f, align ="center")
            draw.text((56, 773), company_name, fill =(1, 1, 1), font = designation_f, align ="center") 
            draw.text((223, 848), '8', fill =(1, 1, 1), font = index_f, align ="center") 
            draw.text((808, 698), commitment_1, fill =(1, 1, 1), font = commitment_f, align ="center") 
            draw.text((648, 768), commitment_2, fill =(1, 1, 1), font = commitment_f, align ="center") 

            thumb_io = BytesIO()
            f.save(thumb_io, format='PNG', quality=80)
            thumb_io = BytesIO()
            f.save(thumb_io, format='PNG', quality=80)
            encoded_img = base64.b64encode(thumb_io.getvalue())
            decoded_img = encoded_img.decode('utf-8')
            img_data = f"data:image/png;base64,{decoded_img}"

            f_instance = Merged()
            #f_instance.m_img = f_inmemory_uploaded_file
            #f_instance.name = name
            #f_instance.village = village
            #f_instance.number = number
            f_instance.save()
    else:
        form = UimgForm()
        
    frame_img = Frame.objects.filter(id=pk).first()
    context = locals()
    return render(request, 'main/upload.html', context)