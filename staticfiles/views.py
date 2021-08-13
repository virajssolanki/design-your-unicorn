from django.shortcuts import render
from .models import Frame, Uimg, Merged
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from PIL import Image, ImageDraw, ImageFont
from .forms import UimgForm
from urllib.request import urlopen
import requests
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def home(request):
    frames = Frame.objects.all()
    context = locals()
    return render(request, 'main/home.html', context)

def simple_upload(request, pk):
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
            village = form.cleaned_data.get('village')
            number = form.cleaned_data.get('number')
            #nl = '\n'
            #info= f'Name: {name}{nl}Village: {village}'

            i = Image.open(img)
            if i.mode != "RGB":
                i.convert('RGB')

            frame_img_obj = Frame.objects.filter(id=pk).first().frame.file
            mask_img_obj = Frame.objects.filter(id=pk).first().mask.file
            f = Image.open(frame_img_obj)
            m = Image.open(mask_img_obj).convert('L').resize(f.size)

            cropped_image = i.crop((x, y, w+x, h+y))
            resized_image = cropped_image.resize((f.size), Image.ANTIALIAS)
            thumb_io = BytesIO()
            resized_image.save(thumb_io, format='PNG', quality=80)
            inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, None, 'user_img.png', 
                                              'image/png', thumb_io.tell(), None)
            instance = Uimg()
            instance.img = inmemory_uploaded_file
            instance.save()


            if f.mode != "RGB":
                f.convert('RGB')

            #draw = ImageDraw.Draw(f)
            #draw.text((5, 5), info ,(255,255,255))

            f = Image.composite(resized_image, f, m)

            #f.paste(resized_image,(322,45))
            thumb_io = BytesIO()
            f.save(thumb_io, format='PNG', quality=80)
            f_inmemory_uploaded_file = InMemoryUploadedFile(thumb_io, None, 'merge.png', 
                                              'image/png', thumb_io.tell(), None)
            f_instance = Merged()
            f_instance.m_img = f_inmemory_uploaded_file
            f_instance.name = name
            f_instance.village = village
            f_instance.number = number
            f_instance.save()
    else:
        form = UimgForm()

    frame_img = Frame.objects.filter(id=pk).first()
    context = locals()
    return render(request, 'main/upload.html', context)