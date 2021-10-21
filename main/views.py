import os
from django.conf import settings
from django.shortcuts import render
from .models import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from PIL import Image, ImageDraw, ImageFont, ImageOps
from .forms import UimgForm, QuizForm, BaseQuizFormSet
from urllib.request import urlopen
import requests
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import base64
from base64 import b64encode
from django import forms
import textwrap

def home(request):
    home = HomePage.objects.filter(country_code='in', language_code='en').first()
    campaign = Campaign.objects.filter(homepage=home).order_by('-pk')
    context = locals()
    return render(request, 'main/home.html', context)

def index(request, country_code, language_code):
    home = HomePage.objects.filter(country_code=country_code, language_code=language_code).first()
    if home is None:
        pass
    campaign = Campaign.objects.filter(homepage=home).order_by('-pk')
    context = locals()
    return render(request, 'main/home.html', context)

def campaign(request, campaign_id):
    campaign = Campaign.objects.get(pk=campaign_id)
    frames = Frame.objects.filter(campaign=campaign).order_by('-pk')
    context = locals()
    return render(request, 'main/index.html', context)

def upload(request, frame_id, campaign_id):
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
            commitment = form.cleaned_data.get('commitment')

            i_rgb = Image.open(img)
            if i_rgb.mode != "RGB":
                i_rgb.convert('RGB')
            i = ImageOps.exif_transpose(i_rgb)

            frame = Frame.objects.get(id=frame_id)
            frame_img_obj = frame.frame.file
            mask_img_obj = Frame.objects.filter(id=frame_id).first().mask.file
            f = Image.open(frame_img_obj)
            m = Image.open(mask_img_obj).convert('L').resize(f.size)

            cropped_image = i.crop((x, y, w+x, h+y))
            new = cropped_image.resize((215, 215), Image.ANTIALIAS)
            resized_image = Image.new('RGB', (f.size), color = (255, 255, 255))
            resized_image.paste(new, (frame.print_image.x, frame.print_image.y))

            if f.mode != "RGB":
                f.convert('RGB')

            f = Image.composite(resized_image, f, m)
            draw = ImageDraw.Draw(f)
            name_f = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'Montserrat-Bold.ttf'), frame.print_name.font_size)
            designation_f = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'Montserrat-Medium.ttf'), frame.print_designation.font_size)
            commitment_f = ImageFont.truetype(os.path.join(settings.BASE_DIR, 'Montserrat-Bold.ttf'), frame.print_commitment.font_size)
            #while font.getsize(info)[0] < 306:
                #fontsize += 1
                #font = ImageFont.truetype('HindVadodara-Medium.ttf', fontsize)  
            draw.text((frame.print_name.x, frame.print_name.y), name, fill =(1, 1, 1), font = name_f, align ="center") 
            draw.text((frame.print_designation.x, frame.print_designation.y), designation, fill =(1, 1, 1), font = designation_f, align ="center")
            lines = textwrap.wrap(commitment, width=25)
            image_width  = frame.print_commitment.x
            y_text = frame.print_commitment.y

            for line in lines:
                line_width, line_height = commitment_f.getsize(line)
                draw.text((image_width, y_text), 
                          line, fill =(1, 1, 1), font = commitment_f, align ="center")
                y_text += line_height

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
    frame_img = Frame.objects.filter(id=frame_id).first()
    campaign = Campaign.objects.filter(id=campaign_id).first()
    context = locals()
    return render(request, 'main/upload.html', context)

def quiz(request, campaign_id):
    queryset = list(Question.objects.filter(campaign=campaign_id).all())
    QuizFormSet = forms.formset_factory(QuizForm, formset=BaseQuizFormSet, extra=len(queryset)) 
    formset = QuizFormSet(form_kwargs={'questions': queryset})
    if request.method == 'POST':
        print(request.POST)
        formset = QuizFormSet(request.POST, form_kwargs={'questions': queryset})
        if formset.is_valid():
            for form in formset:
                print(form.cleaned_data.get('answer'))
    else:
        print('form invalid')
        formset = QuizFormSet(form_kwargs={'questions': queryset})
    context = locals()
    return render(request, 'main/quiz.html', context)   